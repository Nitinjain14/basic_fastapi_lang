from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# Use the Ollama model for deepseek
llm = Ollama(model="deepseek-r1:1.5b")

# Function to send a message using LangChain
def ask_llm_with_langchain(query: str) -> str: #both i/p and o/p is string type
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=query)
    ]

    return llm.invoke(messages)
