## Juno Python Library
[![PyPI version](https://badge.fury.io/py/juno-python.svg)](https://badge.fury.io/py/juno-python)
<!-- [![Build status](https://travis-ci.org/mjr/juno-python.svg?branch=master)](https://secure.travis-ci.org/juno/juno-python) -->
<!-- [![Coverage](https://coveralls.io/repos/mjr/juno-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/mjr/juno-python) -->

The Juno Python library provides integration access to the Juno Gateway.

## Installing

This lib can be found on [pip](https://pypi.python.org/pypi/juno-python). To install it, use:

```
$ pip install juno-python
```

## Documentation

* [API Guide](https://dev.juno.com.br/api/)

## Quick Start Example

```python
import juno

juno.init(
    client_id="CLIENT_ID_JUNO",
    client_secret="CLIENT_SECRET_JUNO",
    resource_token="RESOURCE_TOKEN_JUNO",
    sandbox=False,
)

```python
result_charge = juno.charge.create(
    {
        "charge": {
            "description": "Description",
            "amount": "100.00",
            "references": [""],
            "payment_types": ["CREDIT_CARD"],
        },
        "billing": {
            "name": "Name Test",
            "document": "00000000000",  # Add a valid CPF
        },
    }
)

if result_charge.is_success:
    result_payment = juno.payment.create(
        {
            "charge_id": result_charge.charge.id,
            "billing": {
                "email": "name@test.com",  # Add a valid email
                "address": {  # Add a valid address
                    "street": "",
                    "number": "",
                    "complement": "",
                    "neighborhood": "",
                    "city": "",
                    "state": "",
                    "post_code": "",
                },
                "delayed": False,  # for capture delayed, use: "delayed": True
            },
            # if card is attached: "credit_card_details": {"credit_card_id": "id"}
            "credit_card_details": {"credit_card_hash": "hash"},
        }
    )

    if result_payment.is_success:
        print(f"Success payment: {result_payment.payment.id}")
    else:
        print(result_payment.errors)
else:
    print(result_charge.errors)
```

### Capture Delayed
```python
# ...
juno.payment.capture(result_payment.payment.id, {"charge_id": result_charge.charge.id, "amount": "100.00"})
```

## Support
If you have any problem or suggestion please open an issue [here](https://github.com/mjr/juno-python/issues).

## License

Check [here](LICENSE).
