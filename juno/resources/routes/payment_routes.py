from ..handler_request import get_resource_url


def get_base_url():
    return f"{get_resource_url()}/payments"


def get_refund_payment_url(payment_id):
    return f"{get_base_url()}/{payment_id}/refunds"


def get_capture_payment_url(payment_id):
    return f"{get_base_url()}/{payment_id}/capture"
