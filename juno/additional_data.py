from juno.resources import handler_request
from juno.resources.routes import additional_data_routes


def list_banks():
    return handler_request.get(additional_data_routes.get_banks_url())

def list_company_types():
    return handler_request.get(additional_data_routes.get_company_types_url())

def list_business_areas():
    return handler_request.get(additional_data_routes.get_business_areas_url())