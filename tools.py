# tools.py

def search_products(query, color, price_range, size):
    return [
        {"name": "Floral Skirt", "price": 35, "size": "S", "in_stock": True},
        {"name": "Casual Jeans", "price": 50, "size": "M", "in_stock": True}
    ]

def estimate_shipping(user_location, delivery_date):
    return {"cost": 5.99, "arrival": "2025-02-10", "feasible": True}

def check_discount(price, promo_code):
    if promo_code == "SAVE10":
        return {"final_price": price * 0.9}
    return {"final_price": price}

def compare_prices(product_name):
    return {"SiteA": 80, "SiteB": 75, "SiteC": 78}

def check_return_policy(site_name):
    return {"policy": "30-day return with free shipping."}
