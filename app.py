# from langchain_google_genai import ChatGoogleGenerativeAI
# from browser_use import Agent
# from pydantic import SecretStr
# import os
# from dotenv import load_dotenv
# load_dotenv()
# import asyncio

# api_key = os.getenv("GEMINI_API_KEY")

# async def main():
#     agent = Agent(
#         task="Go to instagram browser and logins are username-a_ashok_kumar_k and password-FearLess@123,and press info and go to message chat with Bhargavi Shamala,where are u now ",
#         llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY'))),
#     )
#     await agent.run()

# asyncio.run(main())


# """
# from langchain_openai import ChatOpenAI
# from browser_use import Agent
# import asyncio
# from dotenv import load_dotenv
# load_dotenv()

# async def main():
#     agent = Agent(
#         task="Go to browser and search for bolt new and logins are username-babyvit074@gmail.com,password-Fearless@123 and search for create a website for aidays 2025 in bolt new",
#         llm=ChatOpenAI(model="gpt-4o"),
#     )
#     await agent.run()

# asyncio.run(main())"""
