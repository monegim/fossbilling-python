"""
FOSSBilling API resources.
"""

from .base import BaseResource
from .clients import ClientResource
from .invoices import InvoiceResource
from .orders import OrderResource
from .services import ServiceResource
from .system import SystemResource

__all__ = [
    'BaseResource',
    'ClientResource',
    'InvoiceResource',
    'OrderResource',
    'ServiceResource',
    'SystemResource',
]
