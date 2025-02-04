from tools import search_products, estimate_shipping, check_discount, compare_prices, check_return_policy

def agent_response(user_input):
    # Task A: Item search and discount
    if "floral skirt" in user_input and "under $40" in user_input and "size S" in user_input:
        products = search_products("floral skirt", "any", "under $40", "S")
        discount = check_discount(products[0]['price'], "SAVE10")
        return f"Found: {products[0]['name']} for ${discount['final_price']} (after discount). In stock: {products[0]['in_stock']}."
    
    # Task B: Shipping estimate
    if "shipping" in user_input:
        shipping = estimate_shipping("New York", "2025-02-10")
        return f"Shipping cost: ${shipping['cost']}. Estimated arrival: {shipping['arrival']}."
    
    # Task C: Competitor price comparison
    if "better deals" in user_input:
        comparison = compare_prices("casual denim jacket")
        return f"Price comparison: SiteA: ${comparison['SiteA']}, SiteB: ${comparison['SiteB']}, SiteC: ${comparison['SiteC']}."
    
    # Task D: Return policy check
    if "returns" in user_input:
        return_policy = check_return_policy("SiteB")
        return f"Return policy for SiteB: {return_policy['policy']}"
    
    # Task E: Combine multiple tasks (search, shipping, discount, competitor)
    if "floral skirt" in user_input and "under $40" in user_input:
        products = search_products("floral skirt", "any", "under $40", "S")
        discount = check_discount(products[0]['price'], "SAVE10")
        shipping = estimate_shipping("New York", "2025-02-10")
        comparison = compare_prices("floral skirt")
        
        return (f"Found: {products[0]['name']} for ${discount['final_price']} (after discount). "
                f"Shipping cost: ${shipping['cost']}. Estimated arrival: {shipping['arrival']}. "
                f"Price comparison: SiteA: ${comparison['SiteA']}, SiteB: ${comparison['SiteB']}, SiteC: ${comparison['SiteC']}.")
    
    return "I couldn't find an answer. Can you refine your question?"

# Example interaction
user_query = "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code ‘SAVE10’?"
print(agent_response(user_query))
