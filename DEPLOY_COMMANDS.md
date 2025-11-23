# 🚀 Complete Deployment Commands

## Copy-Paste Ready Commands for Full Deployment

---

## 📦 Part 1: Push to GitHub

### Step 1: Initialize and Commit

```bash
# Navigate to your project
cd /path/to/your/project

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Interview Assistant Chatbot"
```

### Step 2: Create GitHub Repository

1. Go to: https://github.com/new
2. Repository name: `interview-assistant-chatbot`
3. Keep it **PUBLIC**
4. **DO NOT** initialize with README
5. Click "Create repository"

### Step 3: Push to GitHub

```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/interview-assistant-chatbot.git

# Push
git branch -M main
git push -u origin main
```

---

## 🌐 Part 2: Deploy to Streamlit Cloud

### Step 1: Go to Streamlit Cloud

Visit: https://share.streamlit.io

### Step 2: Create New App

1. Click "New app"
2. Select your repository: `YOUR_USERNAME/interview-assistant-chatbot`
3. Branch: `main`
4. Main file: `streamlit_app.py`

### Step 3: Add Secrets

Click "Advanced settings" → "Secrets"

Add this (replace with your actual API key):

```toml
GOOGLE_API_KEY = "your_actual_gemini_api_key_here"
STREAMLIT_CLOUD = "true"
```

### Step 4: Deploy

Click "Deploy" and wait ~2-3 minutes

---

## 💻 Part 3: Set Up Local SLM with ngrok

### Step 1: Install ngrok

```bash
# Mac (Homebrew)
brew install ngrok

# Or download from: https://ngrok.com/download
```

### Step 2: Sign Up and Configure

1. Go to: https://ngrok.com
2. Sign up (free)
3. Get your authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken
4. Configure:

```bash
# Replace with your actual token
ngrok config add-authtoken YOUR_NGROK_AUTH_TOKEN
```

### Step 3: Start SLM Server

Open Terminal 1:

```bash
cd /path/to/your/project
python slm_server.py
```

Wait for:
```
✅ SLM model loaded successfully
🚀 Server ready on port 5000
```

### Step 4: Start ngrok

Open Terminal 2:

```bash
ngrok http 5000
```

Look for this line:
```
Forwarding    https://xxxx-xx-xx-xxx-xxx.ngrok-free.app -> http://localhost:5000
```

**Copy that URL!**

### Step 5: Update Streamlit Secrets

1. Go back to: https://share.streamlit.io
2. Click your app → Settings → Secrets
3. Add this line (with YOUR ngrok URL):

```toml
GOOGLE_API_KEY = "your_gemini_key"
STREAMLIT_CLOUD = "true"
SLM_ENDPOINT = "https://xxxx-xx-xx-xxx-xxx.ngrok-free.app"
```

4. Save (app will auto-restart)

---

## ✅ Verification Commands

### Test Local SLM Server

```bash
curl http://localhost:5000/health
```

Expected output:
```json
{"status": "healthy", "model_loaded": true}
```

### Test ngrok Tunnel

```bash
# Replace with your ngrok URL
curl https://your-ngrok-url.ngrok-free.app/health
```

Should return same JSON.

### Test Streamlit App

Visit your Streamlit Cloud URL and start an interview!

---

## 🔄 Daily Usage Commands

Every time you want to use your deployed app:

### Terminal 1: Start SLM
```bash
cd /path/to/your/project
python slm_server.py
```

### Terminal 2: Start ngrok
```bash
ngrok http 5000
```

### If ngrok URL changed:
1. Copy new URL from ngrok terminal
2. Update Streamlit Cloud secrets
3. App will auto-restart

---

## 🛑 Stop Everything

### Stop SLM Server
Press `Ctrl+C` in Terminal 1

### Stop ngrok
Press `Ctrl+C` in Terminal 2

---

## 📱 Share Your App

Your Streamlit Cloud URL will be something like:
```
https://your-username-interview-assistant-chatbot-streamlit-app-xxxxx.streamlit.app
```

Share this URL with anyone! They can use your interview chatbot from anywhere.

---

## 🔧 Update Your Code

When you make changes:

```bash
# Commit changes
git add .
git commit -m "Update: description of changes"

# Push to GitHub
git push

# Streamlit Cloud will auto-deploy the update!
```

---

## 💡 Quick Tips

### Keep Mac Awake
```bash
caffeinate -d
```

### View ngrok Traffic
Visit: http://localhost:4040

### Check Streamlit Logs
In Streamlit Cloud, click "Manage app" → "Logs"

### Restart Streamlit App
In Streamlit Cloud, click "Manage app" → "Reboot app"

---

## 🎯 One-Command Deployment (Advanced)

If you want to automate everything:

```bash
./deploy.sh
```

This script will:
1. ✅ Initialize git
2. ✅ Commit your code
3. ✅ Push to GitHub
4. ✅ Guide you through Streamlit Cloud setup
5. ✅ Provide ngrok instructions

---

## 📊 Architecture Summary

```
┌─────────────────────────────────────────┐
│   Users (Anywhere in the World)        │
└────────────────┬────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────┐
│   Streamlit Cloud (Web Interface)      │
│   https://your-app.streamlit.app       │
└────────────┬────────────────────────────┘
             │
             ├──→ Gemini API (Questions & Analysis)
             │
             └──→ ngrok Tunnel
                  │
                  ↓
         ┌────────────────────────┐
         │   Your MacBook Air M4  │
         │   - Flask API Server   │
         │   - Phi-3 SLM Model    │
         └────────────────────────┘
```

---

## 🎉 You're Done!

Your interview chatbot is now:
- ✅ Deployed to the cloud
- ✅ Accessible from anywhere
- ✅ Using your local SLM for smart triage
- ✅ Ready to share with the world!

**Enjoy your deployed app!** 🚀
