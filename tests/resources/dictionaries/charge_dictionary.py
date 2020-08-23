SLIP_PAYMENT = {
    "charge": {
        "description": "Test",
        "amount": "100",
        "due_date": "2020-09-20",
        "installments": 1,
        "max_overdue_days": 0,
        "fine": 0,
        "interest": 0,
        "discount_amount": 0,
        "discount_days": -1,
        "payment_types": ["BOLETO"],
        "payment_advance": True,
        "split": [],
    },
    "billing": {"name": "Name Test", "document": "000000000000", "notify": False},
}

CREDIT_CARD_PAYMENT = {
    "charge": {
        "description": "Test",
        "amount": "100",
        "due_date": "2020-09-17",
        "installments": 1,
        "max_overdue_days": 0,
        "fine": 0,
        "interest": 0,
        "discount_amount": 0,
        "discount_days": -1,
        "payment_types": ["CREDIT_CARD"],
        "payment_advance": True,
        "split": [],
    },
    "billing": {"name": "Name Test", "document": "000000000000", "notify": False},
}

VALID_CREDIT_CARD_CHARGE_WITH_SPLIT_RULE_AMOUNT = {}

VALID_CREDIT_CARD_PAYMENT_WITH_SPLIT_RULE_PERCENTAGE = {}

INVALID_REQUEST = {}

INVALID_REQUEST = {
    "amount": "1",
    "payment_method": "",
    "customer": "",
}
