"""
Base resource class for FOSSBilling API resources.
"""
from typing import Any, Dict, Optional, Union

class BaseResource:
    """Base class for all FOSSBilling API resources."""
    
    def __init__(self, client):
        """Initialize with a client instance."""
        self._client = client
        self._endpoint = ''
    
    def _get(self, path: str = '', params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request to the resource endpoint."""
        return self._client.get(f"{self._endpoint}/{path}".strip('/'), params=params)
    
    def _post(self, path: str = '', data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a POST request to the resource endpoint."""
        return self._client.post(f"{self._endpoint}/{path}".strip('/'), data=data)
    
    def _put(self, path: str = '', data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a PUT request to the resource endpoint."""
        return self._client.put(f"{self._endpoint}/{path}".strip('/'), data=data)
    
    def _delete(self, path: str = '') -> Dict[str, Any]:
        """Make a DELETE request to the resource endpoint."""
        return self._client.delete(f"{self._endpoint}/{path}".strip('/'))
