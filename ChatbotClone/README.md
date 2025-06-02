Alayssa AI - Offline Personal Assistant
A personalized offline AI assistant built with Ollama and Flask, designed to mimic the personality and communication style of Alayssa Hernandez - a 21-year-old Computer Science student.

🚀 Features
Offline Operation: Runs completely offline using Ollama
Personalized Responses: Trained to respond with Alayssa's personality and communication style
Web Interface: Beautiful, responsive chat interface
Real-time Status: Shows connection status and model availability
Mobile Friendly: Works great on both desktop and mobile devices
📋 Prerequisites
Python 3.7+ installed on your system
Ollama installed from https://ollama.ai
Flask and requests Python packages
🛠️ Installation Steps
Step 1: Install Ollama
bash
# Visit https://ollama.ai and install Ollama for your operating system
# On macOS: brew install ollama
# On Linux: curl -fsSL https://ollama.ai/install.sh | sh
Step 2: Download Base Model
bash
ollama pull llama3.2:1b
Step 3: Create Custom Model
Save the Modelfile in your project directory, then run:

bash
ollama create alayssa-ai -f Modelfile
Step 4: Install Python Dependencies
bash
pip install flask requests
Step 5: Set Up Project Structure
Create the following directory structure:

alayssa-ai/
├── Modelfile
├── personal_info.json
├── app.py
├── training_conversations.md
├── Parameter_Tuning_Guide.md
├── templates/
│   └── index.html
└── README.md
Step 6: Start the Application
bash
python app.py
Step 7: Access the Interface
Open your browser and go to: http://localhost:5000

📁 File Descriptions
Core Files
Modelfile: Ollama model configuration with Alayssa's personality and system prompt
personal_info.json: Structured data about Alayssa's background, interests, and personality
app.py: Flask server that handles API requests and serves the web interface
templates/index.html: Beautiful web interface for chatting with the AI
Training and Documentation
training_conversations.md: Example conversations showing Alayssa's communication style
Parameter_Tuning_Guide.md: Comprehensive guide for fine-tuning model parameters
README.md: This setup guide
🎯 Personality Features
Alayssa AI is designed to:

Use casual language with slang and call friends "sis" and "teh"
Show enthusiasm about AI, programming (especially Python), and her academic achievements
Discuss her interests: FPS games, music, fashion, and makeup
Provide emotional support with high emotional intelligence
Share her career goals in forensics and desire for well-paying jobs
Be slightly introverted with new people but warm with friends
🔧 API Endpoints
GET /: Main chat interface
POST /api/chat: Send messages to the AI
GET /api/health: Check Ollama and model status
GET /api/info: Get personal information
GET /setup: Setup instructions
🚨 Troubleshooting
Model Not Loading
bash
# Check if Ollama is running
ollama list

# Recreate the model if needed
ollama create alayssa-ai -f Modelfile
Connection Issues
Ensure Ollama is running on port 11434
Check if the custom model alayssa-ai exists
Restart Ollama service if needed
Web Interface Issues
Make sure Flask is running on port 5000
Check that templates/index.html exists
Verify personal_info.json is in the same directory as app.py
🎨 Customization
Modifying Personality
Edit the SYSTEM section in the Modelfile to change personality traits, then recreate the model:

bash
ollama create alayssa-ai -f Modelfile
Fine-tuning Parameters
The Modelfile includes comprehensive parameters for fine-tuning response quality:

Response Style: Adjust temperature, top_p, top_k for creativity vs consistency
Memory: Configure num_ctx, num_keep for conversation context
Quality: Use mirostat settings for consistent response quality
Performance: Set num_thread, num_gpu for optimal speed
See Parameter_Tuning_Guide.md for detailed explanations and presets.

Adding New Information
Update personal_info.json with new details about preferences, experiences, or background.

Training Examples
Add new conversation examples to training_conversations.md to reference how Alayssa should respond in different scenarios.

📱 Usage Tips
Natural Conversation: Talk to Alayssa naturally - she's designed to be conversational and friendly
Academic Topics: Ask about AI, programming, or her thesis project for detailed responses
Personal Interests: Discuss games, music, fashion, or career goals
Emotional Support: Share problems or concerns - Alayssa has high emotional intelligence
Casual Chat: Use casual language and slang - she'll match your energy!
⚡ Performance Notes
Initial response may take a few seconds as the model loads
Responses are generated locally on your machine
Model uses approximately 1-2GB of RAM when active
No internet connection required after initial setup
🔒 Privacy
All conversations are processed locally on your machine
No data is sent to external servers
Chat history is not saved between sessions
Complete privacy and data control
🤝 Contributing
Feel free to:

Add more training examples in training_conversations.md
Improve the web interface design
Add new API endpoints for additional functionality
Enhance the personality in the Modelfile
📄 License
This project is for educational and personal use. Please respect the open-source licenses of the underlying technologies (Ollama, Flask, etc.).

Enjoy chatting with Alayssa! 🎮🎵💄

