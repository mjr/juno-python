from juno.resources import handler_request
from juno.resources.routes import onboarding_routes


def account_new_onboarding_request(dictionary):
    return handler_request.post(onboarding_routes.get_base_url(), dictionary)