from ..handler_request import get_resource_url


def get_base_url():
    return f"{get_resource_url()}/credit-cards"


def get_tokenization_card_url():
    return f"{get_base_url()}/tokenization"
