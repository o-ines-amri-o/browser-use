from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
response = llm.invoke("What is the capital of France?")
print("🔁 Response from GPT:", response)
