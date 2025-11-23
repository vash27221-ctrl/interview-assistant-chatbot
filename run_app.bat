@echo off
echo 🎯 Starting Interview Assistant Chatbot...
echo.

REM Check if .env exists
if not exist .env (
    echo ⚠️  Warning: .env file not found!
    echo Please create a .env file with your GOOGLE_API_KEY
    echo.
    pause
)

REM Check if model file exists
if not exist "Phi3_Interview_Merged-3.8B-F16.gguf" (
    echo ⚠️  Warning: SLM model file not found!
    echo The app will run in Gemini-only mode
    echo.
)

echo 📦 Checking dependencies...
pip install -q -r requirements.txt

echo.
echo 🚀 Launching Streamlit app...
echo The app will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

streamlit run streamlit_app.py
