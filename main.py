from agents import *

# Customer -> Orchestrator -> Inventory -> Quote -> Sales -> Final Answer

customer_message = "I want 300 A4 paper sheets"

print("--- Beaver's Choice Sales Team Start ---")

paper_type = orchestrator_agent(customer_message)
inventory = inventory_agent(paper_type)
quote = quote_agent(paper_type, 300)
final = sales_agent()

print("\n--- Final Response to Customer ---")
print(f"Hello! {inventory}. {quote}. {final}. Thank you!")
