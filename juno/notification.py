from juno.resources import handler_request
from juno.resources.routes import notification_routes


def find_all_event_types():
    return handler_request.get(notification_routes.get_base_url_event_types())


def create_webhook(dictionary):
    return handler_request.post(notification_routes.get_base_url_webhooks(), dictionary)


def find_all_webhooks():
    return handler_request.get(notification_routes.get_base_url_webhooks())


def find_webhook_by_id(webhook_id):
    return handler_request.get(
        notification_routes.get_specific_webhook_by_id_url(webhook_id)
    )


def update_webhook(webhook_id, dictionary):
    return handler_request.patch(
        charge_routes.get_update_webhook_url(webhook_id), dictionary
    )


def delete_webhook(webhook_id):
    return handler_request.delete(
        notification_routes.get_delete_webhook_url(webhook_id)
    )
