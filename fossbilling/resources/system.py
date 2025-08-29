"""
System resource for the FOSSBilling API.
"""
from typing import Any, Dict, List, Optional

from .base import BaseResource

class SystemResource(BaseResource):
    """Interact with system-related endpoints."""
    
    def __init__(self, client):
        super().__init__(client)
        self._endpoint = 'admin/system'
    
    def info(self) -> Dict[str, Any]:
        """
        Get system information.
        
        Returns:
            System information including version, PHP version, etc.
        """
        return self._get('info')
    
    def stats(self) -> Dict[str, Any]:
        """
        Get system statistics.
        
        Returns:
            System statistics (clients, orders, invoices, etc.)
        """
        return self._get('stats')
    
    def health_check(self) -> Dict[str, Any]:
        """
        Perform a health check.
        
        Returns:
            Health check results
        """
        return self._get('health')
    
    def get_config(self) -> Dict[str, Any]:
        """
        Get system configuration.
        
        Returns:
            System configuration
        """
        return self._get('config')
    
    def update_config(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update system configuration.
        
        Args:
            data: Configuration data to update
            
        Returns:
            Updated configuration
        """
        return self._post('config', data=data)
    
    def get_logs(self, **params) -> List[Dict[str, Any]]:
        """
        Get system logs.
        
        Args:
            **params: Query parameters (e.g., per_page, page, type, search)
            
        Returns:
            List of log entries
        """
        return self._get('logs', params=params).get('list', [])
    
    def clear_cache(self) -> bool:
        """
        Clear system cache.
        
        Returns:
            True if cache was cleared successfully
        """
        self._post('cache/clear')
        return True
