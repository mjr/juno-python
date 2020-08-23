from datetime import datetime, timedelta

from juno.exceptions import JunoException, JunoInvalidCredentials
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
        raise JunoInvalidCredentials("Invalid credentials")

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
        raise JunoException(
            data["details"][0]["message"],
            data["timestamp"],
            data["details"][0]["error_code"],
            data["status"],
            data["error"],
            data["path"],
        )

    raise Exception(data)

