"""
Flask API Server for Local SLM Model
Exposes the Phi-3 model via REST API for remote access through ngrok
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_cpp import Llama
import os
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for Streamlit Cloud access

# Configuration
SLM_MODEL_PATH = "Phi3_Interview_Merged-3.8B-F16.gguf"
PORT = 5000

# Global model instance
slm_model = None

def load_model():
    """Load the SLM model on server startup"""
    global slm_model
    print(f"🔄 Loading SLM model from: {SLM_MODEL_PATH}")
    print("⏳ This may take a moment...")
    
    start_time = time.time()
    
    try:
        slm_model = Llama(
            model_path=SLM_MODEL_PATH,
            n_gpu_layers=-1,  # Use all GPU layers (M4 GPU)
            n_ctx=2048,
            verbose=False
        )
        
        load_time = time.time() - start_time
        print(f"✅ SLM model loaded successfully in {load_time:.2f} seconds")
        print(f"🚀 Server ready on port {PORT}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to load SLM model: {e}")
        return False

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "model_loaded": slm_model is not None,
        "model_path": SLM_MODEL_PATH
    })

@app.route('/generate', methods=['POST'])
def generate():
    """
    Generate text using the SLM model
    
    Expected JSON payload:
    {
        "messages": [
            {"role": "system", "content": "..."},
            {"role": "user", "content": "..."},
            {"role": "assistant", "content": "..."}
        ],
        "max_tokens": 80,
        "temperature": 0.25,
        "stop": ["<|end|>", "<|user|>"]
    }
    """
    if slm_model is None:
        return jsonify({
            "error": "Model not loaded",
            "success": False
        }), 503
    
    try:
        data = request.json
        
        # Extract parameters
        messages = data.get('messages', [])
        max_tokens = data.get('max_tokens', 80)
        temperature = data.get('temperature', 0.25)
        stop = data.get('stop', ["<|end|>", "<|user|>", "You:", "Candidate:", "Interviewer:"])
        
        if not messages:
            return jsonify({
                "error": "No messages provided",
                "success": False
            }), 400
        
        # Generate response
        start_time = time.time()
        
        output = slm_model.create_chat_completion(
            messages=messages,
            max_tokens=max_tokens,
            stop=stop,
            temperature=temperature
        )
        
        generation_time = time.time() - start_time
        
        # Extract the generated text
        generated_text = output['choices'][0]['message']['content'].strip()
        
        return jsonify({
            "success": True,
            "text": generated_text,
            "generation_time": generation_time,
            "tokens_used": output['usage']['total_tokens']
        })
        
    except Exception as e:
        print(f"❌ Generation error: {e}")
        return jsonify({
            "error": str(e),
            "success": False
        }), 500

@app.route('/triage', methods=['POST'])
def triage():
    """
    Specialized endpoint for interview question triage
    Matches the _get_slm_triage_question functionality
    
    Expected JSON payload:
    {
        "topic": "Machine Learning",
        "conversation_history": [
            {"role": "assistant", "content": "..."},
            {"role": "user", "content": "..."}
        ],
        "system_prompt": "..."
    }
    """
    if slm_model is None:
        return jsonify({
            "error": "Model not loaded",
            "success": False
        }), 503
    
    try:
        data = request.json
        
        topic = data.get('topic', '')
        conversation_history = data.get('conversation_history', [])
        system_prompt = data.get('system_prompt', '')
        
        # Build messages
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.extend(conversation_history)
        
        # Generate triage question
        start_time = time.time()
        
        output = slm_model.create_chat_completion(
            messages=messages,
            max_tokens=80,
            stop=["<|end|>", "<|user|>", "You:", "Candidate:", "Interviewer:"],
            temperature=0.25
        )
        
        generation_time = time.time() - start_time
        
        next_question = output['choices'][0]['message']['content'].strip()
        
        # Check for confidence low signal
        if not next_question or "[CONFIDENCE_LOW]" in next_question:
            return jsonify({
                "success": True,
                "confidence": "low",
                "text": "[CONFIDENCE_LOW]",
                "generation_time": generation_time
            })
        
        # Validate the question (same logic as in kiro7.py)
        import re
        
        def meaningful_word_count(s):
            fillers = {"umm", "ummm", "uh", "uhh", "hmm", "er", "ah", "like", "...", "uhm"}
            tokens = re.findall(r"[A-Za-z']+", s.lower())
            meaningful = [t for t in tokens if t not in fillers and len(t) > 1]
            return len(meaningful)
        
        hesitation_tokens = ["umm", "ummm", "uh", "uhh", "hmm", "er", "ah", "...", "uhm"]
        
        if any(tok in next_question.lower() for tok in hesitation_tokens):
            return jsonify({
                "success": True,
                "confidence": "low",
                "text": "[CONFIDENCE_LOW]",
                "reason": "hesitation_detected",
                "generation_time": generation_time
            })
        
        if meaningful_word_count(next_question) < 3:
            return jsonify({
                "success": True,
                "confidence": "low",
                "text": "[CONFIDENCE_LOW]",
                "reason": "too_short",
                "generation_time": generation_time
            })
        
        # Valid question
        return jsonify({
            "success": True,
            "confidence": "high",
            "text": next_question,
            "generation_time": generation_time,
            "tokens_used": output['usage']['total_tokens']
        })
        
    except Exception as e:
        print(f"❌ Triage error: {e}")
        return jsonify({
            "error": str(e),
            "success": False
        }), 500

@app.route('/', methods=['GET'])
def index():
    """Root endpoint with API documentation"""
    return jsonify({
        "name": "Interview Assistant SLM API",
        "version": "1.0.0",
        "status": "running",
        "model_loaded": slm_model is not None,
        "endpoints": {
            "/health": "GET - Health check",
            "/generate": "POST - Generate text",
            "/triage": "POST - Interview question triage"
        },
        "documentation": "See GITHUB_DEPLOY.md for usage"
    })

if __name__ == '__main__':
    print("=" * 60)
    print("🎯 Interview Assistant SLM API Server")
    print("=" * 60)
    
    # Load model on startup
    if not load_model():
        print("❌ Failed to start server: Model loading failed")
        exit(1)
    
    print("\n" + "=" * 60)
    print("📡 Starting Flask server...")
    print(f"🌐 Local URL: http://localhost:{PORT}")
    print("🔗 Use ngrok to expose this server publicly")
    print("   Command: ngrok http 5000")
    print("=" * 60 + "\n")
    
    # Run Flask server
    app.run(
        host='0.0.0.0',  # Accept connections from any IP
        port=PORT,
        debug=False,  # Set to True for development
        threaded=True  # Handle multiple requests
    )
