from juno.resources import handler_request
from juno.resources.routes import card_routes


def tokenization(dictionary):
    return handler_request.post(card_routes.get_tokenization_card_url(), dictionary)
