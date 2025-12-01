import os
import sys
import asyncio
from dotenv import load_dotenv
from colorama import init, Fore, Style

# Load environment variables
load_dotenv()

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from career_compass.agent import root_agent
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Initialize Colorama
init(autoreset=True)

async def main():
    print(Fore.CYAN + "Welcome to Career Compass!")
    print(Fore.CYAN + "========================")

    if not os.getenv("GOOGLE_API_KEY"):
        print(Fore.RED + "Error: GOOGLE_API_KEY not found.")
        return

    # Initialize ADK Runner
    session_service = InMemorySessionService()
    app_name = root_agent.name  # Use the agent's name as app_name
    runner = Runner(
        app_name=app_name,
        agent=root_agent,
        session_service=session_service
    )
    
    # Create a session
    session = await session_service.create_session(
        app_name=app_name,
        user_id="user_001"
    )
    
    print("Career Compass: Hello! How can I help you with your study abroad plans today?")
    
    while True:
        user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL)
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Career Compass: Goodbye!")
            break
        
        try:
            # Run the agent with user input
            content = types.Content(parts=[types.Part(text=user_input)])
            
            # Collect response
            response_text = ""
            async for event in runner.run_async(
                user_id="user_001",
                session_id=session.id,
                new_message=content
            ):
                if hasattr(event, 'content') and event.content:
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            response_text += str(part.text)
            
            if response_text:
                print(Fore.CYAN + f"Career Compass: {response_text}")
            else:
                print(Fore.YELLOW + "Career Compass: (No response)")
                
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
