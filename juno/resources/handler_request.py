from datetime import datetime, timedelta

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
    # if juno_response.status_code in [403, 401] and not resend:
    #     request_authorization()

    response_json = underscoreize(juno_response.json())
    if juno_response.ok:
        return response_json
    else:
        return error(response_json)


def init(client_id=None, client_secret=None, resource_token=None, sandbox=True):
    if not client_id or not client_secret or not resource_token:
        raise Exception("Invalid credentials")

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


def delete(end_point, data={}):
    juno_response = requests_retry_session().delete(end_point, json=camelize(data))
    return validate_response(juno_response)


def get(end_point, data={}):
    juno_response = requests_retry_session().get(end_point, json=camelize(data))
    return validate_response(juno_response)


def post(end_point, data={}):
    juno_response = requests_retry_session().post(end_point, json=camelize(data))
    return validate_response(juno_response)


def put(end_point, data={}):
    juno_response = requests_retry_session().put(end_point, json=camelize(data))
    return validate_response(juno_response)


def error(data):
    if "errors" in data:
        raise Exception(data["errors"])

    raise Exception(data)

