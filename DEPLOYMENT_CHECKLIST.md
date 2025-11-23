# 🚀 Deployment Checklist

## ✅ Pre-Deployment

### Local Testing
- [ ] `.env` file created with `GOOGLE_API_KEY`
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] SLM model file present (or Gemini-only mode configured)
- [ ] Test locally: `streamlit run streamlit_app.py`
- [ ] Test all features: theme, font size, typewriter effect
- [ ] Test interview flow: start, answer, view analysis, quit
- [ ] Test rate limit handling (if possible)

### Code Preparation
- [ ] All files committed to git
- [ ] `.gitignore` properly configured
- [ ] No sensitive data in code
- [ ] Model file excluded from git (too large)

---

## 🌐 Streamlit Cloud Deployment

### Repository Setup
- [ ] Code pushed to GitHub
- [ ] Repository is public or you have Streamlit Cloud access
- [ ] `.env` file NOT in repository
- [ ] Model file NOT in repository (use Gemini-only mode)

### Streamlit Cloud Configuration
1. [ ] Go to [share.streamlit.io](https://share.streamlit.io)
2. [ ] Sign in with GitHub
3. [ ] Click "New app"
4. [ ] Select your repository
5. [ ] Set main file: `streamlit_app.py`
6. [ ] Configure secrets:
   ```toml
   GOOGLE_API_KEY = "your_key_here"
   STREAMLIT_CLOUD = "true"
   ```
7. [ ] Click "Deploy"

### Post-Deployment Testing
- [ ] App loads without errors
- [ ] Can start interview
- [ ] Questions generate properly
- [ ] Analysis dropdowns work
- [ ] Theme customization works
- [ ] Mobile responsive (test on phone)
- [ ] Rate limit handling works

---

## 🔧 Configuration Options

### For Local Development (Full Features)
```python
# In kiro7.py - keep SLM loading as-is
# Ensure model file is present
```

### For Cloud Deployment (Gemini-Only)
```python
# In kiro7.py - modify __init__:
IS_CLOUD = os.getenv("STREAMLIT_CLOUD", "false").lower() == "true"
if IS_CLOUD:
    self.slm_model = None
else:
    # existing SLM loading code
```

---

## 📱 Mobile Optimization

- [ ] Test on iOS Safari
- [ ] Test on Android Chrome
- [ ] Check landscape orientation
- [ ] Verify touch interactions
- [ ] Test analysis dropdowns on mobile

---

## 🎨 UI Customization

### Before Deployment, Consider:
- [ ] Adjust default theme color
- [ ] Modify gradient colors in CSS
- [ ] Change default font sizes
- [ ] Adjust typewriter speed defaults
- [ ] Customize welcome message

### CSS Locations in `streamlit_app.py`:
- Line ~30: Main gradient colors
- Line ~50: Chat message styling
- Line ~100: Button styling
- Line ~120: Animation speeds

---

## 🐛 Common Issues & Solutions

### Issue: App won't start
- **Check**: Python version (3.8+)
- **Check**: All dependencies installed
- **Check**: `.env` file exists (local)
- **Check**: Secrets configured (cloud)

### Issue: SLM not loading
- **Solution**: Use Gemini-only mode for cloud
- **Local**: Verify model file path

### Issue: Rate limit errors
- **Solution**: Already handled gracefully
- **Check**: API key is valid
- **Consider**: API quota limits

### Issue: Slow performance
- **Cloud**: Expected with API calls
- **Local**: Check SLM model size
- **Solution**: Adjust typewriter speed

---

## 📊 Performance Monitoring

After deployment, monitor:
- [ ] Response times
- [ ] Error rates
- [ ] User engagement
- [ ] API usage/costs
- [ ] Memory usage (cloud)

---

## 🔒 Security Checklist

- [ ] API keys in secrets (not code)
- [ ] `.env` in `.gitignore`
- [ ] No hardcoded credentials
- [ ] HTTPS enabled (automatic on Streamlit Cloud)
- [ ] Input validation working
- [ ] Error messages don't leak sensitive info

---

## 🎯 Launch Checklist

### Final Steps Before Going Live
1. [ ] All tests passing
2. [ ] Documentation complete
3. [ ] Secrets configured
4. [ ] Error handling tested
5. [ ] Mobile tested
6. [ ] Share link ready
7. [ ] Monitoring setup

### Share Your App
- [ ] Get Streamlit Cloud URL
- [ ] Test the public URL
- [ ] Share with users
- [ ] Gather feedback

---

## 📈 Post-Launch

### Week 1
- [ ] Monitor for errors
- [ ] Check user feedback
- [ ] Verify API costs
- [ ] Test under load

### Ongoing
- [ ] Update dependencies
- [ ] Improve based on feedback
- [ ] Add new features
- [ ] Optimize performance

---

## 🎉 You're Ready!

Once all items are checked, your Interview Assistant Chatbot is ready for deployment!

**Quick Deploy Command:**
```bash
# Local test
streamlit run streamlit_app.py

# Or use the helper scripts
./run_app.sh        # Mac/Linux
run_app.bat         # Windows
```

**Cloud Deploy:**
Visit [share.streamlit.io](https://share.streamlit.io) and follow the steps above.

Good luck! 🚀
