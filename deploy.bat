@echo off
echo Creating GitHub repository and pushing code...
echo.

echo 1. Go to https://github.com/new and create a new repository
echo 2. Copy the repository URL
echo 3. Run the following commands in your terminal:
echo.
echo git remote add origin YOUR_REPOSITORY_URL
echo git branch -M main
echo git push -u origin main
echo.
echo Replace YOUR_REPOSITORY_URL with the actual URL of your GitHub repository.
echo.
echo After pushing to GitHub, you can deploy to Render by:
echo 1. Going to https://dashboard.render.com
echo 2. Connecting your GitHub account
echo 3. Creating a new Web Service
echo 4. Selecting your repository
echo 5. Using the following settings:
echo    - Build Command: pip install -r requirements.txt
echo    - Start Command: gunicorn digitalmarketing.wsgi:application
echo    - Environment Variables: PYTHON_VERSION = 3.13.0
echo.
pause