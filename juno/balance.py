from juno.resources import handler_request
from juno.resources.routes import balance_routes


def find_by_resource_token(resource_token=None):
    return handler_request.get(
        balance_routes.get_base_url(),
        {"resource_token": resource_token} if resource_token else {},
    )
