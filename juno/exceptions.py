class JunoException(Exception):
    def __init__(
        self,
        message,
        timestamp=None,
        error_code=None,
        status=None,
        error=None,
        path=None,
    ):
        self.timestamp = timestamp
        self.message = message
        self.error_code = error_code
        self.status = status
        self.error = error
        self.path = path

    def __str__(self):
        if not self.error_code:
            return self.message

        return f"{self.message} (timestamp={self.timestamp}, error_code={self.error_code}, status={self.status}, error={self.error}, path={self.path})"

    def __repr__(self):
        if not self.error_code:
            return self.message

        return f"('{self.timestamp}', '{self.message}', '{self.error_code}', {self.status}, '{self.error}', '{self.path}')"


class JunoInvalidCredentials(JunoException):
    pass
