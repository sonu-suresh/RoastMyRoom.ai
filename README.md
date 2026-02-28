# RoastMyRoom.ai 🧹

A strict, sarcastic, yet ultimately helpful AI interior designer for messy rooms built using the [Vision-Agents framework](https://github.com/GetStream/Vision-Agents) and Gemini Realtime API! 

This AI project streams your live video and audio, taking on the persona of "Marie Kondo (The Roaster)" - an incredibly funny, slightly sarcastic, and deeply offended Interior Designer from Bangalore.

## Features ✨

* **Realtime Video & Audio Analysis:** Streams live from your camera using WebRTC to analyze your room instantly.
* **The Look of Disgust ("Fahhhhhhh" Expression):** If the AI detects items scattered around in a visibly messy room, it will instantly play a deeply offended **"fahhhhhhh"** sound effect 🔉 to express its disgust before even saying a word.
* **Cleaning Instructions:** It will quickly identify obvious trash or scattered clothes and instruct you humorously on exactly what you need to pick up or throw away.
* **Aesthetics and Improvement Suggestions:** Once the obvious trash is cleared, the AI acts as your interior design coach. It analyzes your furniture, lighting, and layout, offering 2-3 specific, premium aesthetic improvements (e.g., adding a plant or fixing the desk setup) to make the space look 10x better!

## How Vision Agents is Used 🧠

This project leverages the **Vision Agents** framework to effortlessly orchestrate a multimodal, real-time AI assistant:

- **Core Agent Architecture:** We use `vision_agents.core.Agent` to tie together the LLM, the video/audio stream, the persona instructions, and the user identity. It manages the entire lifecycle of the interaction.
- **Multimodal LLM Integration:** Powered by the `gemini.Realtime()` plugin, the agent simultaneously processes the live visual feed of the room and the user's spoken audio for native, instantaneous context understanding.
- **Real-Time WebRTC Streaming:** We utilize the `getstream.Edge()` plugin to handle the complex WebRTC infrastructure, ensuring a seamless, low-latency live video connections between the user's camera and the AI.
- **Custom Tool Calling:** We use the framework's `@llm.register_function` decorator to give the agent the ability to execute local machine commands (like playing the `fahhhhh.mp3` sound via macOS's `afplay`) autonomously when it detects a messy room.
- **Easy Bootstrapping:** `AgentLauncher` and `Runner` are used to wrap the agent creation into a clean CLI application that handles asynchronous runtime execution and call joining out-of-the-box.

## Prerequisites 🛠️

- Python 3.10+
- The `uv` package manager (optional, but recommended)
- macOS (for native `afplay` sound command compatibility)

## Setup Instructions 🚀

1. **Clone the repository and access the directory:**
    ```bash
    cd RoastMyRoom.ai
    ```

2. **Install the dependencies:**
    This project uses `uv` for dependency management. 
    ```bash
    uv sync
    ```
    *Alternatively, you can create a virtual environment and use pip if you do not have uv.*

3. **Set up Environment Variables:**
    Copy the template `.env.template` into a `.env` file and fill in your API keys (e.g., Google Gemini API key and GetStream keys for WebRTC).
    ```bash
    cp .env.template .env
    ```

4. **Verify Audio Asset:**
    Ensure the `fahhhhh.mp3` file is located in the root directory.

## Running the Agent 🏃‍♂️

Launch the CLI runner to start your video stream with the AI.

```bash
uv run main.py
```

The AI will join the call, connect to your live camera feed, and greet you with a "Namaskara! I am connected to your camera. Show me this disaster of a room you live in." 

Pan your room and let the roasting (and cleaning) begin!
