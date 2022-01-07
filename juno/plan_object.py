from juno.attribute_getter import AttributeGetter


class Plan(AttributeGetter):
    def __init__(self, attributes=None):
        if attributes is None:
            attributes = {}
        self._setattrs = []
        for key, val in attributes.items():
            setattr(self, key, val)
            self._setattrs.append(key)
