

class PayhereError(Exception):
    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None, headers=None, code=None):
        super(PayhereError, self).__init__(message)

        if http_body and hasattr(http_body, 'decode'):
            try:
                http_body = http_body.decode('utf-8')
            except BaseException:
                http_body = ('<Could not decode body as utf-8. ')

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}
        self.code = code
        self.request_id = self.headers.get('request-id', None)

    def __str__(self):
        msg = self._message or "<empty message>"
        if self.request_id is not None:
            return u"Request {0}: {1}".format(self.request_id, msg)
        else:
            return msg

    # Returns the underlying `Exception` (base class) message

    @property
    def user_message(self):
        return self._message

    def __repr__(self):
        return '{0}(message={1}, http_status={2}, request_id={3})'.format(
            self.__class__.__name__,
            self._message,
            self.http_status,
            self.request_id)


class APIError(PayhereError):
    pass


class APIConnectionError(PayhereError):
    pass


class AuthenticationError(PayhereError):
    pass


class PermissionError(PayhereError):
    pass


class PreapprovalError(PayhereError):
    pass


class RequestToPayError(PayhereError):
    pass


class TransferError(PayhereError):
    pass


class GeneralError(PayhereError):
    pass


class ValidationError(Exception):
    pass


class ConfigurationError(Exception):
    pass
