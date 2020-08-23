from datetime import datetime

from requests import Session
from requests.adapters import HTTPAdapter
from requests.auth import _basic_auth_str
from requests.packages.urllib3.util.retry import Retry

from juno import sdk


def headers():
    from .handler_request import request_authorization, KEYS

    if datetime.now() > KEYS["expires"]:
        request_authorization()

    _headers = {
        "Authorization": f"Bearer {KEYS['access_token']}",
        "X-API-Version": sdk.VERSION,
        "X-Resource-Token": KEYS["resource_token"],
        "Content-Type": "application/json",
    }
    return _headers


def headers_authorization():
    from .handler_request import KEYS

    _headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": _basic_auth_str(KEYS["client_id"], KEYS["client_secret"]),
    }
    return _headers


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
    authorization=False,
):
    session = session or Session()
    session.headers.update(headers_authorization() if authorization else headers())

    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    return session
