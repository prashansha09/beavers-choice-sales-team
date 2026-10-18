from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
import operator

class SalesState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
    customer_request: str
    paper_type: str
    quantity: int
    inventory_result: str
    history_result: str
    quote_result: str
    final_response: str