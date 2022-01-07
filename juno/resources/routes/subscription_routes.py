from ..handler_request import get_resource_url


def get_base_url():
    return f"{get_resource_url()}/subscriptions"


def get_specific_subscription_by_id_url(subscription_id):
    return f"{get_base_url()}/{subscription_id}"


def get_deactivation_subscription_url(subscription_id):
    return f"{get_base_url()}/{subscription_id}/deactivation"


def get_activation_subscription_url(subscription_id):
    return f"{get_base_url()}/{subscription_id}/activation"


def get_cancelation_subscription_url(subscription_id):
    return f"{get_base_url()}/{subscription_id}/cancelation"


def get_completion_subscription_url(subscription_id):
    return f"{get_base_url()}/{subscription_id}/completion"
