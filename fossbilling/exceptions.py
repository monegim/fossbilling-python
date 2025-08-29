"""
Exceptions for the FOSSBilling Python SDK.
"""

class FOSSBillingException(Exception):
    """Base exception for all FOSSBilling exceptions."""
    pass


class AuthenticationError(FOSSBillingException):
    """Raised when authentication fails."""
    pass


class APIError(FOSSBillingException):
    """Raised when the API returns an error."""
    def __init__(self, message, code=None, response=None):
        self.code = code
        self.response = response
        super().__init__(message)


class NotFoundError(FOSSBillingException):
    """Raised when a resource is not found."""
    pass


class ValidationError(FOSSBillingException):
    """Raised when input validation fails."""
    pass
