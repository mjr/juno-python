from datetime import datetime, timedelta

from juno import exceptions
from juno.utils import camelize, underscoreize

from .requests_retry import requests_retry_session


scheme = "https"
path_authorization = "/authorization-server/oauth/token"

KEYS = {}
RESOURCE_SERVER_URL = ""
AUTHORIZATION_URL = ""


def data_authorization():
    _data = {"grant_type": "client_credentials"}
    return _data


def dict_to_keys(dictionary):
    global KEYS

    for key, value in dictionary.items():
        if key == "expires_in":
            KEYS["max_age"] = value
            KEYS["expires"] = datetime.now() + timedelta(seconds=value)
        else:
            KEYS[key] = value


def request_authorization():
    dict_to_keys(
        validate_response(
            requests_retry_session(authorization=True).post(
                AUTHORIZATION_URL, data=data_authorization()
            )
        )
    )


def validate_response(juno_response):
    if juno_response.status_code == 204:
        return None

    response_json = underscoreize(juno_response.json())
    if juno_response.ok:
        return response_json
    else:
        return error(response_json)


def init(client_id=None, client_secret=None, resource_token=None, sandbox=True):
    if not client_id or not client_secret or not resource_token:
        raise exceptions.JunoInvalidCredentials("Invalid credentials")

    global KEYS, AUTHORIZATION_URL, RESOURCE_SERVER_URL
    KEYS["client_id"] = client_id
    KEYS["client_secret"] = client_secret
    KEYS["resource_token"] = resource_token

    host = "sandbox.boletobancario.com" if sandbox else "api.juno.com.br"
    path = "/api-integration" if sandbox else ""

    RESOURCE_SERVER_URL = f"{scheme}://{host}{path}"
    AUTHORIZATION_URL = f"{scheme}://{host}{path_authorization}"

    request_authorization()


def get_resource_url():
    return RESOURCE_SERVER_URL


def request_function(method):
    if method == "GET":
        return requests_retry_session().get
    elif method == "POST":
        return requests_retry_session().post
    elif method == "PUT":
        return requests_retry_session().put
    elif method == "DELETE":
        return requests_retry_session().delete
    elif method == "PATCH":
        return requests_retry_session().patch


def hook_requests(method, end_point, data):
    juno_response = request_function(method)(end_point, json=camelize(data))

    if juno_response.status_code in [401, 403]:
        request_authorization()
        return request_function(method)(end_point, json=camelize(data))

    return juno_response


def get(end_point, data={}):
    return validate_response(hook_requests("GET", end_point, data))


def post(end_point, data={}):
    return validate_response(hook_requests("POST", end_point, data))


def put(end_point, data={}):
    return validate_response(hook_requests("PUT", end_point, data))


def delete(end_point, data={}):
    return validate_response(hook_requests("DELETE", end_point, data))


def patch(end_point, data={}):
    return validate_response(hook_requests("PATCH", end_point, data))


def error(data):
    if "details" in data:
        raise_exception_from_error_code(
            data["details"][0]["error_code"], data["details"][0]["message"]
        )

    raise Exception(data)


capture_value_greater_than_authorized_value_error_code = "289999"
capture_value_greater_than_authorized_value_message = (
    "O valor informado na captura é maior que o valor autorizado"
)

not_found_credit_card_by_hash_error_code = "501008"

operation_failed_error_code = "373014"

invalid_credit_card_error_code = "289999"
invalid_credit_card_message = "Não autorizado. Cartão inválido."

restricted_credit_card_error_code = "289999"
restricted_credit_card_message = None

credit_card_with_insufficient_balance_error_code = "289999"
credit_card_with_insufficient_balance_message = "Não autorizado. Saldo insuficiente."

already_registered_webhook_for_indicated_events_error_code = "441009"


def raise_exception_from_error_code(error_code, message=None):
    if error_code == not_found_credit_card_by_hash_error_code:
        raise exceptions.JunoNotFoundCreditCardByHash(message)
    elif (
        error_code == credit_card_with_insufficient_balance_error_code
        and message == credit_card_with_insufficient_balance_message
    ):
        raise exceptions.JunoCreditCardWithInsufficientBalance(message)
    elif (
        error_code == restricted_credit_card_error_code
        and message == restricted_credit_card_message
    ):
        raise exceptions.JunoRestrictedCreditCard(message)
    elif (
        error_code == invalid_credit_card_error_code
        and message == invalid_credit_card_message
    ):
        raise exceptions.JunoInvalidCreditCard(message)
    elif error_code == operation_failed_error_code:
        raise exceptions.JunoOperationFailed(message)
    elif (
        error_code == capture_value_greater_than_authorized_value_error_code
        and message == capture_value_greater_than_authorized_value_message
    ):
        raise exceptions.JunoCaptureValueGreaterThanAuthorizedValue(message)
    elif error_code == already_registered_webhook_for_indicated_events_error_code:
        raise exceptions.JunoAlreadyRegisteredWebhookForIndicatedEvents(message)
    else:
        raise exceptions.JunoException(message)

