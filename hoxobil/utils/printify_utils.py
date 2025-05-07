import requests
from django.conf import settings

# Define the base URL for the Printify API
PRINTIFY_API_URL = "https://api.printify.com/v1"

def get_printify_products(shop_id):
    """Fetch products from a specific Printify shop"""
    headers = {
        'Authorization': f'Bearer {settings.PRINTIFY_API_TOKEN}',
    }
    response = requests.get(f"{PRINTIFY_API_URL}/shops/{shop_id}/products.json", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": "Failed to fetch products from Printify",
            "status_code": response.status_code,
            "message": response.text
        }

def create_printify_product(shop_id, data):
    """Create a new product on a specific Printify shop"""
    headers = {
        'Authorization': f'Bearer {settings.PRINTIFY_API_TOKEN}',
        'Content-Type': 'application/json',
    }
    response = requests.post(f"{PRINTIFY_API_URL}/shops/{shop_id}/products.json", json=data, headers=headers)

    if response.status_code == 201:
        return response.json()
    else:
        return {
            "error": "Failed to create product on Printify",
            "status_code": response.status_code,
            "message": response.text
        }
