from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch



llm = ChatOllama(
    temperature=0,
    model="gemma4:31b-cloud",
    base_url="https://ollama.com"
)

tools = [TavilySearch()]

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
