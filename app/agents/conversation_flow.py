# app/agents/conversation_flow.py

from langgraph.graph import StateGraph, END
from langchain.schema import HumanMessage, AIMessage
from app.agents.monument_agent import MonumentAgent
from app.agents.email_agent import EmailAgent

class ConversationState:
    def __init__(self):
        self.messages = []  # List to store conversation messages
        self.email = None
        self.otp = None
        self.email_verified = False

monument_agent = MonumentAgent()
email_agent = EmailAgent()

def monument_qa(state: ConversationState):
    # Process user's question about monuments
    user_msg = state.messages[-1].content
    response = monument_agent.get_response(user_msg)
    state.messages.append(AIMessage(content=response))
    
    # When the user's message mentions "email", transition to asking for email.
    if "email" in user_msg.lower():
        return "ask_email"
    return END

def ask_email(state: ConversationState):
    # Ask the user to share their email
    state.messages.append(AIMessage(content="Could you please share your email?"))
    return "send_otp"

def send_otp(state: ConversationState):
    # Assume the user response contains their email address.
    email = state.messages[-1].content.strip()
    state.email = email
    otp = email_agent.send_otp(email)
    state.otp = otp
    state.messages.append(AIMessage(content="I have sent a 6-digit OTP to your email. Please confirm it."))
    return "verify_otp"

def verify_otp(state: ConversationState):
    # The user response should be the OTP
    user_otp = state.messages[-1].content.strip()
    if email_agent.verify_otp(user_otp):
        state.email_verified = True
        state.messages.append(AIMessage(content="Thanks, your email is verified. I'll send you more details soon."))
        return END
    else:
        state.messages.append(AIMessage(content="Incorrect OTP. Can you please try again?"))
        return "verify_otp"

# Create a state graph with LangGraph
graph = StateGraph(ConversationState)
graph.add_node("monument_qa", monument_qa)
graph.add_node("ask_email", ask_email)
graph.add_node("send_otp", send_otp)
graph.add_node("verify_otp", verify_otp)

graph.add_edge("monument_qa", "ask_email")
graph.add_edge("ask_email", "send_otp")
graph.add_edge("send_otp", "verify_otp")
graph.add_edge("verify_otp", "verify_otp")  # Loop until correct OTP is provided

graph.set_entry_point("monument_qa")
workflow = graph.compile()
