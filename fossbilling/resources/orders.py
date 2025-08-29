"""
Order resource for the FOSSBilling API.
"""
from typing import Any, Dict, List, Optional

from .base import BaseResource

class OrderResource(BaseResource):
    """Interact with order-related endpoints."""
    
    def __init__(self, client):
        super().__init__(client)
        self._endpoint = 'admin/order'
    
    def list(self, **params) -> List[Dict[str, Any]]:
        """
        List all orders.
        
        Args:
            **params: Additional query parameters (e.g., per_page, page, client_id, status, etc.)
            
        Returns:
            List of order dictionaries
        """
        return self._get('', params=params).get('list', [])
    
    def get(self, order_id: int) -> Dict[str, Any]:
        """
        Get an order by ID.
        
        Args:
            order_id: The ID of the order to retrieve
            
        Returns:
            Order details as a dictionary
        """
        return self._get(str(order_id))
    
    def create(self, client_id: int, product_id: int, **kwargs) -> Dict[str, Any]:
        """
        Create a new order.
        
        Args:
            client_id: The ID of the client
            product_id: The ID of the product to order
            **kwargs: Additional order data (period, quantity, config options, etc.)
            
        Returns:
            The created order details
        """
        data = {
            'client_id': client_id,
            'product_id': product_id,
            **kwargs
        }
        return self._post('', data=data)
    
    def update(self, order_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an order.
        
        Args:
            order_id: The ID of the order to update
            data: Order data to update
            
        Returns:
            The updated order details
        """
        return self._put(str(order_id), data=data)
    
    def delete(self, order_id: int, delete_addons: bool = False) -> bool:
        """
        Delete an order.
        
        Args:
            order_id: The ID of the order to delete
            delete_addons: Whether to delete associated addons
            
        Returns:
            True if deletion was successful
        """
        params = {'delete_addons': int(delete_addons)}
        self._delete(f"{order_id}", params=params)
        return True
    
    def activate(self, order_id: int) -> Dict[str, Any]:
        """
        Activate a pending order.
        
        Args:
            order_id: The ID of the order to activate
            
        Returns:
            Updated order details
        """
        return self._post(f"{order_id}/activate")
    
    def renew(self, order_id: int) -> Dict[str, Any]:
        """
        Renew an active order.
        
        Args:
            order_id: The ID of the order to renew
            
        Returns:
            Updated order details
        """
        return self._post(f"{order_id}/renew")
    
    def suspend(self, order_id: int, reason: str = '') -> Dict[str, Any]:
        """
        Suspend an active order.
        
        Args:
            order_id: The ID of the order to suspend
            reason: Reason for suspension
            
        Returns:
            Updated order details
        """
        return self._post(f"{order_id}/suspend", data={'reason': reason})
    
    def unsuspend(self, order_id: int) -> Dict[str, Any]:
        """
        Unsuspend a suspended order.
        
        Args:
            order_id: The ID of the order to unsuspend
            
        Returns:
            Updated order details
        """
        return self._post(f"{order_id}/unsuspend")
    
    def cancel(self, order_id: int, reason: str = '') -> Dict[str, Any]:
        """
        Cancel an order.
        
        Args:
            order_id: The ID of the order to cancel
            reason: Reason for cancellation
            
        Returns:
            Updated order details
        """
        return self._post(f"{order_id}/cancel", data={'reason': reason})
