# Hybrid Interview Bot (SLM + Gemini)

This project is a CLI-based technical interview bot that uses a hybrid AI model:

* **Local SLM (`llama-cpp-python`):** Generates fast, natural-sounding follow-up questions.
* **Gemini API (LLM):** Used for strategic, in-depth tasks like scoring answers and providing feedback.

The system runs the local SLM by default and intelligently falls back to the Gemini API if the local model fails or isn't configured.

---

## File Structure

* `main.py` : The main orchestrator that runs the interview loop.
* `slm_followup.py` : Interface for the local SLM (uses `llama-cpp-python` library).
* `gemini_api.py` : Client for the Google Gemini API.
* `evaluator.py` : Handles scoring logic (via Gemini) and clarity detection.
* `state_manager.py` : Manages the conversation history and session state.
* `prompt_templates.py`: Stores the prompts for the AI models.
* `logger.py`: Simple JSONL logger for event tracking.

---

## 🚀 How to Run

1.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download a GGUF Model:**
    This project requires a GGUF-formatted model to be run by `llama-cpp-python`. You can download one, such as `gemma-2b-it.gguf`, and place it in a `./models` directory.

4.  **Set Up Environment Variables:**
    Create a file named `.env` in the root directory and add your keys:

    ```.env
    # Your Google AI Studio API Key
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    
    # Path to your downloaded GGUF model
    LLAMA_MODEL_PATH="./models/gemma-2b-it.gguf"
    ```

5.  **Run the Interview Bot:**
    ```bash
    python main.py
    ```