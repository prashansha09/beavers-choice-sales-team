from tools import *

# 4 Agents simple function ke form me

def orchestrator_agent(message):
    print(f"[Orchestrator] Customer bola: {message}")
    return "A4"  # paper type nikal liya

def inventory_agent(paper_type):
    result = check_inventory(paper_type)
    print(f"[Inventory] {result}")
    return result

def quote_agent(paper_type, qty):
    history = get_history("customer")
    quote = generate_quote(paper_type, qty)
    print(f"[Quote] History: {history}, Quote: {quote}")
    return quote

def sales_agent():
    fulfill = fulfill_order()
    delivery = check_delivery_timeline()
    cash = check_cash_balance()
    print(f"[Sales] {fulfill}, {delivery}, {cash}")
    return f"{fulfill} - {delivery}"