"""
FOSSBilling API client implementation.
"""
import json
import requests
from typing import Dict, Any, Optional, Union
from urllib.parse import urljoin

from .exceptions import (
    AuthenticationError,
    APIError,
    NotFoundError,
    ValidationError
)

class Client:
    """
    A client for the FOSSBilling API.
    
    Args:
        base_url: The base URL of your FOSSBilling installation (e.g., 'https://billing.example.com/')
        api_key: Your FOSSBilling API key
        timeout: Request timeout in seconds (default: 30)
    """
    
    def __init__(self, base_url: str, api_key: str, timeout: int = 30):
        if not base_url.endswith('/'):
            base_url += '/'
            
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-API-Key': self.api_key
        })
        
        # Initialize resources
        self.clients = ClientResource(self)
        self.invoices = InvoiceResource(self)
        self.orders = OrderResource(self)
        self.services = ServiceResource(self)
        self.system = SystemResource(self)
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        Make a request to the FOSSBilling API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (e.g., 'admin/client')
            **kwargs: Additional arguments to pass to requests.request()
            
        Returns:
            dict: The parsed JSON response
            
        Raises:
            AuthenticationError: If authentication fails
            APIError: If the API returns an error
            requests.RequestException: For network-related errors
        """
        url = urljoin(self.base_url, f'api/{endpoint.lstrip("/")}')
        
        # Add timeout if not specified
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout
            
        try:
            response = self.session.request(method, url, **kwargs)
            
            # Handle non-OK responses
            if not response.ok:
                self._handle_error_response(response)
                
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")
    
    def _handle_error_response(self, response: requests.Response) -> None:
        """Handle error responses from the API."""
        status_code = response.status_code
        
        try:
            error_data = response.json()
            error_msg = error_data.get('error', {}).get('message', response.text)
        except ValueError:
            error_msg = response.text or f"HTTP {status_code}"
        
        if status_code == 401:
            raise AuthenticationError("Invalid API key or insufficient permissions")
        elif status_code == 404:
            raise NotFoundError(error_msg)
        elif status_code == 422:
            raise ValidationError(error_msg)
        else:
            raise APIError(
                f"API request failed with status {status_code}: {error_msg}",
                code=status_code,
                response=response
            )
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request to the API."""
        return self._request('GET', endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a POST request to the API."""
        return self._request('POST', endpoint, json=data)
    
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a PUT request to the API."""
        return self._request('PUT', endpoint, json=data)
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request to the API."""
        return self._request('DELETE', endpoint)
