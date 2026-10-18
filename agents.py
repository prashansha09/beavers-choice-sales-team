from tools import *

def orchestrator_agent(message):
    # Dynamic paper type retreiving
    message = message.upper()
    paper_type = "A4"  # default
    for pt in ["A4", "A3", "LETTER", "CARDSTOCK"]:
        if pt in message:
            paper_type = pt if pt != "LETTER" else "Letter"
            if paper_type == "A4": paper_type = "A4"
            if paper_type == "A3": paper_type = "A3"
            break
    
    # retreive quantity
    import re
    nums = re.findall(r'\d+', message)
    qty = int(nums[0]) if nums else 100
    
    print(f"[Orchestrator] Paper: {paper_type}, Qty: {qty}")
    return paper_type, qty

def inventory_agent(paper_type):
    result = check_inventory(paper_type)
    print(f"[Inventory] {result}")
    return result

def quote_agent(paper_type, qty):
    history = get_history()
    quote_data = generate_quote(paper_type, qty, history)
    print(f"[Quote] History: {history['last_order']}, {quote_data['text']}")
    return quote_data

def sales_agent(paper_type, qty, final_price):
    fulfill = fulfill_order(paper_type, qty)
    delivery = check_delivery_timeline(qty)
    cash = check_cash_balance(final_price)
    print(f"[Sales] {fulfill} | {delivery} | {cash}")
    return f"{fulfill} - {delivery}"