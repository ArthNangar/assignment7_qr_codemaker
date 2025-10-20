# 📦 Project Setup (Windows)

# 🧩 1. Install and Configure Git

Download and install Git for Windows: https://git-scm.com/download/win  
During installation, accept default options.

Verify Git installation:
  git --version

Set your global username and email:
-
  git config --global user.name "Your Name"

  git config --global user.email "your_email@example.com"

---

# 🧩 2. Clone Your Repository

Clone your repository and move into it:

  git clone https://github.com/ArthNangar/assignment7_qr_codemaker.git

---

# 🧩 3. Install Python

Download and install Python 3.10 or higher from https://www.python.org/downloads/  

Verify installation:
  python --version

---

# 🧩 4. Create and Activate Virtual Environment

Create a virtual environment:

  python -m venv venv

Activate it:

  venv\Scripts\activate.bat

Install dependencies:

  pip install -r requirements.txt

---

# 🐳 5. Docker Setup

Install Docker Desktop for Windows: 

https://www.docker.com/products/docker-desktop/  

Ensure Docker is running.

Build the image:
  docker build -t <image-name> .

Run the container:
  docker run -it --rm <image-name>

---

# 🚀 6. Running the Project

To run without Docker:
  python main.py

To run with Docker:
  docker run -it --rm <image-name>

Or
docker run -v ./qr_codes:/app/qr_codes arthnangar7/qr_codemaker

Or
docker compose up

---
# 👤 Author
Arth Nangar

Date: 10/19/2025

