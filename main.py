# Main entrypoint for PromptOps
import asyncio
from dotenv import load_dotenv
import os
from promptops.agents.working import handle_user_prompt
def main():

    load_dotenv(override=True)  # Load environment variables from .env file if needed
    # print("env loaded",os.getenv("OPENAI_API_KEY"), os.getenv("GEMINI_API_KEY"))
    print("main.py: Starting PromptOps...")
    prompt = input("PromptOps > ")
    asyncio.run(handle_user_prompt(prompt))

if __name__ == "__main__":
    main()
