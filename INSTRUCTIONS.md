# DSO101 Assignment 4: CI/CD Pipeline Implementation

## 📋 Overview
This project implements a complete CI/CD pipeline with:
- Flask backend application
- Comprehensive unit tests using pytest
- GitHub Actions for automated CI/CD
- Auto-deployment to Render

---

## 📂 Project Structure
```
DSO101_Assignment4/
├── app.py                          # Flask application
├── test_app.py                     # Unit tests
├── requirements.txt                # Python dependencies
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions workflow
├── .gitignore                      # Git ignore file
├── INSTRUCTIONS.md                 # This file
└── README.md                       # Assignment description
```

---

## ✅ Step-by-Step Instructions

### **Phase 1: Local Setup & Testing**

#### Step 1: Install Python & Dependencies
```bash
# 1. Ensure Python 3.9+ is installed
python --version

# 2. Create a virtual environment (optional but recommended)
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
```

#### Step 2: Run the Flask Application Locally
```bash
# Start the Flask app
python app.py

# Output should show:
# * Running on http://127.0.0.1:5000
```

#### Step 3: Test the API Endpoints (in another terminal)
```bash
# Test home endpoint
curl http://localhost:5000/

# Test health check
curl http://localhost:5000/api/health

# Test creating a task (POST)
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"My Task","description":"Task description"}'

# Test adding numbers (POST)
curl -X POST http://localhost:5000/api/add \
  -H "Content-Type: application/json" \
  -d '{"a":5,"b":3}'
```

#### Step 4: Run Unit Tests Locally
```bash
# Run all tests
pytest test_app.py -v

# Run tests with coverage report
pytest test_app.py -v --cov=. --cov-report=html

# View coverage report
# Open htmlcov/index.html in browser
```

**Expected Output:**
```
test_app.py::TestHomeEndpoint::test_home_returns_200 PASSED
test_app.py::TestHealthCheck::test_health_check_returns_200 PASSED
test_app.py::TestTaskOperations::test_create_task_success PASSED
test_app.py::TestBasicMath::test_simple_addition PASSED
...
======================== XX passed in X.XXs ========================
```

---

### **Phase 2: GitHub Setup**

#### Step 5: Push Code to GitHub
```bash
# 1. Initialize git (if not already done)
git init

# 2. Add all files
git add .

# 3. Create initial commit
git commit -m "Initial commit: Flask app with CI/CD pipeline"

# 4. Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/DSO101_Assignment4.git

# 5. Rename branch to main (if needed)
git branch -M main

# 6. Push to GitHub
git push -u origin main
```

**Note:** Replace `YOUR_USERNAME` with your actual GitHub username.

#### Step 6: Verify GitHub Actions Workflow
1. Go to your GitHub repository: `https://github.com/YOUR_USERNAME/DSO101_Assignment4`
2. Click on the **Actions** tab
3. You should see your workflow running automatically
4. Wait for the workflow to complete (should take 1-2 minutes)
5. Verify all checks pass (green checkmarks)

---

### **Phase 3: Render Deployment**

#### Step 7: Create a Render Account
1. Visit https://render.com
2. Sign up with GitHub (recommended for easy integration)
3. Create a new account and verify your email

#### Step 8: Create a Web Service on Render
1. Dashboard → **New +** → **Web Service**
2. Connect your GitHub repository:
   - Select your `DSO101_Assignment4` repository
   - Click **Connect**
3. Configure the service:
   - **Name:** `dso101-assignment4` (or similar)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** `Free` (for learning)
4. Click **Create Web Service**
5. Wait for deployment to complete (3-5 minutes)
6. Once deployed, you'll get a URL like: `https://dso101-assignment4.onrender.com`

#### Step 9: Get Render Deploy Hook URL
1. In your Render service dashboard, go to **Settings**
2. Find **Deploy Hook** section
3. Copy the deploy hook URL
4. **IMPORTANT:** Keep this URL secret!

#### Step 10: Add Deploy Hook to GitHub Secrets
1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `RENDER_DEPLOY_HOOK_URL`
5. Value: Paste the deploy hook URL from Step 9
6. Click **Add secret**

#### Step 11: Test Automated Deployment
1. Make a small change to `app.py` (e.g., update the welcome message)
2. Commit and push:
   ```bash
   git add app.py
   git commit -m "Test deployment trigger"
   git push
   ```
3. Go to GitHub Actions tab and monitor the workflow
4. Once complete, check your Render app URL to confirm the changes are live

---

## 🧪 Testing the Live Application

Once deployed, test your live app:

```bash
# Test home endpoint
curl https://your-app-name.onrender.com/

# Test health check
curl https://your-app-name.onrender.com/api/health

# Test POST request
curl -X POST https://your-app-name.onrender.com/api/add \
  -H "Content-Type: application/json" \
  -d '{"a":10,"b":5}'
```

---

## 📊 Marking Rubric Alignment

| Criteria | Points | Status |
|----------|--------|--------|
| **Project Structure** | 2 | ✅ app.py, test_app.py, requirements.txt, .github/workflows/ci.yml |
| **CI Pipeline (Build + Test)** | 3 | ✅ GitHub Actions with build and test steps |
| **Test Implementation** | 2 | ✅ 30+ comprehensive unit tests in test_app.py |
| **Deployment Automation** | 2 | ✅ Auto-deploy to Render on push to main |
| **Documentation** | 1 | ✅ Detailed README and instructions |
| **TOTAL** | 10 | ✅ All requirements met |

---

## 📸 Screenshots to Capture for Submission

1. **Local Tests Passing:**
   - Run: `pytest test_app.py -v`
   - Screenshot the terminal showing all tests PASSED

2. **GitHub Actions Workflow:**
   - Go to Actions tab in your repository
   - Screenshot the completed workflow run (green checkmarks)

3. **Live App Running:**
   - Test endpoint: `https://your-app.onrender.com/`
   - Screenshot the JSON response

---

## 📦 Submission Checklist

- [ ] GitHub repository created and public
- [ ] All files pushed to main branch
- [ ] `.github/workflows/ci.yml` workflow is running successfully
- [ ] Tests are passing (screenshot saved)
- [ ] App is deployed to Render (live URL working)
- [ ] Auto-deployment working (verified with a test commit)
- [ ] `RENDER_DEPLOY_HOOK_URL` secret configured in GitHub
- [ ] Documentation complete

---

## 🔗 Useful Links

- **Flask Documentation:** https://flask.palletsprojects.com/
- **pytest Documentation:** https://docs.pytest.org/
- **GitHub Actions:** https://docs.github.com/en/actions
- **Render Documentation:** https://render.com/docs
- **HTTP Status Codes:** https://httpwg.org/specs/rfc7231.html#status.codes

---

## 🐛 Troubleshooting

### Issue: Tests fail locally
```bash
# Solution: Ensure all dependencies are installed
pip install -r requirements.txt --force-reinstall
pytest test_app.py -v
```

### Issue: GitHub Actions workflow failing
1. Check the workflow logs in the Actions tab
2. Ensure `requirements.txt` has correct versions
3. Review error messages in the "Run tests" step

### Issue: Render deployment not working
1. Verify the **Build Command** is: `pip install -r requirements.txt`
2. Verify the **Start Command** is: `gunicorn app:app`
3. Check Render service logs for errors

### Issue: Auto-deploy not triggering
1. Verify `RENDER_DEPLOY_HOOK_URL` secret is set in GitHub
2. Check the workflow file has correct secret name
3. Make sure you're pushing to the `main` branch

---

## 💡 Next Steps (Optional Enhancements)

- Add database integration (PostgreSQL)
- Add authentication (JWT tokens)
- Add API documentation (Swagger/OpenAPI)
- Add Docker containerization
- Add performance monitoring
- Add security testing

---

## 📞 Support
If you encounter issues:
1. Check the troubleshooting section above
2. Review the official documentation links provided
3. Check GitHub Actions logs for specific error messages
4. Review Render service logs for deployment errors

**Good luck with your submission! 🚀**
