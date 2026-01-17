# 🚨 FraudCheck – Internship Scam Detection Tool

FraudCheck is a web-based application designed to help students **identify potentially fraudulent internship offers**.  
It analyzes internship **URLs and messages** using a combination of **Machine Learning (NLP)** and **rule-based URL verification** to classify them as **SAFE** or **HIGH RISK**.

With the increasing number of fake internship scams targeting students, FraudCheck provides a **simple, fast, and interpretable solution** for early scam detection.

---

## 📌 Problem Statement

Students frequently receive internship offers through emails, WhatsApp, Telegram, and social media platforms.  
Many of these offers:
- Ask for **registration or training fees**
- Use **urgent or threatening language**
- Redirect to **fake or shortened URLs**
- Impersonate well-known companies

Students often find it difficult to verify the authenticity of such offers.

**FraudCheck helps by automatically analyzing the content and links to flag suspicious internship offers.**

---

## ✨ Key Features

- 🔍 Accepts internship **URL and/or message**
- 🤖 Machine Learning–based text classification
- 🔗 Rule-based suspicious URL detection
- 🧠 Trusted domain verification
- ⚠️ Detects scam-related keywords such as:
  - `pay`, `fee`, `urgent`, `verify`, `reward`, `bonus`
- 🌐 Clean and simple frontend interface
- ⚡ Flask REST API backend
- 🔄 Instant risk prediction

---

## 🧩 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Backend
- Python
- Flask
- Flask-CORS

### Machine Learning
- scikit-learn
- joblib
- NLP-based text preprocessing

---

## 📂 Project Structure

```text
FraudCheck/
│
├── logini.html                  # Frontend UI
├── login.css                    # Styling
├── app.py                       # Flask backend
├── internship_scam_model.pkl    # Trained ML model
├── vectorizer.pkl               # Text vectorizer
└── README.md                    # Project documentation
---

## ⚙️ How the System Works

1. The user enters:
   - An internship URL
   - A message received from a recruiter (optional)
2. The frontend sends the combined input to the backend API
3. The backend:
   - Cleans and preprocesses text
   - Detects URLs and checks for suspicious patterns
   - Verifies trusted domains
   - Runs the Machine Learning model
4. A final decision is made:
   - **SAFE**
   - **HIGH RISK**
5. The result is displayed instantly on the frontend

---

## 🧠 Risk Decision Logic

The final risk is marked as **HIGH RISK** if **any** of the following conditions are met:
- Machine Learning model predicts **Scam**
- URL contains suspicious or shortened patterns
- URL is not from trusted domains
- Keywords such as `pay`, `fee`, `urgent`, `payment`, or `verify` are detected

If none of these conditions are met, the result is classified as **SAFE**.

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/FraudCheck.git
cd FraudCheck
### 2️⃣ Start the Backend Server
```bash
python app.py
### 3️⃣ Run the Frontend
- Open `logini.html` in any web browser
- Enter an internship URL and/or message
- Click **Check Now!** to view the risk prediction
---

## 🎯 Use Cases

- Students verifying internship offers
- College scam-awareness initiatives
- Career guidance platforms
- Academic projects and hackathons
- Portfolio project for machine learning and web development roles




