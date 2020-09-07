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

CREDIT_CARD_CHARGE = {
    "charge": {
        "description": "Description",
        "amount": "100.00",
        "installments": 1,
        "payment_types": ["CREDIT_CARD"],
    },
    "billing": {
        "name": "Name Test",
        "document": "00000000000", # Add a valid CPF
        "notify": False,
    },
}

result = juno.charge.create(CREDIT_CARD_CHARGE)

print("result: " + result)
```

## Support
If you have any problem or suggestion please open an issue [here](https://github.com/mjr/juno-python/issues).

## License

Check [here](LICENSE).
