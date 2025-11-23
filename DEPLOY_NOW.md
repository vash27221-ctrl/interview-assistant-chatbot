# 🚀 Deploy NOW - Simple Steps

## ✅ ngrok is installed!

Now follow these steps to deploy:

---

## 📦 Step 1: Push to GitHub (5 minutes)

### 1.1 Create GitHub Repository

1. Go to: **https://github.com/new**
2. Repository name: `interview-assistant-chatbot`
3. Keep it **PUBLIC** ✅
4. **DO NOT** check "Initialize with README"
5. Click **"Create repository"**

### 1.2 Push Your Code

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Interview Assistant Chatbot"

# Add remote (REPLACE YOUR_USERNAME!)
git remote add origin https://github.com/YOUR_USERNAME/interview-assistant-chatbot.git

# Push
git branch -M main
git push -u origin main
```

**Done!** ✅ Your code is now on GitHub.

---

## 🌐 Step 2: Deploy to Streamlit Cloud (3 minutes)

### 2.1 Go to Streamlit Cloud

Visit: **https://share.streamlit.io**

### 2.2 Sign In

Click "Sign in with GitHub"

### 2.3 Create New App

1. Click **"New app"**
2. Select:
   - **Repository**: `YOUR_USERNAME/interview-assistant-chatbot`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`

### 2.4 Add Secrets

Click **"Advanced settings"** → **"Secrets"**

Paste this (replace with YOUR Gemini API key):

```toml
GOOGLE_API_KEY = "your_actual_gemini_api_key_here"
STREAMLIT_CLOUD = "true"
```

### 2.5 Deploy!

Click **"Deploy"**

Wait ~2-3 minutes for deployment.

**Done!** ✅ Your app is now live!

---

## 💻 Step 3: Connect Local SLM (Optional - 5 minutes)

### 3.1 Sign Up for ngrok

1. Go to: **https://ngrok.com**
2. Click **"Sign up"** (free)
3. After signing in, go to: **https://dashboard.ngrok.com/get-started/your-authtoken**
4. Copy your authtoken

### 3.2 Configure ngrok

```bash
# Paste your authtoken
ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE
```

### 3.3 Start SLM Server (Terminal 1)

```bash
cd /path/to/your/project
python slm_server.py
```

Wait for:
```
✅ SLM model loaded successfully
🚀 Server ready on port 5000
```

### 3.4 Start ngrok (Terminal 2)

Open a NEW terminal:

```bash
ngrok http 5000
```

Look for this line:
```
Forwarding    https://xxxx-xx-xx-xxx-xxx.ngrok-free.app -> http://localhost:5000
```

**Copy that URL!** (the https one)

### 3.5 Update Streamlit Secrets

1. Go back to: **https://share.streamlit.io**
2. Click your app → **⋮** menu → **"Settings"**
3. Go to **"Secrets"**
4. Update to include your ngrok URL:

```toml
GOOGLE_API_KEY = "your_gemini_key"
STREAMLIT_CLOUD = "true"
SLM_ENDPOINT = "https://xxxx-xx-xx-xxx-xxx.ngrok-free.app"
```

5. Click **"Save"** (app will auto-restart)

**Done!** ✅ Your local SLM is now connected!

---

## ✅ Verification

### Test Your Deployed App

1. Go to your Streamlit Cloud URL
2. Enter an interview domain (e.g., "Python Programming")
3. Click "Start Interview"
4. Answer a question
5. Check if it works!

### Check SLM Connection (if you set it up)

In your SLM server terminal, you should see requests coming in.

---

## 🎉 You're Live!

Your app is now:
- ✅ Deployed to the cloud
- ✅ Accessible from anywhere
- ✅ Ready to share!

### Your App URL:
```
https://YOUR_USERNAME-interview-assistant-chatbot-streamlit-app-xxxxx.streamlit.app
```

**Share this URL with anyone!**

---

## 🔄 Daily Usage (if using local SLM)

Every time you want to use your app with local SLM:

### Terminal 1:
```bash
python slm_server.py
```

### Terminal 2:
```bash
ngrok http 5000
```

### If ngrok URL changed:
Update Streamlit Cloud secrets with new URL

---

## 🛑 Stop Everything

### Stop SLM Server:
Press `Ctrl+C` in Terminal 1

### Stop ngrok:
Press `Ctrl+C` in Terminal 2

---

## 💡 Pro Tips

### Keep Mac Awake
```bash
caffeinate -d
```

### View ngrok Traffic
Visit: **http://localhost:4040**

### Check Streamlit Logs
In Streamlit Cloud: **Manage app** → **Logs**

---

## 🐛 Troubleshooting

### "Git push failed"
```bash
# Authenticate with GitHub
gh auth login
```

### "Can't reach SLM"
- Check if `slm_server.py` is running
- Check if ngrok is running
- Verify ngrok URL in Streamlit secrets
- Restart Streamlit app

### "Rate limit error"
- This is handled gracefully
- Wait a few minutes
- Try again

---

## 🎯 Summary

You just deployed:
- ✅ Beautiful web interface
- ✅ AI-powered interview system
- ✅ Adaptive difficulty
- ✅ Mobile responsive
- ✅ Publicly accessible

**Congratulations!** 🎊

---

## 📞 Need Help?

- **Quick Start**: `QUICKSTART.md`
- **Full Guide**: `GITHUB_DEPLOY.md`
- **ngrok Help**: `NGROK_SETUP.md`
- **All Commands**: `DEPLOY_COMMANDS.md`

---

**Ready to share your app with the world?** 🚀
