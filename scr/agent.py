import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain import hub

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM (OpenAI GPT-4o-mini)
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the search tool (Tavily)
search = TavilySearchResults(max_results=3)

# Define tools available to the agent
tools = [search]

# Initialize conversational memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Pull a predefined prompt from LangChain hub for agent behavior
prompt = hub.pull("hwchase17/openai-functions-agent")

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Function to run the agent with a user query
def run_agent(query):
    response = agent.run(query)
    return response

# Example usage
if __name__ == "__main__":
    # Test the agent with a question
    query = "What is the capital of France?"
    response = run_agent(query)
    print("Query:", query)
    print("Response:", response)

    # Test follow-up question to demonstrate memory
    follow_up = "What is its largest city?"
    response = run_agent(follow_up)
    print("\nQuery:", follow_up)
    print("Response:", response)