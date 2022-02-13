from juno.resources import handler_request
from juno.resources.routes import plan_routes


def create(dictionary):
    return handler_request.post(plan_routes.get_base_url(), dictionary)


def find_all(size=10):
    return handler_request.get(f"{plan_routes.get_base_url()}/?pageSize={size}")


def find_by_id(plan_id):
    return handler_request.get(plan_routes.get_specific_plan_by_id_url(plan_id))


def deactivation(plan_id):
    return handler_request.post(plan_routes.get_deactivation_plan_url(plan_id))


def activation(plan_id):
    return handler_request.post(plan_routes.get_activation_plan_url(plan_id))
