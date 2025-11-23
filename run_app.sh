#!/bin/bash

echo "🎯 Starting Interview Assistant Chatbot..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Please create a .env file with your GOOGLE_API_KEY"
    echo ""
    read -p "Press Enter to continue anyway or Ctrl+C to exit..."
fi

# Check if model file exists
if [ ! -f "Phi3_Interview_Merged-3.8B-F16.gguf" ]; then
    echo "⚠️  Warning: SLM model file not found!"
    echo "The app will run in Gemini-only mode"
    echo ""
fi

# Install requirements if needed
echo "📦 Checking dependencies..."
pip install -q -r requirements.txt

echo ""
echo "🚀 Launching Streamlit app..."
echo "The app will open in your browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run streamlit_app.py
