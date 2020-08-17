from ..handler_request import get_resource_url


def get_base_url():
    return f"{get_resource_url()}/charges"


def get_specific_charge_by_id_url(charge_id):
    return f"{get_base_url()}/{charge_id}"


def get_cancelation_charge_url(charge_id):
    return f"{get_base_url()}/{charge_id}/cancelation"


def get_update_split_charge_url(charge_id):
    return f"{get_base_url()}/{charge_id}/split"
