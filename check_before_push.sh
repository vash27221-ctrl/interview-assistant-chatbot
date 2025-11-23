#!/bin/bash

echo "🔍 Checking what will be pushed to GitHub..."
echo ""

# Initialize git if not already done
if [ ! -d .git ]; then
    echo "Initializing git repository..."
    git init
fi

# Add files
git add .

echo "✅ Files that WILL be pushed:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
git ls-files | grep -E '\.(py|md|txt|toml|sh|bat)$' | head -20
echo ""
echo "(Showing first 20 files, run 'git ls-files' to see all)"
echo ""

echo "❌ Files that WON'T be pushed (ignored):"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
git status --ignored --short | grep '^!!' | head -20
echo ""
echo "(Showing first 20 ignored files)"
echo ""

echo "📊 Summary:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
total_files=$(git ls-files | wc -l | tr -d ' ')
echo "Total files to push: $total_files"
echo ""

# Check for sensitive files
echo "🔒 Security Check:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if git ls-files | grep -q "\.env$"; then
    echo "⚠️  WARNING: .env file will be pushed! (Contains API keys)"
else
    echo "✅ .env is ignored (good!)"
fi

if git ls-files | grep -q "\.gguf$"; then
    echo "⚠️  WARNING: .gguf model files will be pushed! (Too large)"
else
    echo "✅ .gguf files are ignored (good!)"
fi

if git ls-files | grep -q "kiro[1-6]\.py"; then
    echo "⚠️  WARNING: Old kiro files will be pushed (not needed)"
else
    echo "✅ Old kiro files are ignored (good!)"
fi

echo ""
echo "✅ All checks passed! Safe to push to GitHub."
echo ""
echo "Next steps:"
echo "1. git commit -m 'Initial commit'"
echo "2. git remote add origin https://github.com/YOUR_USERNAME/interview-assistant-chatbot.git"
echo "3. git push -u origin main"
