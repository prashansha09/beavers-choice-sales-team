from agents import *
import re

# Customer -> Orchestrator -> Inventory -> Quote -> Sales -> Final Answer

customer_message = "I want 300 A4 paper sheets"

print("--- Beaver's Choice Sales Team Start ---")

paper_type, qty = orchestrator_agent(customer_message)
inventory = inventory_agent(paper_type)
quote_data = quote_agent(paper_type, qty)
final = sales_agent(paper_type, qty, quote_data["final"])

print("\n--- Final Response to Customer ---")
print(f"Hello! {inventory}. {quote_data['text']}. {final}. Thank you!")
