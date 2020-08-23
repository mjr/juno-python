VALID_CREDIT_CARD_PAYMENT_CAPTURE_FALSE = {
    "charge_id": "",
    "billing": {
        "email": "",
        "address": {
            "street": "",
            "number": "",
            "complement": "",
            "neighborhood": "",
            "city": "",
            "state": "",
            "postCode": "",
        },
        "delayed": True,
    },
    "credit_card_details": {"credit_card_hash": ""},
}

REFUNDED_OR_CAPTURE_PAYMENT = {
    "charge_id": "",
    "amount": "100",
}

VALID_CREDIT_CARD_PAYMENT = {
    "charge_id": "",
    "billing": {
        "email": "",
        "address": {
            "street": "",
            "number": "",
            "complement": "",
            "neighborhood": "",
            "city": "",
            "state": "",
            "postCode": "",
        },
        "delayed": False,
    },
    "credit_card_details": {"credit_card_id": ""},
}
