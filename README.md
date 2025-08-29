# FOSSBilling Python SDK

A Python client library for interacting with the FOSSBilling API.

## Installation

```bash
pip install fossbilling
```

## Quick Start

```python
from fossbilling import Client

# Initialize the client
client = Client(
    base_url="https://your-fossbilling-installation.com/",
    api_key="your_api_key_here"
)

# List clients
clients = client.clients.list()
print(f"Found {len(clients)} clients")

# Get a specific client
client_details = client.clients.get(client_id=1)
print(f"Client email: {client_details['email']}")

# Create a new client
new_client = client.clients.create({
    'email': 'new@example.com',
    'first_name': 'John',
    'last_name': 'Doe',
    'password': 'secure_password'
})
print(f"Created new client with ID: {new_client['id']}")
```

## Features

- Full support for FOSSBilling's API endpoints
- Type hints for better IDE support
- Comprehensive error handling
- Asynchronous support (coming soon)

## Available Resources

- **Clients**: Manage client accounts
- **Invoices**: Create and manage invoices
- **Orders**: Handle product orders
- **Services**: Manage client services
- **System**: System information and utilities

## Documentation

Full documentation is available at [FOSSBilling Documentation](https://fossbilling.org/docs).

## Examples

### Creating an Invoice

```python
invoice = client.invoices.create(
    client_id=1,
    items=[
        {
            'title': 'Web Hosting - Basic Plan',
            'price': 9.99,
            'quantity': 1,
            'taxed': True
        }
    ],
    due_date='2023-12-31'
)
print(f"Created invoice #{invoice['id']}")
```

### Managing Orders

```python
# Create an order
order = client.orders.create(
    client_id=1,
    product_id=1,
    period='1M'  # 1 month
)

# Activate the order
client.orders.activate(order['id'])

# Suspend the order
client.orders.suspend(order['id'], reason="Payment overdue")
```

## Error Handling

The SDK raises specific exceptions for different types of errors:

```python
try:
    client.clients.get(999)  # Non-existent client
except fossbilling.NotFoundError as e:
    print("Client not found!")
except fossbilling.AuthenticationError as e:
    print("Authentication failed!")
except fossbilling.APIError as e:
    print(f"API Error: {e}")
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

MIT

## Support

For support, please open an issue in the [GitHub repository](https://github.com/yourusername/fossbilling-python/issues).
