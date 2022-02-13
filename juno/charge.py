from juno.resources import handler_request
from juno.resources.routes import charge_routes


def create(dictionary):
    return handler_request.post(charge_routes.get_base_url(), dictionary)


def find_all(query_params={}):
    return handler_request.get(charge_routes.get_base_url(), query_params)


def find_by_id(charge_id):
    return handler_request.get(charge_routes.get_specific_charge_by_id_url(charge_id))


def cancelation(charge_id):
    return handler_request.put(charge_routes.get_cancelation_charge_url(charge_id))


def update_split(charge_id, dictionary):
    return handler_request.put(
        charge_routes.get_update_split_charge_url(charge_id), dictionary
    )
