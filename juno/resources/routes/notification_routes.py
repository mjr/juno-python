from ..handler_request import get_resource_url


def get_base_url():
    return f"{get_resource_url()}/notifications"


def get_base_url_event_types():
    return f"{get_base_url()}/event-types"


def get_base_url_webhooks():
    return f"{get_base_url()}/webhooks"


def get_specific_webhook_by_id_url(webhook_id):
    return f"{get_base_url_webhooks()}/{webhook_id}"


def get_update_webhook_url(webhook_id):
    return f"{get_base_url_webhooks()}/{webhook_id}"


def get_delete_webhook_url(webhook_id):
    return f"{get_base_url_webhooks()}/{webhook_id}"
