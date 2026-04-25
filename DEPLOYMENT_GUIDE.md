# Heroku Deployment Guide

This guide will walk you through deploying your TB-AI Predictive Model to Heroku in just a few steps.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Step 1: Prepare Your Application](#step-1-prepare-your-application)
- [Step 2: Create Heroku Account](#step-2-create-heroku-account)
- [Step 3: Install Heroku CLI](#step-3-install-heroku-cli)
- [Step 4: Configure Application](#step-4-configure-application)
- [Step 5: Deploy to Heroku](#step-5-deploy-to-heroku)
- [Step 6: Test Live Application](#step-6-test-live-application)
- [Step 7: Monitor & Troubleshoot](#step-7-monitor--troubleshoot)
- [Additional Resources](#additional-resources)

---

## Prerequisites

Before starting, ensure you have:
- ✅ Git installed and configured
- ✅ GitHub account with your repo pushed
- ✅ Python 3.11+ installed locally
- ✅ A Heroku account (free tier available)
- ✅ Your app files: `app.py`, `requirements.txt`, `Procfile`

---

## Step 1: Prepare Your Application

### 1.1 Verify Required Files

Your repository must contain:

```
✅ app.py                    (main Flask application)
✅ requirements.txt          (Python dependencies)
✅ Procfile                  (Heroku process definition)
✅ .gitignore               (prevent tracking unwanted files)
✅ .env.example             (configuration template)
✅ runtime.txt              (optional: Python version)
```

### 1.2 Create `runtime.txt` (Optional but Recommended)

```bash
touch runtime.txt
```

Add your Python version:

```
python-3.11.8
```

Check available versions at: https://devcenter.heroku.com/articles/python-support

### 1.3 Update `Procfile`

Verify your `Procfile` exists and contains:

```
web: gunicorn app:app
```

**Note**: The `app:app` format means:
- First `app` = Python module (app.py)
- Second `app` = Flask application instance inside app.py

### 1.4 Verify `requirements.txt`

Your `requirements.txt` should include Flask and Gunicorn:

```bash
pip list | grep -E "(Flask|gunicorn)"
```

If Gunicorn is missing, add it:

```bash
pip install gunicorn
pip freeze > requirements.txt
```

### 1.5 Push to GitHub

Ensure all changes are committed and pushed:

```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push origin main
```

---

## Step 2: Create Heroku Account

### 2.1 Sign Up

1. Visit https://www.heroku.com/
2. Click **"Sign up"**
3. Fill in your details:
   - Email
   - First name
   - Last name
   - Company (optional)
   - Role (Developer)
   - Language (Node.js or Python - choose Python)
4. Click **"Create Free Account"**
5. Check your email and verify your account

### 2.2 Heroku Dashboard

After verification:
1. Log in to https://dashboard.heroku.com/
2. You should see the dashboard with option to create a new app

---

## Step 3: Install Heroku CLI

### 3.1 Installation

**macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**Windows:**
Download from: https://cli-assets.heroku.com/branches/stable/heroku-windows-x64.exe
Then run the installer.

**Linux (Ubuntu/Debian):**
```bash
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

### 3.2 Verify Installation

```bash
heroku --version
```

Expected output:
```
heroku/7.x.x (linux-x64) node-vx.x.x
```

### 3.3 Login to Heroku

```bash
heroku login
```

This will:
1. Open your browser
2. Ask you to click "Log in"
3. Return to terminal (you're now authenticated)

Verify login:
```bash
heroku auth:whoami
```

---

## Step 4: Configure Application

### 4.1 Create Heroku App

**Option A: Via CLI (Recommended)**
```bash
heroku create your-app-name
```

Replace `your-app-name` with something unique (e.g., `tb-ai-model-123`)

**Note**: App name must be:
- Unique across all Heroku
- Lowercase with hyphens only
- 3-30 characters

**Option B: Via Dashboard**
1. Go to https://dashboard.heroku.com/
2. Click "New" → "Create new app"
3. Enter app name
4. Choose region (closest to you)
5. Click "Create app"

### 4.2 Add Heroku as Remote

If using dashboard to create:
```bash
heroku git:remote -a your-app-name
```

Verify:
```bash
git remote -v
```

Expected output:
```
heroku  https://git.heroku.com/your-app-name.git (fetch)
heroku  https://git.heroku.com/your-app-name.git (push)
```

### 4.3 Set Environment Variables

Set required configuration variables:

```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key-change-this
heroku config:set FLASK_DEBUG=False
```

View all config:
```bash
heroku config
```

### 4.4 Add Add-ons (Optional)

**PostgreSQL Database** (if needed):
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

**Redis** (for caching):
```bash
heroku addons:create heroku-redis:premium-0
```

---

## Step 5: Deploy to Heroku

### 5.1 Deploy via Git Push

```bash
git push heroku main
```

**Note**: If your default branch is different (e.g., `master`):
```bash
git push heroku master:main
```

### 5.2 Monitor Deployment

Watch the output for:
- ✅ "Fetching source"
- ✅ "Building application"
- ✅ "Installing dependencies"
- ✅ "Running release phase"
- ✅ "Launching..."

Expected final output:
```
remote: Verifying deploy... done.
To https://git.heroku.com/your-app-name.git
   abc1234..xyz9876  main -> main
```

### 5.3 Check Deployment Status

```bash
heroku logs --tail
```

This shows real-time logs. Press `Ctrl+C` to exit.

---

## Step 6: Test Live Application

### 6.1 Get App URL

```bash
heroku apps:info your-app-name
```

Or find it in the dashboard.

URL format: `https://your-app-name.herokuapp.com`

### 6.2 Test Home Page

```bash
curl https://your-app-name.herokuapp.com
```

Expected: HTML content from your home page

### 6.3 Test API Endpoints

**Get County Data:**
```bash
curl https://your-app-name.herokuapp.com/county-data
```

**Make Prediction:**
```bash
curl -X POST https://your-app-name.herokuapp.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "latitude": -1.2921,
    "longitude": 36.8219,
    "feature1": 10,
    "feature2": 20
  }'
```

**Get County Stats:**
```bash
curl https://your-app-name.herokuapp.com/county-stats/Nairobi
```

### 6.4 Open in Browser

```bash
heroku open
```

Or visit: `https://your-app-name.herokuapp.com`

---

## Step 7: Monitor & Troubleshoot

### 7.1 View Logs

**Real-time logs:**
```bash
heroku logs --tail
```

**Last 50 lines:**
```bash
heroku logs -n 50
```

**Filter by process type:**
```bash
heroku logs --source web
heroku logs --source heroku
```

### 7.2 Common Issues & Solutions

#### Issue: Application Error (Error H14)

```
Application Error
```

**Solution:**
1. Check logs: `heroku logs --tail`
2. Verify `Procfile`: Must be exactly `web: gunicorn app:app`
3. Ensure app starts locally: `python app.py`
4. Check for syntax errors: `python -m py_compile app.py`

#### Issue: Module Not Found

```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
1. Update requirements: `pip freeze > requirements.txt`
2. Verify Gunicorn is included
3. Redeploy: `git push heroku main`

#### Issue: Port Configuration

**Error:** App starts but doesn't respond

**Solution:** Update app.py:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

#### Issue: Static Files Not Loading

**Solution:** Add in app.py:
```python
from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='/static')
```

#### Issue: Timeout (H12)

```
Error H12: Request timeout
```

**Solution:**
- Optimize database queries
- Add caching
- Increase dyno size: `heroku dyos:resize standard-1x`

### 7.3 Restart Application

```bash
heroku restart
```

### 7.4 Scale Dynos

View current dyno configuration:
```bash
heroku ps
```

Increase web dynos (costs money):
```bash
heroku ps:scale web=2
```

---

## Step 8: Advanced Configuration

### 8.1 Custom Domain

```bash
heroku domains:add www.yourdomain.com
```

Then update DNS records at your registrar.

### 8.2 SSL/TLS Certificate

Heroku provides free SSL by default. Verify:
```bash
heroku certs:info
```

### 8.3 Scheduled Tasks (if needed)

Add scheduler add-on:
```bash
heroku addons:create scheduler:standard
```

### 8.4 Environment-Specific Settings

Production settings:
```bash
heroku config:set FLASK_ENV=production
heroku config:set DEBUG=False
```

### 8.5 Database Migration (if using DB)

```bash
heroku run python manage.py migrate
```

---

## Step 9: Continuous Deployment

### 9.1 Connect GitHub

1. Go to your Heroku app dashboard
2. Click "Deploy" tab
3. Under "Deployment method" select "GitHub"
4. Click "Connect to GitHub"
5. Search for your repository
6. Click "Connect"

### 9.2 Enable Auto Deploy

1. Under "Automatic deploys"
2. Select branch (main)
3. Check "Wait for CI to pass before deploy"
4. Click "Enable Automatic Deploys"

Now, every push to `main` will auto-deploy!

---

## Step 10: Local Development with Heroku

### 10.1 Use Heroku Local

```bash
# Install Heroku Toolbelt (already done if you have CLI)

# Create Procfile.local
echo "web: python app.py" > Procfile.local

# Run locally with Heroku environment
heroku local web -f Procfile.local
```

### 10.2 Test Environment Variables Locally

```bash
# Create .env file
cp .env.example .env

# Edit .env with your values
nano .env

# Run with heroku local
heroku local
```

---

## Summary Checklist

- ✅ Created `Procfile` with `web: gunicorn app:app`
- ✅ Created `runtime.txt` with Python version
- ✅ Added Gunicorn to `requirements.txt`
- ✅ Verified app runs locally: `python app.py`
- ✅ Pushed code to GitHub
- ✅ Created Heroku account
- ✅ Installed Heroku CLI
- ✅ Logged in: `heroku login`
- ✅ Created app: `heroku create your-app-name`
- ✅ Set environment variables: `heroku config:set ...`
- ✅ Deployed: `git push heroku main`
- ✅ Tested endpoints: `curl https://your-app-name.herokuapp.com`
- ✅ View logs: `heroku logs --tail`

---

## Deployment Complete! 🎉

Your TB-AI Predictive Model is now live on:
```
https://your-app-name.herokuapp.com
```

### Share Your Live App

- **Share URL**: `https://your-app-name.herokuapp.com`
- **API Base URL**: `https://your-app-name.herokuapp.com/api`
- **Documentation**: Link to README.md on GitHub

### Next Steps

1. ✅ Monitor app health: `heroku logs --tail`
2. ✅ Set up custom domain (optional)
3. ✅ Enable GitHub auto-deploy (optional)
4. ✅ Set up monitoring alerts (optional)
5. ✅ Gather user feedback

---

## Useful Commands Reference

```bash
# App Management
heroku create your-app-name          # Create app
heroku apps:list                     # List all apps
heroku apps:info your-app-name       # Get app info
heroku open                          # Open app in browser
heroku rename new-name               # Rename app

# Deployment
git push heroku main                 # Deploy
git push heroku feature:main         # Deploy specific branch
heroku releases                      # View deployment history
heroku rollback                      # Revert to previous version

# Configuration
heroku config                        # View all config vars
heroku config:set KEY=VALUE          # Set config var
heroku config:unset KEY              # Remove config var

# Logs & Monitoring
heroku logs --tail                   # Real-time logs
heroku logs -n 100                   # Last 100 lines
heroku logs --source web             # Web process logs
heroku logs --source heroku          # Heroku system logs

# Dynos
heroku ps                            # View running processes
heroku ps:scale web=2                # Scale web dynos
heroku restart                       # Restart app
heroku restart web                   # Restart web dyno

# Troubleshooting
heroku run bash                      # SSH into dyno
heroku run python -c "import app"    # Run Python command
heroku labs:enable log-runtime-metrics  # Enable metrics
```

---

## Support & Resources

- **Heroku Docs**: https://devcenter.heroku.com/
- **Python Support**: https://devcenter.heroku.com/articles/python-support
- **Flask Deployment**: https://flask.palletsprojects.com/deployment/
- **Troubleshooting**: https://devcenter.heroku.com/articles/troubleshooting-heroku-logs
- **Community**: https://help.heroku.com/

---

**Last Updated**: April 2026
**Status**: Ready for Production
