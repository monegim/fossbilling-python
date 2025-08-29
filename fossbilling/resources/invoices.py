"""
Invoice resource for the FOSSBilling API.
"""
from typing import Any, Dict, List, Optional

from .base import BaseResource

class InvoiceResource(BaseResource):
    """Interact with invoice-related endpoints."""
    
    def __init__(self, client):
        super().__init__(client)
        self._endpoint = 'admin/invoice'
    
    def list(self, **params) -> List[Dict[str, Any]]:
        """
        List all invoices.
        
        Args:
            **params: Additional query parameters (e.g., per_page, page, client_id, status, etc.)
            
        Returns:
            List of invoice dictionaries
        """
        return self._get('', params=params).get('list', [])
    
    def get(self, invoice_id: int) -> Dict[str, Any]:
        """
        Get an invoice by ID.
        
        Args:
            invoice_id: The ID of the invoice to retrieve
            
        Returns:
            Invoice details as a dictionary
        """
        return self._get(str(invoice_id))
    
    def create(self, client_id: int, items: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """
        Create a new invoice.
        
        Args:
            client_id: The ID of the client
            items: List of invoice items, each with 'title', 'price', 'quantity', etc.
            **kwargs: Additional invoice data (due_date, tax, discount, etc.)
            
        Returns:
            The created invoice details
        """
        data = {
            'client_id': client_id,
            'items': items,
            **kwargs
        }
        return self._post('', data=data)
    
    def update(self, invoice_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an invoice.
        
        Args:
            invoice_id: The ID of the invoice to update
            data: Invoice data to update
            
        Returns:
            The updated invoice details
        """
        return self._put(str(invoice_id), data=data)
    
    def delete(self, invoice_id: int) -> bool:
        """
        Delete an invoice.
        
        Args:
            invoice_id: The ID of the invoice to delete
            
        Returns:
            True if deletion was successful
        """
        self._delete(str(invoice_id))
        return True
    
    def mark_as_paid(self, invoice_id: int, **kwargs) -> Dict[str, Any]:
        """
        Mark an invoice as paid.
        
        Args:
            invoice_id: The ID of the invoice
            **kwargs: Additional payment data (txn_id, amount, etc.)
            
        Returns:
            Updated invoice details
        """
        return self._post(f"{invoice_id}/mark_as_paid", data=kwargs)
    
    def generate_pdf(self, invoice_id: int) -> bytes:
        """
        Generate PDF for an invoice.
        
        Args:
            invoice_id: The ID of the invoice
            
        Returns:
            PDF content as bytes
        """
        response = self._client._request(
            'GET', 
            f"{self._endpoint}/{invoice_id}/pdf",
            headers={'Accept': 'application/pdf'}
        )
        return response.content
    
    def send_reminder(self, invoice_id: int) -> bool:
        """
        Send payment reminder for an invoice.
        
        Args:
            invoice_id: The ID of the invoice
            
        Returns:
            True if reminder was sent successfully
        """
        self._post(f"{invoice_id}/send_reminder")
        return True
