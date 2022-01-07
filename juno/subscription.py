from juno.resources import handler_request
from juno.resources.routes import subscription_routes


def create(dictionary):
    return handler_request.post(subscription_routes.get_base_url(), dictionary)


def find_all():
    return handler_request.get(subscription_routes.get_base_url())


def find_by_id(subscription_id):
    return handler_request.get(subscription_routes.get_specific_subscription_by_id_url(subscription_id))


def deactivation(subscription_id):
    return handler_request.post(subscription_routes.get_deactivation_subscription_url(subscription_id))


def activation(subscription_id):
    return handler_request.post(subscription_routes.get_activation_subscription_url(subscription_id))


def cancelation(subscription_id):
    return handler_request.post(subscription_routes.get_cancelation_subscription_url(subscription_id))


def completion(subscription_id):
    return handler_request.post(subscription_routes.get_completion_subscription_url(subscription_id))
