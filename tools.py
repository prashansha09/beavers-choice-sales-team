from langchain_core.tools import tool

@tool
def check_inventory(paper_type: str) -> str:
    """Check inventory for paper type. Input: paper_type like A4, A3, Letter, Cardstock"""
    inventory = {"A4": 500, "A3": 200, "Letter": 1000, "Cardstock": 50}
    stock = inventory.get(paper_type, 0)
    return f"{paper_type} inventory: {stock} units available - {'In Stock' if stock>0 else 'Out of Stock'}"

@tool
def get_quote_history(customer_name: str) -> str:
    """Get customer past order history. Input: customer name"""
    return f"Customer {customer_name} history: Last order 200 A4, total spent $800, loyal customer"

@tool
def calculate_bulk_discount(quantity: int) -> str:
    """Calculate bulk discount based on quantity. Input: quantity as int"""
    if quantity >= 300:
        return "15% bulk discount eligible"
    elif quantity >= 100:
        return "10% bulk discount eligible"
    else:
        return "5% loyalty discount only"

@tool
def generate_quote(paper_type: str, quantity: int, discount_info: str) -> str:
    """Generate final price quote. Inputs: paper_type, quantity, discount_info"""
    prices = {"A4": 2.0, "A3": 3.5, "Letter": 2.2, "Cardstock": 5.0}
    base = prices.get(paper_type, 2.0) * quantity
    discount_pct = 15 if "15%" in discount_info else 10 if "10%" in discount_info else 5
    final = base * (1 - discount_pct/100)
    return f"Quote for {quantity} {paper_type}: Base ${base:.2f}, Discount {discount_pct}%, Final ${final:.2f}"

@tool
def check_delivery_timeline(quantity: int) -> str:
    """Check delivery timeline based on quantity. Input: quantity"""
    if quantity > 500:
        return "Delivery in 5-7 days"
    elif quantity > 100:
        return "Delivery in 3 days"
    else:
        return "Delivery in 1-2 days"

@tool
def check_cash_balance(amount: float) -> str:
    """Check if company has cash to fulfill order. Input: final amount"""
    balance = 5000
    return f"Cash balance ${balance}, order amount ${amount} - {'Approved' if balance>=amount else 'Need approval'}"