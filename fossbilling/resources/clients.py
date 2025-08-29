"""
Client resource for the FOSSBilling API.
"""
from typing import Any, Dict, List, Optional

from .base import BaseResource

class ClientResource(BaseResource):
    """Interact with client-related endpoints."""
    
    def __init__(self, client):
        super().__init__(client)
        self._endpoint = 'admin/client'
    
    def list(self, **params) -> List[Dict[str, Any]]:
        """
        List all clients.
        
        Args:
            **params: Additional query parameters (e.g., per_page, page, search, etc.)
            
        Returns:
            List of client dictionaries
        """
        return self._get('', params=params).get('list', [])
    
    def get(self, client_id: int) -> Dict[str, Any]:
        """
        Get a client by ID.
        
        Args:
            client_id: The ID of the client to retrieve
            
        Returns:
            Client details as a dictionary
        """
        return self._get(str(client_id))
    
    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new client.
        
        Args:
            data: Client data (email, first_name, last_name, etc.)
            
        Returns:
            The created client details
        """
        required = ['email', 'first_name', 'last_name', 'password']
        if not all(field in data for field in required):
            raise ValueError(f"Missing required fields: {required}")
            
        return self._post('', data=data)
    
    def update(self, client_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a client.
        
        Args:
            client_id: The ID of the client to update
            data: Client data to update
            
        Returns:
            The updated client details
        """
        return self._put(str(client_id), data=data)
    
    def delete(self, client_id: int, delete_orders: bool = False) -> bool:
        """
        Delete a client.
        
        Args:
            client_id: The ID of the client to delete
            delete_orders: Whether to delete associated orders
            
        Returns:
            True if deletion was successful
        """
        params = {'delete_orders': int(delete_orders)}
        self._delete(f"{client_id}", params=params)
        return True
    
    def get_balance(self, client_id: int) -> Dict[str, Any]:
        """
        Get client's balance.
        
        Args:
            client_id: The ID of the client
            
        Returns:
            Balance information
        """
        return self._get(f"{client_id}/balance")
    
    def update_balance(self, client_id: int, amount: float, 
                      description: str = '') -> Dict[str, Any]:
        """
        Update client's balance.
        
        Args:
            client_id: The ID of the client
            amount: Amount to add (positive) or subtract (negative)
            description: Description for the transaction
            
        Returns:
            Updated balance information
        """
        data = {
            'amount': amount,
            'description': description or 'Balance update'
        }
        return self._post(f"{client_id}/balance", data=data)
