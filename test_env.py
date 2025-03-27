import os
from dotenv import load_dotenv

load_dotenv()  # This loads your .env file

# Print the value of your OpenAI API key
print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
