# Dynamic data
INVENTORY = {
    "A4": 500,
    "A3": 200,
    "Letter": 1000,
    "Cardstock": 50
}

PRICE_PER_UNIT = {
    "A4": 2.0,
    "A3": 3.5,
    "Letter": 2.2,
    "Cardstock": 5.0
}

CUSTOMER_HISTORY = {
    "default": {"last_order": "200 A4", "total_spent": 800, "is_loyal": True},
    "new": {"last_order": "None", "total_spent": 0, "is_loyal": False}
}

CASH_BALANCE = 5000

def check_inventory(paper_type):
    stock = INVENTORY.get(paper_type, 0)
    if stock > 0:
        return f"{paper_type} in stock - {stock} units available"
    else:
        return f"{paper_type} out of stock"

def get_history(customer_type="default"):
    data = CUSTOMER_HISTORY.get(customer_type, CUSTOMER_HISTORY["default"])
    return data

def generate_quote(paper_type, quantity, customer_data):
    base_price = PRICE_PER_UNIT.get(paper_type, 2.0) * quantity
    
    # Dynamic discount calculation
    discount = 0
    if quantity >= 300:
        discount = 15  # bulk
    elif quantity >= 100:
        discount = 10
    if customer_data["is_loyal"]:
        discount += 5  # loyal extra

    final_price = base_price * (1 - discount/100)
    return {
        "base": base_price,
        "discount_percent": discount,
        "final": final_price,
        "text": f"Price ${base_price:.2f} - {discount}% discount = Final ${final_price:.2f}"
    }

def fulfill_order(paper_type, quantity):
    if INVENTORY.get(paper_type, 0) >= quantity:
        INVENTORY[paper_type] -= quantity
        return f"Order fulfilled - {quantity} {paper_type} deducted. Remaining: {INVENTORY[paper_type]}"
    return "Cannot fulfill - low stock"

def check_delivery_timeline(quantity):
    if quantity > 500:
        return "Delivery in 5-7 days (large order)"
    elif quantity > 100:
        return "Delivery in 3 days"
    else:
        return "Delivery in 1-2 days"

def check_cash_balance(final_price):
    global CASH_BALANCE
    if CASH_BALANCE >= final_price:
        return f"Cash OK - Balance ${CASH_BALANCE}"
    else:
        return "Low cash balance"
