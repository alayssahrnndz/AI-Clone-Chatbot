from flask import Flask, request, jsonify, render_template
import requests
import json
import os

app = Flask(__name__)

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "alayssa-ai"  # Custom model name after creating from modelfile


# Load personal information
def load_personal_info():
    try:
        with open('personal_info.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


personal_info = load_personal_info()


@app.route('/')
def index():
    """Serve the main web interface"""
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests to Ollama"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Prepare payload for Ollama
        payload = {
            "model": MODEL_NAME,
            "prompt": user_message,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 40
            }
        }

        # Send request to Ollama
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)

        if response.status_code == 200:
            result = response.json()
            ai_response = result.get('response', 'Sorry, I could not generate a response.')
            return jsonify({'response': ai_response})
        else:
            return jsonify({'error': f'Ollama API error: {response.status_code}'}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Connection error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/api/info')
def get_info():
    """Get personal information"""
    return jsonify(personal_info)


@app.route('/api/health')
def health_check():
    """Check if Ollama is running"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_exists = any(model.get('name') == MODEL_NAME for model in models)
            return jsonify({
                'ollama_status': 'running',
                'model_loaded': model_exists,
                'available_models': [model.get('name') for model in models]
            })
        else:
            return jsonify({'ollama_status': 'error', 'model_loaded': False}), 500
    except requests.exceptions.RequestException:
        return jsonify({'ollama_status': 'not_running', 'model_loaded': False}), 500


@app.route('/setup')
def setup_guide():
    """Provide setup instructions"""
    instructions = {
        'steps': [
            '1. Install Ollama from https://ollama.ai',
            '2. Pull the base model: ollama pull llama3.2:1b',
            '3. Create custom model: ollama create alayssa-ai -f Modelfile',
            '4. Start this Flask app: python app.py',
            '5. Visit http://localhost:5000 to use the chat interface'
        ],
        'requirements': [
            'Ollama installed and running',
            'llama3.2:1b model downloaded',
            'Custom model created from Modelfile',
            'Python Flask installed'
        ]
    }
    return jsonify(instructions)


if __name__ == '__main__':
    print("Starting Alayssa AI Chat Server...")
    print("Make sure Ollama is running and the model is loaded!")
    print("Visit /setup for setup instructions")
    app.run(debug=True, host='0.0.0.0', port=5000)