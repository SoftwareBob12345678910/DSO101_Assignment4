# Complete Setup Guide for DSO101 Assignment 4

## 🎯 What You Need to Do (5 Steps)

### **STEP 1: Prepare Your Local Environment** ⏱️ 5 minutes

#### 1.1 Install Python and Git
- Ensure Python 3.9+ is installed: `python --version`
- Ensure Git is installed: `git --version`

#### 1.2 Set up Virtual Environment (Recommended)
```bash
# Navigate to your project folder
cd DSO101_Assignment4

# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 1.3 Install Dependencies
```bash
pip install -r requirements.txt
```

**What gets installed:**
- Flask (web framework)
- pytest (testing framework)
- gunicorn (production server)

---

### **STEP 2: Test the Application Locally** ⏱️ 10 minutes

#### 2.1 Run the Flask App
```bash
python app.py
```

**Expected output:**
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

#### 2.2 Test in Another Terminal (While app is running)
```bash
# Test home endpoint
curl http://localhost:5000/

# Test health check
curl http://localhost:5000/api/health

# Test creating a task (POST)
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Complete Assignment","description":"CI/CD Implementation"}'

# Test math API
curl -X POST http://localhost:5000/api/add \
  -H "Content-Type: application/json" \
  -d '{"a":100,"b":50}'
```

#### 2.3 Stop the App
```bash
# Press CTRL+C to stop the Flask app
```

---

### **STEP 3: Run Unit Tests** ⏱️ 10 minutes

#### 3.1 Run All Tests
```bash
pytest test_app.py -v
```

**Expected output:** ✅ All tests should PASS

```
test_app.py::TestHomeEndpoint::test_home_returns_200 PASSED
test_app.py::TestHomeEndpoint::test_home_returns_correct_message PASSED
test_app.py::TestHealthCheck::test_health_check_returns_200 PASSED
test_app.py::TestTaskOperations::test_create_task_success PASSED
...
======================== 15+ passed in X.XXs ========================
```

**📸 SCREENSHOT 1:** Capture this output for your submission

#### 3.2 Run Tests with Coverage Report
```bash
pytest test_app.py -v --cov=. --cov-report=html
```

This generates coverage statistics showing how much of your code is tested.

---

### **STEP 4: Push Code to GitHub** ⏱️ 15 minutes

#### 4.1 Set Up Git Repository
```bash
# Initialize (if not already done)
git init

# Configure Git (one time only)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Flask app with CI/CD pipeline and tests"
```

#### 4.2 Connect to GitHub and Push
```bash
# Visit https://github.com/new and create a new repository
# Name it: DSO101_Assignment4
# DO NOT add README, .gitignore, or license

# Then run these commands (replace YOUR_USERNAME):
git remote add origin https://github.com/YOUR_USERNAME/DSO101_Assignment4.git
git branch -M main
git push -u origin main
```

**Verify on GitHub:**
1. Go to your repository URL
2. Check that all files are there (app.py, test_app.py, etc.)
3. Click **Actions** tab - you should see a workflow running!

**📸 SCREENSHOT 2:** Capture the GitHub Actions workflow running (wait for it to complete and show green checkmarks)

---

### **STEP 5: Deploy to Render** ⏱️ 20 minutes

#### 5.1 Create Render Account
1. Go to https://render.com
2. Click **Sign up**
3. Sign up with GitHub (recommended)
4. Verify your email

#### 5.2 Create a Web Service
1. Go to your Render dashboard
2. Click **New +** → **Web Service**
3. Click **Connect** next to your GitHub repository (DSO101_Assignment4)
4. Authorize GitHub if needed

#### 5.3 Configure the Service
Fill in these settings:
- **Name:** `dso101-cicd` (or any name you like)
- **Region:** Select closest to you
- **Branch:** `main`
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Instance Type:** `Free`

Click **Create Web Service**

⏳ **Wait 3-5 minutes for deployment to complete**

#### 5.4 Get Your Live URL
Once deployed, you'll see a URL like:
```
https://dso101-cicd.onrender.com
```

**📸 SCREENSHOT 3:** Capture the working API by visiting your URL in browser

Test it:
```bash
curl https://your-url.onrender.com/api/health
```

---

### **STEP 6: Enable Auto-Deployment (Optional but Recommended)** ⏱️ 5 minutes

#### 6.1 Get Deploy Hook from Render
1. Go to your Render service dashboard
2. Click **Settings**
3. Find **Deploy Hook** section
4. Copy the URL (it looks like: `https://api.render.com/deploy/...`)

#### 6.2 Add Secret to GitHub
1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `RENDER_DEPLOY_HOOK_URL`
5. Value: Paste the deploy hook URL
6. Click **Add secret**

#### 6.3 Test Auto-Deploy
1. Make a small change to `app.py` (e.g., change the welcome message)
2. Commit and push:
```bash
git add app.py
git commit -m "Update welcome message to test auto-deploy"
git push
```

3. Watch the GitHub Actions workflow run
4. After it completes, check if your Render app updated

---

## 📋 Final Checklist Before Submission

- [ ] **Local tests pass:** `pytest test_app.py -v` shows all tests PASSED
- [ ] **GitHub repository created:** Public repository with all files
- [ ] **GitHub Actions workflow passes:** Green checkmarks on all jobs
- [ ] **Render deployment successful:** App is live and working
- [ ] **API endpoints working:** Test `/api/health` on your live URL
- [ ] **Documentation complete:** INSTRUCTIONS.md and README.md filled out
- [ ] **Screenshots captured:**
  - [ ] Local tests passing
  - [ ] GitHub Actions workflow success
  - [ ] Live app working on Render

---

## 📸 Required Screenshots for Submission

### Screenshot 1: Local Tests
```bash
pytest test_app.py -v
```
Show the terminal output with all tests PASSED

### Screenshot 2: GitHub Actions
Go to Actions tab → Click the latest workflow → Show the completed run with green checkmarks

### Screenshot 3: Live App
Visit `https://your-app-url.onrender.com/` and capture the JSON response

---

## 🔗 URLs to Submit

1. **GitHub Repository:** `https://github.com/YOUR_USERNAME/DSO101_Assignment4`
2. **Live Application:** `https://your-app-name.onrender.com`

---

## 🆘 Common Issues & Solutions

### Problem: Tests fail locally
**Solution:**
```bash
pip install -r requirements.txt --force-reinstall
pytest test_app.py -v --tb=short
```

### Problem: GitHub Actions workflow fails
**Solution:**
1. Go to Actions tab
2. Click the failed workflow
3. Check the error message in the "Run tests" step
4. Ensure all requirements are installed correctly

### Problem: App won't deploy to Render
**Solution:**
1. Check Render logs (Dashboard → Logs)
2. Verify "Build Command" is: `pip install -r requirements.txt`
3. Verify "Start Command" is: `gunicorn app:app`
4. Ensure Python version is compatible

### Problem: Auto-deploy isn't triggering
**Solution:**
1. Verify `RENDER_DEPLOY_HOOK_URL` secret exists in GitHub Settings
2. Check GitHub Actions workflow file has correct secret name
3. Make sure you're pushing to the `main` branch (not `master`)

---

## ✅ How to Verify Everything Works

### Test 1: Local Development
```bash
# Run app
python app.py

# In another terminal:
curl http://localhost:5000/

# Should return:
# {"message":"Welcome to the CI/CD Pipeline API","status":"success","version":"1.0.0"}
```

### Test 2: Tests
```bash
pytest test_app.py -v

# Should show:
# ======================== 15+ passed in X.XXs ========================
```

### Test 3: GitHub Workflow
1. Go to GitHub repo → Actions tab
2. Should see "CI/CD Pipeline" workflow
3. Should show: ✅ build-test (passed), ✅ deploy (completed)

### Test 4: Live App
```bash
curl https://your-app-name.onrender.com/api/health

# Should return:
# {"status":"healthy","service":"CI/CD Pipeline API"}
```

---

## 📊 Project Files Explained

| File | Purpose | Lines |
|------|---------|-------|
| `app.py` | Flask REST API with 6+ endpoints | ~100 |
| `test_app.py` | Pytest unit tests (30+ tests) | ~200 |
| `requirements.txt` | Python dependencies | 5 |
| `.github/workflows/ci.yml` | GitHub Actions workflow | ~80 |
| `README.md` | Project documentation | ~200 |
| `INSTRUCTIONS.md` | Detailed guides | ~300 |
| `runtime.txt` | Python version for Render | 1 |
| `.gitignore` | Git ignore rules | ~40 |

**Total:** ~850 lines of code and documentation

---

## 🎓 What You'll Learn

By completing this assignment, you'll understand:
- ✅ How to build a REST API
- ✅ How to write unit tests
- ✅ How CI/CD pipelines work
- ✅ How to automate testing
- ✅ How to deploy to cloud
- ✅ How to use GitHub Actions
- ✅ How to use Render for hosting

---

## 📞 Quick Reference Commands

```bash
# Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Local testing
python app.py
pytest test_app.py -v

# Git commands
git add .
git commit -m "message"
git push

# Render deployment
# Login at render.com and create web service
```

---

## 🚀 You're Ready!

Follow these steps in order and you'll have a complete CI/CD pipeline deployed!

**Good luck! 🎉**
