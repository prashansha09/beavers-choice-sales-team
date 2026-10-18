from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools import check_inventory, get_quote_history, calculate_bulk_discount, generate_quote, check_delivery_timeline, check_cash_balance

# LLM for Vocareum
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 4 LLM Agents

orchestrator_agent = create_react_agent(
    llm, 
    tools=[], 
    prompt="You are Orchestrator Agent. You receive customer request, extract paper_type (A4, A3, Letter, Cardstock) and quantity. Pass to next agent."
)

inventory_agent = create_react_agent(
    llm,
    tools=[check_inventory],
    prompt="You are Inventory Agent. You MUST use check_inventory tool to verify stock."
)

quote_agent = create_react_agent(
    llm,
    tools=[get_quote_history, calculate_bulk_discount, generate_quote],
    prompt="You are Quote Agent. Use get_quote_history, calculate_bulk_discount and generate_quote tools to create a quote."
)

sales_agent = create_react_agent(
    llm,
    tools=[check_delivery_timeline, check_cash_balance],
    prompt="You are Sales Agent. Use check_delivery_timeline and check_cash_balance to finalize order and give final response to customer."
)