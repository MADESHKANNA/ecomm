from django.shortcuts import render,redirect

# Hardcoded products
products = [
    {
        "id": 1,
        "name": "Lenovo IdeaPad Gaming 3 Intel Core i5 10th Gen 10300H",
        "price": 60000,
        "description": "A high-performance laptop for work and gaming.",
        'image': '/static/images/1.jpg'
    },
    {
        "id": 2,
        "name": "MOTOROLA Edge 60 5G",
        "price": 25000,
        "description": "A sleek smartphone with a powerful camera.",
        'image': '/static/images/2.jpg'
    },
    {
        "id": 3,
        "name": "boAt Airdopes",
        "price": 1499,
        "description": "Noise-cancelling headphones with deep bass.",
        'image': '/static/images/3.jpg'
    }
]
cart = []

def home(request):
    return render(request, 'recipe/home.html', {'products': products})

def product_detail(request, product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return render(request, 'recipe/404.html')
    return render(request, 'recipe/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product and product not in cart:
        cart.append(product)
    return redirect('cart')

def buy_now(request, product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        # For simplicity, redirect to a success page
        return render(request, 'recipe/success.html', {'product': product})
    return redirect('home')

def view_cart(request):
    return render(request, 'recipe/cart.html', {'cart': cart})
