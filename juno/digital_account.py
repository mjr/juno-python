from juno.resources import handler_request
from juno.resources.routes import digital_account_routes


def create(dictionary):
    return handler_request.post(digital_account_routes.get_base_url(), dictionary)


def find_by_resource_token(resource_token=None):
    return handler_request.get(
        digital_account_routes.get_base_url(),
        {"resource_token": resource_token} if resource_token else {},
    )
