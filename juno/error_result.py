class ErrorResult(object):
    def __init__(self, attributes):
        self.timestamp = attributes["timestamp"]
        self.status = attributes["status"]
        self.message = attributes["error"]
        self.errors = attributes["details"]
        self.path = attributes["path"]

    def __repr__(self):
        return "<%s '%s' at %x>" % (self.__class__.__name__, self.message, id(self))

    @property
    def is_success(self):
        """ Returns whether the result from the gateway is a successful response. """

        return False
