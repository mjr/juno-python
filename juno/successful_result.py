from juno.attribute_getter import AttributeGetter


class SuccessfulResult(AttributeGetter):
    @property
    def is_success(self):
        """ Returns whether the result from the gateway is a successful response. """
        return True
