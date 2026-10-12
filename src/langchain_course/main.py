from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama


@tool
def search(query: str) -> str:
    """
    Tool that search over the internet

    Args:
        query: The query to search for

    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return "Answering query..."


llm = ChatOllama(
    temperature=0,
    model="gemma4:31b-cloud",
    base_url="https://ollama.com"
)

tools = [search]

agent = create_agent(
    model=llm,
    tools=tools
)

def main() -> None:
    print("Hello from langchain-course!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="What is the weather in Montreal?"
            )
        }
    )
    print(result)


if __name__ == "__main__":
    main()
