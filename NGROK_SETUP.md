# 🔗 ngrok Setup Guide for Local SLM

## 📋 What is ngrok?

ngrok creates a secure tunnel from a public URL to your local MacBook, allowing Streamlit Cloud to access your local SLM model.

```
Internet → ngrok URL → Your MacBook → SLM Model
```

---

## 🚀 Quick Setup (5 minutes)

### Step 1: Install ngrok

```bash
# Using Homebrew (recommended for Mac)
brew install ngrok

# Or download from https://ngrok.com/download
```

### Step 2: Sign Up (Free)

1. Go to [ngrok.com](https://ngrok.com)
2. Click "Sign up" (free account)
3. After signing in, go to "Your Authtoken"
4. Copy your authtoken

### Step 3: Configure ngrok

```bash
# Add your authtoken (one-time setup)
ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE
```

---

## 💻 Running Your Setup

### Terminal 1: Start SLM Server

```bash
cd /path/to/your/project
python slm_server.py
```

You should see:
```
🎯 Interview Assistant SLM API Server
============================================================
🔄 Loading SLM model from: Phi3_Interview_Merged-3.8B-F16.gguf
⏳ This may take a moment...
✅ SLM model loaded successfully in 8.45 seconds
🚀 Server ready on port 5000
============================================================
📡 Starting Flask server...
🌐 Local URL: http://localhost:5000
```

### Terminal 2: Start ngrok Tunnel

```bash
ngrok http 5000
```

You should see:
```
ngrok                                                                    

Session Status                online
Account                       Your Name (Plan: Free)
Version                       3.x.x
Region                        United States (us)
Latency                       -
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://xxxx-xx-xx-xxx-xxx.ngrok-free.app -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

### Step 4: Copy Your ngrok URL

Look for the line that says:
```
Forwarding    https://xxxx-xx-xx-xxx-xxx.ngrok-free.app -> http://localhost:5000
```

Copy this URL: `https://xxxx-xx-xx-xxx-xxx.ngrok-free.app`

---

## 🌐 Update Streamlit Cloud

### Step 1: Go to Your App Settings

1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Click on your app
3. Click the menu (⋮) → "Settings"
4. Go to "Secrets"

### Step 2: Add ngrok URL

Add or update this line in your secrets:

```toml
GOOGLE_API_KEY = "your_gemini_key"
STREAMLIT_CLOUD = "true"
SLM_ENDPOINT = "https://xxxx-xx-xx-xxx-xxx.ngrok-free.app"
```

**Important:** Replace with YOUR actual ngrok URL!

### Step 3: Restart App

Click "Reboot app" or just save the secrets (auto-restarts)

---

## ✅ Test Your Setup

### Test 1: Check SLM Server

```bash
curl http://localhost:5000/health
```

Should return:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_path": "Phi3_Interview_Merged-3.8B-F16.gguf"
}
```

### Test 2: Check ngrok Tunnel

```bash
curl https://your-ngrok-url.ngrok-free.app/health
```

Should return the same JSON.

### Test 3: Use Your Streamlit App

1. Go to your Streamlit Cloud URL
2. Start an interview
3. Check the logs - you should see SLM being used

---

## 🔄 Daily Usage

Every time you want to use your app:

1. **Start SLM Server** (Terminal 1):
   ```bash
   python slm_server.py
   ```

2. **Start ngrok** (Terminal 2):
   ```bash
   ngrok http 5000
   ```

3. **If ngrok URL changed**, update Streamlit secrets

4. **Use your app!**

---

## 💡 Pro Tips

### Keep Your Mac Awake

```bash
# Prevent sleep while servers are running
caffeinate -d
```

### Use a Static ngrok URL (Paid)

Free ngrok URLs change every time you restart. For $8/month, get a static URL:

1. Upgrade at [ngrok.com/pricing](https://ngrok.com/pricing)
2. Reserve a domain
3. Use: `ngrok http --domain=your-static-domain.ngrok-free.app 5000`
4. Set once in Streamlit secrets, never change again!

### Monitor ngrok Traffic

Visit `http://localhost:4040` while ngrok is running to see:
- All requests
- Response times
- Errors
- Request/response details

### Run in Background

```bash
# Start SLM server in background
nohup python slm_server.py > slm_server.log 2>&1 &

# Start ngrok in background
nohup ngrok http 5000 > ngrok.log 2>&1 &

# View logs
tail -f slm_server.log
tail -f ngrok.log
```

---

## 🐛 Troubleshooting

### Issue: "command not found: ngrok"

**Solution:**
```bash
brew install ngrok
# Or download from https://ngrok.com/download
```

### Issue: "ERR_NGROK_108"

**Solution:** You need to add your authtoken:
```bash
ngrok config add-authtoken YOUR_TOKEN
```

### Issue: ngrok URL changes every restart

**Solution:** This is normal for free accounts. Either:
- Update Streamlit secrets each time
- Upgrade to ngrok paid plan for static URL

### Issue: Streamlit can't reach SLM

**Checklist:**
- ✅ Is `slm_server.py` running?
- ✅ Is ngrok running?
- ✅ Is the ngrok URL correct in Streamlit secrets?
- ✅ Did you restart the Streamlit app after updating secrets?

### Issue: "Model not loaded" error

**Solution:** Check `slm_server.py` terminal for errors. The model file must be in the same directory.

### Issue: Slow responses

**Solution:** This is normal with internet round-trip. Expect +500ms-1s latency compared to local.

---

## 📊 Performance Comparison

### Local SLM (No ngrok)
- **Latency**: ~100-200ms
- **Quality**: Best
- **Setup**: Simple
- **Access**: Local only

### Remote SLM (via ngrok)
- **Latency**: ~600-1000ms
- **Quality**: Same as local
- **Setup**: Requires ngrok
- **Access**: Public (Streamlit Cloud)

### Gemini-Only (No SLM)
- **Latency**: ~500-800ms
- **Quality**: Excellent (different approach)
- **Setup**: Simplest
- **Access**: Public

---

## 🔒 Security Notes

### What's Safe:
✅ ngrok uses HTTPS encryption
✅ Your SLM stays on your Mac
✅ No data stored by ngrok
✅ You control when it's accessible

### Best Practices:
- Don't share your ngrok URL publicly
- Stop ngrok when not in use
- Monitor traffic at http://localhost:4040
- Use ngrok's IP restrictions (paid feature)

---

## 💰 Cost Breakdown

### Free Setup:
- ngrok Free: $0/month
  - Random URLs (change on restart)
  - 1 online ngrok process
  - 40 connections/minute
  
- Streamlit Cloud: $0/month
  - Public apps
  - Unlimited viewers
  - Community support

**Total: $0/month** ✅

### Paid Setup (Optional):
- ngrok Personal: $8/month
  - Static domain
  - 3 online processes
  - 120 connections/minute
  
- Streamlit Cloud: $0/month (same)

**Total: $8/month**

---

## 🎯 Quick Reference

### Start Everything:
```bash
# Terminal 1
python slm_server.py

# Terminal 2
ngrok http 5000

# Copy ngrok URL and update Streamlit secrets if changed
```

### Stop Everything:
```bash
# Press Ctrl+C in both terminals
```

### Check Status:
```bash
# SLM Server
curl http://localhost:5000/health

# ngrok Tunnel
curl https://your-url.ngrok-free.app/health

# ngrok Dashboard
open http://localhost:4040
```

---

## 🎉 You're All Set!

Your local SLM is now accessible from anywhere via ngrok!

**Questions?** Check the troubleshooting section or see `GITHUB_DEPLOY.md` for more details.

**Ready to deploy?** Run `./deploy.sh` to push everything to GitHub and Streamlit Cloud!
