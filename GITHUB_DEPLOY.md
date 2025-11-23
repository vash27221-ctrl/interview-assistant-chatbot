# 🚀 GitHub + Streamlit Cloud + ngrok Deployment Guide

## 📋 Overview

This guide will help you:
1. Push your code to GitHub
2. Deploy the web interface to Streamlit Cloud
3. Run your SLM locally on your MacBook Air M4
4. Connect them using ngrok

---

## 🔧 Part 1: Push to GitHub

### Step 1: Initialize Git Repository

```bash
# Navigate to your project directory
cd /path/to/your/project

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Interview Assistant Chatbot"
```

### Step 2: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click the **+** icon → **New repository**
3. Name it: `interview-assistant-chatbot`
4. Keep it **Public** (required for free Streamlit Cloud)
5. **DO NOT** initialize with README (you already have files)
6. Click **Create repository**

### Step 3: Push to GitHub

```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/interview-assistant-chatbot.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note:** The `.gitignore` file will automatically exclude:
- `.env` (your API keys)
- `.gguf` files (too large)
- `__pycache__` and other temp files

---

## 🌐 Part 2: Deploy to Streamlit Cloud

### Step 1: Prepare for Cloud Deployment

Create a cloud-compatible version of `kiro7.py`:

```bash
# We'll modify kiro7.py to detect cloud environment
```

I'll create a modified version for you below.

### Step 2: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select:
   - **Repository**: `YOUR_USERNAME/interview-assistant-chatbot`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
5. Click **"Advanced settings"**
6. Add **Secrets** (TOML format):

```toml
GOOGLE_API_KEY = "your_gemini_api_key_here"
STREAMLIT_CLOUD = "true"
SLM_ENDPOINT = "https://your-ngrok-url.ngrok-free.app"
```

7. Click **"Deploy"**

---

## 💻 Part 3: Set Up Local SLM with ngrok

### Step 1: Install ngrok

```bash
# Install ngrok using Homebrew
brew install ngrok

# Or download from https://ngrok.com/download
```

### Step 2: Sign Up for ngrok (Free)

1. Go to [ngrok.com](https://ngrok.com)
2. Sign up for a free account
3. Get your auth token from the dashboard
4. Configure ngrok:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

### Step 3: Create SLM API Server

I'll create a Flask server to expose your SLM via API.

---

## 📡 Part 4: Connect Everything

### Architecture:

```
┌─────────────────────────────────────────────────┐
│         Streamlit Cloud (Web Interface)         │
│              streamlit_app.py                   │
└────────────────┬────────────────────────────────┘
                 │
                 │ HTTPS
                 ↓
┌─────────────────────────────────────────────────┐
│              Gemini API (Cloud)                 │
│         Question Generation & Analysis          │
└─────────────────────────────────────────────────┘
                 │
                 │ (Optional: SLM Triage)
                 ↓
┌─────────────────────────────────────────────────┐
│         ngrok Tunnel (Public URL)               │
│         https://xxxx.ngrok-free.app             │
└────────────────┬────────────────────────────────┘
                 │
                 │ Tunnel
                 ↓
┌─────────────────────────────────────────────────┐
│      Your MacBook Air M4 (Local)                │
│         Flask API Server                        │
│         Phi-3 SLM Model                         │
└─────────────────────────────────────────────────┘
```

---

## 🎯 Quick Start Commands

### On Your MacBook (Terminal 1):
```bash
# Start the SLM API server
python slm_server.py
```

### On Your MacBook (Terminal 2):
```bash
# Start ngrok tunnel
ngrok http 5000
```

### Copy the ngrok URL:
```
https://xxxx-xx-xx-xxx-xxx.ngrok-free.app
```

### Update Streamlit Cloud Secrets:
Add the ngrok URL to your Streamlit secrets:
```toml
SLM_ENDPOINT = "https://xxxx-xx-xx-xxx-xxx.ngrok-free.app"
```

---

## 🔒 Security Notes

### What's Safe:
✅ ngrok provides HTTPS encryption
✅ API keys stored in Streamlit secrets
✅ SLM runs locally on your machine
✅ No sensitive data leaves your control

### Important:
⚠️ Free ngrok URLs change on restart
⚠️ Update Streamlit secrets when ngrok URL changes
⚠️ Keep your MacBook running for SLM access
⚠️ Consider ngrok paid plan for static URLs

---

## 🐛 Troubleshooting

### Issue: ngrok URL changes
**Solution**: Use ngrok paid plan ($8/month) for static URLs

### Issue: SLM server not responding
**Solution**: Check if Flask server is running on port 5000

### Issue: Streamlit can't reach SLM
**Solution**: Verify ngrok URL in Streamlit secrets

### Issue: Slow performance
**Solution**: This is normal with API calls over internet

---

## 📊 Performance Expectations

### With Local SLM (via ngrok):
- **Latency**: +500ms-1s (internet round trip)
- **Quality**: Full SLM triage functionality
- **Cost**: Free (ngrok free tier)

### Without SLM (Gemini-only):
- **Latency**: Normal API latency
- **Quality**: Still excellent (Gemini handles everything)
- **Cost**: Only Gemini API costs

---

## 🎉 You're Done!

Once everything is set up:
1. ✅ Code is on GitHub
2. ✅ Web interface on Streamlit Cloud
3. ✅ SLM running locally
4. ✅ ngrok tunnel connecting them

**Your app is now publicly accessible!**

Share the Streamlit URL with anyone! 🚀
