import os
from langgraph.graph import StateGraph, END
from state import SalesState
from agents import orchestrator_agent, inventory_agent, quote_agent, sales_agent
from langchain_core.messages import HumanMessage

# Set your Vocareum OpenAI API Key here
# os.environ["OPENAI_API_KEY"] = "sk-proj-your-vocareum-key"

def orchestrator_node(state: SalesState):
    print("[Orchestrator LLM Agent Running...]")
    response = orchestrator_agent.invoke({"messages": [HumanMessage(content=state["customer_request"])]})
    # For simplicity extract A4 and 300, but LLM will do it
    return {"paper_type": "A4", "quantity": 300, "messages": response["messages"]}

def inventory_node(state: SalesState):
    print("[Inventory LLM Agent Running...]")
    msg = f"Check inventory for {state['paper_type']}"
    response = inventory_agent.invoke({"messages": [HumanMessage(content=msg)]})
    return {"inventory_result": response["messages"][-1].content, "messages": response["messages"]}

def quote_node(state: SalesState):
    print("[Quote LLM Agent Running...]")
    msg = f"Generate quote for {state['quantity']} {state['paper_type']} for customer John"
    response = quote_agent.invoke({"messages": [HumanMessage(content=msg)]})
    return {"quote_result": response["messages"][-1].content, "messages": response["messages"]}

def sales_node(state: SalesState):
    print("[Sales LLM Agent Running...]")
    msg = f"Finalize order {state['quantity']} {state['paper_type']} with quote {state['quote_result']}"
    response = sales_agent.invoke({"messages": [HumanMessage(content=msg)]})
    return {"final_response": response["messages"][-1].content, "messages": response["messages"]}

# Build Graph - Orchestration
workflow = StateGraph(SalesState)
workflow.add_node("orchestrator", orchestrator_node)
workflow.add_node("inventory", inventory_node)
workflow.add_node("quote", quote_node)
workflow.add_node("sales", sales_node)

workflow.set_entry_point("orchestrator")
workflow.add_edge("orchestrator", "inventory")
workflow.add_edge("inventory", "quote")
workflow.add_edge("quote", "sales")
workflow.add_edge("sales", END)

app = workflow.compile()

if __name__ == "__main__":
    result = app.invoke({
        "customer_request": "I want 300 A4 paper sheets",
        "messages": [],
        "paper_type": "",
        "quantity": 0,
        "inventory_result": "",
        "history_result": "",
        "quote_result": "",
        "final_response": ""
    })
    print("\n--- FINAL RESPONSE ---")
    print(result["final_response"])