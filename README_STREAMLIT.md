# 🎯 Interview Assistant Chatbot - Streamlit Deployment Guide

## 📋 Overview
A highly interactive web-based AI interview assistant with modern UI features including:
- 🎨 Customizable theme colors
- ⚡ Typewriter effect for questions
- 📊 Expandable analysis dropdowns
- 📱 Mobile-responsive design
- 🎭 Smooth animations and transitions
- ⚙️ Adjustable font sizes and speeds

## 🚀 Quick Start

### Local Development

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Set Up Environment Variables**
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

3. **Ensure Required Files**
Make sure these files are in your project directory:
- `streamlit_app.py` (main app)
- `kiro7.py` (interview orchestrator)
- `momentum_signal.py` (momentum computation)
- `Phi3_Interview_Merged-3.8B-F16.gguf` (SLM model)
- `.env` (API keys)

4. **Run Locally**
```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🌐 Streamlit Cloud Deployment

### Option 1: Deploy with Local SLM (Hybrid Setup)

**Note:** Streamlit Cloud has limited resources. For best performance with the local SLM model, consider:

1. **Deploy to Streamlit Cloud** (for the web interface)
2. **Run SLM locally** on your PC
3. **Use ngrok or similar** to expose your local SLM endpoint

#### Steps:

1. **Prepare Repository**
   - Push your code to GitHub
   - Include: `streamlit_app.py`, `kiro7.py`, `momentum_signal.py`, `requirements.txt`
   - **DO NOT** include the `.gguf` model file (too large for GitHub)

2. **Modify for Cloud Deployment**
   
   Update `kiro7.py` to make SLM optional:
   ```python
   # In InterviewOrchestrator.__init__, modify SLM loading:
   self.slm_model = None
   if os.path.exists(SLM_MODEL_PATH):
       try:
           # existing SLM loading code
       except Exception as e:
           print("SLM not available, using Gemini-only mode")
   else:
       print("SLM model not found, using Gemini-only mode")
   ```

3. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Select `streamlit_app.py` as the main file
   - Add secrets in Streamlit Cloud dashboard:
     - Go to App Settings → Secrets
     - Add: `GOOGLE_API_KEY = "your_key_here"`

4. **Run SLM Locally (Optional)**
   - Keep the SLM running on your PC for better performance
   - The app will fall back to Gemini-only mode if SLM is unavailable

---

### Option 2: Gemini-Only Deployment (Recommended for Cloud)

For pure cloud deployment without local dependencies:

1. **Modify `kiro7.py`** to skip SLM loading in cloud environment:
```python
# Add at the top of __init__
import platform
IS_CLOUD = os.getenv("STREAMLIT_CLOUD", "false").lower() == "true"

if IS_CLOUD:
    self.slm_model = None
    print("Running in cloud mode (Gemini-only)")
else:
    # existing SLM loading code
```

2. **Set Environment Variable in Streamlit Cloud**
   - In Secrets: `STREAMLIT_CLOUD = "true"`

3. **Deploy** following the same steps as Option 1

---

## 🎨 Features

### Interactive UI Elements

1. **Theme Customization**
   - Color picker in sidebar
   - Adjustable font sizes
   - Typewriter speed control

2. **Chat Interface**
   - Gradient message bubbles
   - Smooth animations
   - Typing indicators
   - Role-based styling

3. **Analysis Dropdown**
   - Expandable analysis for each answer
   - Shows answer type, notes, and summary
   - **Score is hidden** from user view

4. **Progress Tracking**
   - Question counter
   - Topic progression
   - Interview statistics

### Mobile Responsive
- Adapts to all screen sizes
- Touch-friendly interface
- Optimized for mobile browsers

---

## 📁 File Structure

```
project/
├── streamlit_app.py              # Main Streamlit app
├── kiro7.py                      # Interview orchestrator
├── momentum_signal.py            # Momentum computation
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (local only)
├── Phi3_Interview_Merged-3.8B-F16.gguf  # SLM model (local only)
└── README_STREAMLIT.md          # This file
```

---

## ⚙️ Configuration

### Environment Variables

**Required:**
- `GOOGLE_API_KEY` - Your Gemini API key

**Optional:**
- `STREAMLIT_CLOUD` - Set to "true" for cloud deployment
- `SLM_MODEL_PATH` - Path to local SLM model (default in kiro7.py)

### Streamlit Secrets (Cloud Deployment)

Add in Streamlit Cloud dashboard under App Settings → Secrets:

```toml
GOOGLE_API_KEY = "your_gemini_api_key"
STREAMLIT_CLOUD = "true"
```

---

## 🐛 Troubleshooting

### Issue: SLM Model Not Loading
- **Solution**: Ensure the `.gguf` file is in the project directory
- **Cloud**: Use Gemini-only mode (SLM won't work on Streamlit Cloud)

### Issue: Rate Limit Errors
- **Solution**: The app handles 429 errors gracefully
- Wait a few minutes and try again
- Consider upgrading your Gemini API quota

### Issue: Slow Performance
- **Solution**: Adjust typewriter speed in sidebar
- Use Gemini-only mode for faster cloud performance
- Run SLM locally for hybrid setup

### Issue: Mobile Display Issues
- **Solution**: The app is responsive, but some features work best on desktop
- Use landscape mode on mobile for better experience

---

## 🎯 Usage Tips

1. **Start Simple**: Begin with basic technical domains
2. **Natural Answers**: Respond conversationally, not in bullet points
3. **View Analysis**: Expand dropdowns to see feedback
4. **Adjust Settings**: Customize theme and speed in sidebar
5. **Type 'quit'**: End interview anytime

---

## 📊 Performance Notes

### Local Setup (Recommended)
- Full SLM + Gemini functionality
- Faster response times
- Better question quality

### Cloud Setup (Streamlit Cloud)
- Gemini-only mode
- Slightly slower due to API calls
- No local model required
- Accessible from anywhere

---

## 🔒 Security Notes

- Never commit `.env` file to GitHub
- Use Streamlit Secrets for API keys in cloud
- Keep your Gemini API key private
- The `.gguf` model file is too large for GitHub (use Git LFS if needed)

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
3. Check Gemini API status: [ai.google.dev](https://ai.google.dev)

---

## 🎉 Enjoy Your Interview Assistant!

The chatbot is designed to provide an engaging, interactive interview experience with modern UI/UX features. Customize it to your liking and good luck with your interviews!
