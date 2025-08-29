"""
Service resource for the FOSSBilling API.
"""
from typing import Any, Dict, List, Optional

from .base import BaseResource

class ServiceResource(BaseResource):
    """Interact with service-related endpoints."""
    
    def __init__(self, client):
        super().__init__(client)
        self._endpoint = 'admin/service'
    
    def list(self, **params) -> List[Dict[str, Any]]:
        """
        List all services.
        
        Args:
            **params: Additional query parameters (e.g., per_page, page, client_id, etc.)
            
        Returns:
            List of service dictionaries
        """
        return self._get('', params=params).get('list', [])
    
    def get(self, service_id: int) -> Dict[str, Any]:
        """
        Get a service by ID.
        
        Args:
            service_id: The ID of the service to retrieve
            
        Returns:
            Service details as a dictionary
        """
        return self._get(str(service_id))
    
    def update(self, service_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a service.
        
        Args:
            service_id: The ID of the service to update
            data: Service data to update
            
        Returns:
            The updated service details
        """
        return self._put(str(service_id), data=data)
    
    def delete(self, service_id: int) -> bool:
        """
        Delete a service.
        
        Args:
            service_id: The ID of the service to delete
            
        Returns:
            True if deletion was successful
        """
        self._delete(str(service_id))
        return True
    
    def renew(self, service_id: int, **kwargs) -> Dict[str, Any]:
        """
        Renew a service.
        
        Args:
            service_id: The ID of the service to renew
            **kwargs: Additional renewal options (e.g., period)
            
        Returns:
            Updated service details
        """
        return self._post(f"{service_id}/renew", data=kwargs)
    
    def suspend(self, service_id: int, reason: str = '') -> Dict[str, Any]:
        """
        Suspend a service.
        
        Args:
            service_id: The ID of the service to suspend
            reason: Reason for suspension
            
        Returns:
            Updated service details
        """
        return self._post(f"{service_id}/suspend", data={'reason': reason})
    
    def unsuspend(self, service_id: int) -> Dict[str, Any]:
        """
        Unsuspend a suspended service.
        
        Args:
            service_id: The ID of the service to unsuspend
            
        Returns:
            Updated service details
        """
        return self._post(f"{service_id}/unsuspend")
    
    def cancel(self, service_id: int, reason: str = '') -> Dict[str, Any]:
        """
        Cancel a service.
        
        Args:
            service_id: The ID of the service to cancel
            reason: Reason for cancellation
            
        Returns:
            Updated service details
        """
        return self._post(f"{service_id}/cancel", data={'reason': reason})
