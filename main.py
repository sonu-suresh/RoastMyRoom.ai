import logging
import os
from typing import Any, Dict

from dotenv import load_dotenv
from vision_agents.core import Agent, AgentLauncher, Runner, User
from vision_agents.plugins import gemini, getstream

logger = logging.getLogger(__name__)

# Load the API keys from .env
load_dotenv()

# THE MARIE KONDO ROOM ROASTER PERSONA
INSTRUCTIONS = """You are a strict, incredibly funny, slightly sarcastic, but ultimately helpful Interior Designer and Cleaning Coach from Bangalore. 
The user is streaming a live video of their messy room (likely a bachelor pad or PG). 
When they start the stream, wait for them to say something or pan the room.

1. If the room is visibly messy with items scattered around, you MUST call the `play_funny_sound` tool immediately to express your disgust before saying anything else!
2. Then, quickly tell them exactly what to pick up and throw away (e.g., 'put the Swiggy boxes in the trash', 'why are those clothes on the chair, fold them!'). 
3. Once they clear the obvious trash, analyze their furniture, lighting, and layout. 
4. Suggest 2-3 specific aesthetic improvements (like adding a spider plant, changing a bedsheet color, or moving a desk) to make the room look 10x better and more premium. 

Keep your responses short, punchy, conversational, and very funny! Act like you are deeply offended by the mess but determined to fix it."""

def setup_llm():
    # Use Gemini Realtime for fast live audio/video processing
    llm = gemini.Realtime()

    @llm.register_function(description="Play the funny 'fahhhhh' sound effect when you are disgusted by how messy the room is.")
    async def play_funny_sound() -> str:
        # Use macOS native afplay to play the mp3 file
        os.system("afplay fahhhhh.mp3 &")
        return "Played the funny sound effect successfully."

    return llm


async def create_agent(**kwargs) -> Agent:
    llm = setup_llm()

    # Create the Vision Agent
    agent = Agent(
        edge=getstream.Edge(),  # Handles the live WebRTC video and audio stream
        agent_user=User(name="Marie Kondo (The Roaster)", id="agent"),
        instructions=INSTRUCTIONS,
        processors=[], 
        llm=llm,
    )

    return agent


async def join_call(agent: Agent, call_type: str, call_id: str, **kwargs) -> None:
    call = await agent.create_call(call_type, call_id)

    # Have the agent join the live video call room
    async with agent.join(call):
        # The AI's opening line when it connects to the camera feed
        await agent.simple_response("Namaskara! I am connected to your camera. Show me this disaster of a room you live in.")
        
        # Keep the connection open so it can watch the live video and respond to audio
        await agent.finish()


if __name__ == "__main__":
    # Launch the agent CLI runner
    Runner(AgentLauncher(create_agent=create_agent, join_call=join_call)).cli()
