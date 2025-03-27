import os
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

async def main():
    agent = Agent(
    task="""
    Go to the EPFL Laboratories List website
    Your goal is:
    - To find a lab focused on AI, artificial intelligence, machine learning, deep learning in healthcare, medicine, or biology
    - I recommend you look through the list instead of using the search, look for think like NeuroAI lab
    - Click into the lab’s website
    - Look for project sections such as: “Master Projects”, “Student Projects”, “Open Positions”,“Join”
    - If projects mention AI OR artificial intelligence OR machine learning OR deep learning AND healthcare OR medicine OR biology OR any related term:
    You must: get the labme na, the Professor’s name, a contact Email, the Project title, project description and the Link to the project page
    THEN: Open this Google Doc and write the information you find:
    https://docs.google.com/document/d/1g03OaTBOFN_yn5qc93tqzAXMWC3Ken0x5fwfqj7UVOs/edit?tab=t.0
    
    Once this is done, check you have added all the information, AND that there are not duplicates in text. 
    If you find duplicated information then delete it.
    once this is done,
    your task is completed successfully. Congratulations!
    """
    ,
        llm=ChatOpenAI(model="gpt-4o"),
    )
    print("🔐 OpenAI Key Loaded:", os.getenv("OPENAI_API_KEY")[:10], "...")  # Just a preview

    await agent.run()

asyncio.run(main())
