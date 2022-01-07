from ..handler_request import get_resource_url


def get_base_url():
    return f"{get_resource_url()}/plans"


def get_specific_plan_by_id_url(plan_id):
    return f"{get_base_url()}/{plan_id}"


def get_deactivation_plan_url(plan_id):
    return f"{get_base_url()}/{plan_id}/deactivation"


def get_activation_plan_url(plan_id):
    return f"{get_base_url()}/{plan_id}/activation"
