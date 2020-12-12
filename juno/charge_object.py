from juno.attribute_getter import AttributeGetter
from juno.payment_object import Payment


class Charge(AttributeGetter):
    def __init__(self, attributes=None):
        if attributes is None:
            attributes = {}
        self._setattrs = []
        for key, val in attributes.items():
            if key == "payments":
                setattr(self, key, [Payment(payment_dict) for payment_dict in val])
            else:
                setattr(self, key, val)

            self._setattrs.append(key)
