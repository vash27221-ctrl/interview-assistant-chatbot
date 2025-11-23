#!/bin/bash

echo "🚀 Interview Assistant Chatbot - Full Deployment Script"
echo "========================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Check prerequisites
echo "📋 Step 1: Checking prerequisites..."
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git is not installed. Please install git first.${NC}"
    exit 1
fi

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo -e "${YELLOW}⚠️  ngrok is not installed.${NC}"
    echo "   Install with: brew install ngrok"
    echo "   Or download from: https://ngrok.com/download"
    read -p "   Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo -e "${GREEN}✅ Prerequisites checked${NC}"
echo ""

# Step 2: Initialize git repository
echo "📦 Step 2: Initializing Git repository..."
echo ""

if [ ! -d .git ]; then
    git init
    echo -e "${GREEN}✅ Git repository initialized${NC}"
else
    echo -e "${YELLOW}ℹ️  Git repository already exists${NC}"
fi

# Step 3: Add files to git
echo ""
echo "📝 Step 3: Adding files to Git..."
echo ""

git add .
git status

echo ""
read -p "Does this look correct? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 1
fi

# Step 4: Commit
echo ""
echo "💾 Step 4: Creating commit..."
echo ""

git commit -m "Deploy: Interview Assistant Chatbot with SLM support"
echo -e "${GREEN}✅ Commit created${NC}"

# Step 5: Get GitHub username
echo ""
echo "🔗 Step 5: Setting up GitHub remote..."
echo ""

read -p "Enter your GitHub username: " github_username

if [ -z "$github_username" ]; then
    echo -e "${RED}❌ GitHub username is required${NC}"
    exit 1
fi

repo_name="interview-assistant-chatbot"
remote_url="https://github.com/$github_username/$repo_name.git"

# Check if remote already exists
if git remote | grep -q "origin"; then
    echo -e "${YELLOW}ℹ️  Remote 'origin' already exists${NC}"
    git remote set-url origin $remote_url
else
    git remote add origin $remote_url
fi

echo -e "${GREEN}✅ Remote configured: $remote_url${NC}"

# Step 6: Push to GitHub
echo ""
echo "⬆️  Step 6: Pushing to GitHub..."
echo ""
echo -e "${YELLOW}⚠️  Make sure you've created the repository on GitHub first!${NC}"
echo "   Go to: https://github.com/new"
echo "   Repository name: $repo_name"
echo "   Keep it PUBLIC (required for free Streamlit Cloud)"
echo ""
read -p "Have you created the repository? (y/n) " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Please create the repository first, then run this script again."
    exit 1
fi

git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Code pushed to GitHub successfully!${NC}"
else
    echo -e "${RED}❌ Failed to push to GitHub${NC}"
    echo "   You may need to authenticate with GitHub"
    echo "   Try: gh auth login"
    exit 1
fi

# Step 7: Instructions for Streamlit Cloud
echo ""
echo "=" * 60
echo "🌐 Step 7: Deploy to Streamlit Cloud"
echo "=" * 60
echo ""
echo "1. Go to: https://share.streamlit.io"
echo "2. Sign in with your GitHub account"
echo "3. Click 'New app'"
echo "4. Select:"
echo "   - Repository: $github_username/$repo_name"
echo "   - Branch: main"
echo "   - Main file: streamlit_app.py"
echo ""
echo "5. Click 'Advanced settings' and add these secrets:"
echo ""
echo "   GOOGLE_API_KEY = \"your_gemini_api_key_here\""
echo "   STREAMLIT_CLOUD = \"true\""
echo ""
echo "6. Click 'Deploy'"
echo ""
read -p "Press Enter when you've deployed to Streamlit Cloud..."

# Step 8: Instructions for ngrok
echo ""
echo "=" * 60
echo "🔗 Step 8: Set up ngrok for local SLM"
echo "=" * 60
echo ""
echo "Open a NEW terminal window and run these commands:"
echo ""
echo "Terminal 1 (SLM Server):"
echo "  cd $(pwd)"
echo "  python slm_server.py"
echo ""
echo "Terminal 2 (ngrok):"
echo "  ngrok http 5000"
echo ""
echo "Then:"
echo "1. Copy the ngrok URL (https://xxxx.ngrok-free.app)"
echo "2. Go to your Streamlit Cloud app settings"
echo "3. Add this secret:"
echo "   SLM_ENDPOINT = \"https://xxxx.ngrok-free.app\""
echo "4. Restart your Streamlit app"
echo ""

# Step 9: Summary
echo ""
echo "=" * 60
echo "🎉 Deployment Complete!"
echo "=" * 60
echo ""
echo "Your app is now deployed! Here's what you have:"
echo ""
echo "✅ Code on GitHub: https://github.com/$github_username/$repo_name"
echo "✅ Web interface on Streamlit Cloud"
echo "✅ Local SLM ready (run slm_server.py + ngrok)"
echo ""
echo "Next steps:"
echo "1. Start your SLM server: python slm_server.py"
echo "2. Start ngrok: ngrok http 5000"
echo "3. Update Streamlit secrets with ngrok URL"
echo "4. Share your Streamlit URL with the world!"
echo ""
echo "📚 For more details, see GITHUB_DEPLOY.md"
echo ""
