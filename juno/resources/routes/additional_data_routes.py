from ..handler_request import get_resource_url


def get_base_url():
    return f"{get_resource_url()}/data"

def get_banks_url():
    return f"{get_base_url()}/banks"

def get_company_types_url():
    return f"{get_base_url()}/company-types"

def get_business_areas_url():
    return f"{get_base_url()}/business-areas"