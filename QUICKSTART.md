# ⚡ Quick Start Guide

## 🚀 Get Running in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up API Key
Create a `.env` file:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Step 3: Run the App
```bash
streamlit run streamlit_app.py
```

**Or use the helper scripts:**
- Mac/Linux: `./run_app.sh`
- Windows: `run_app.bat`

---

## 🎯 That's It!

The app will open in your browser at `http://localhost:8501`

### First Time Using?
1. Enter an interview domain (e.g., "Python Programming")
2. Click "Start Interview"
3. Answer questions naturally
4. View analysis by expanding dropdowns
5. Type 'quit' to end anytime

### Customize Your Experience
- **Theme Color**: Pick your favorite color in the sidebar
- **Font Size**: Adjust for comfortable reading
- **Question Speed**: Control the typewriter effect

---

## 📱 Mobile Access

Want to use on your phone?
1. Find your computer's local IP (e.g., 192.168.1.100)
2. Run: `streamlit run streamlit_app.py --server.address 0.0.0.0`
3. On phone, visit: `http://YOUR_IP:8501`

---

## 🌐 Deploy to Cloud

Want to share with others?

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo
4. Add your API key in Secrets
5. Deploy!

See `README_STREAMLIT.md` for detailed instructions.

---

## 🐛 Troubleshooting

**App won't start?**
- Check Python version (need 3.8+)
- Verify `.env` file exists
- Make sure all dependencies installed

**SLM not loading?**
- That's okay! App works in Gemini-only mode
- For full features, ensure `.gguf` file is present

**Rate limit errors?**
- App handles these gracefully
- Wait a few minutes and try again

---

## 💡 Pro Tips

1. **Better Questions**: The more natural your answers, the better the follow-ups
2. **View Analysis**: Always check the analysis dropdown for feedback
3. **Adjust Speed**: Slow down the typewriter if questions appear too fast
4. **Mobile Friendly**: Works great on phones in landscape mode
5. **Save Progress**: Interview state is maintained during the session

---

## 📚 More Info

- **Full Features**: See `FEATURES.md`
- **Deployment Guide**: See `README_STREAMLIT.md`
- **Deployment Checklist**: See `DEPLOYMENT_CHECKLIST.md`

---

## 🎉 Enjoy!

You're all set! Have a great interview experience! 🚀
