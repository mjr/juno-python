from juno.resources import handler_request
from juno.resources.routes import payment_routes


def create(dictionary):
    return handler_request.post(payment_routes.get_base_url(), dictionary)


def refund(payment_id, dictionary):
    return handler_request.post(
        payment_routes.get_refund_payment_url(payment_id), dictionary
    )


def capture(payment_id, dictionary):
    return handler_request.post(
        payment_routes.get_capture_payment_url(payment_id), dictionary
    )

