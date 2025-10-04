#!/usr/bin/env python3
"""
Deployment script for Render.com
This script helps prepare the Django application for deployment to Render.
"""

import os
import sys
import subprocess

def check_prerequisites():
    """Check if required tools are installed."""
    try:
        subprocess.run([sys.executable, "--version"], check=True, capture_output=True)
        print("✓ Python is installed")
    except subprocess.CalledProcessError:
        print("✗ Python is not installed")
        return False
    
    try:
        subprocess.run(["pip", "--version"], check=True, capture_output=True)
        print("✓ Pip is installed")
    except subprocess.CalledProcessError:
        print("✗ Pip is not installed")
        return False
        
    return True

def install_requirements():
    """Install Python requirements."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        print("✓ Requirements installed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install requirements: {e}")
        return False

def collect_static():
    """Collect static files."""
    try:
        subprocess.run([sys.executable, "manage.py", "collectstatic", "--noinput"], 
                      check=True, capture_output=True)
        print("✓ Static files collected")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to collect static files: {e}")
        return False

def main():
    """Main deployment preparation function."""
    print("Preparing application for Render deployment...")
    
    if not check_prerequisites():
        print("Please install the required prerequisites and try again.")
        return 1
    
    if not install_requirements():
        print("Failed to install requirements.")
        return 1
    
    if not collect_static():
        print("Failed to collect static files.")
        return 1
    
    print("\n✓ Application is ready for deployment to Render!")
    print("\nTo deploy to Render:")
    print("1. Push your code to your GitHub repository")
    print("2. Connect your repository to Render")
    print("3. Render will automatically use render.yaml for deployment configuration")
    print("\nFor manual deployment, you can also use the Render CLI:")
    print("  render deploy")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())