from django.shortcuts import render
from .models import Product
from hoxobil.utils.printify_utils import create_printify_product, get_printify_products
from django.http import JsonResponse

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def fetch_printify_products(request):
    """Fetch products from Printify"""
    shop_id = 'YOUR_SHOP_ID'  # Replace with actual ID
    products = get_printify_products(shop_id)
    return JsonResponse(products)

def create_printify_product_view(request):
    """Create a new product on Printify"""
    shop_id = 'YOUR_SHOP_ID'  # Replace with actual ID
    product_data = {
        "title": "HOXOBIL T-shirt",
        "variants": [
            {
                "size": "M",
                "price": "20.00",
                "sku": "H-Tshirt-M",
                "color": "Black"
            }
        ],
        "print_provider_id": 1,  # Example provider ID
    }

    response = create_printify_product(shop_id, product_data)
    return JsonResponse(response)
