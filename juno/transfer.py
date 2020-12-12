from juno.resources import handler_request
from juno.resources.routes import transfer_routes


def create(dictionary, resource_token=None):
    if resource_token:
        dictionary["resource_token"] = resource_token

    return handler_request.post(transfer_routes.get_base_url(), dictionary)
