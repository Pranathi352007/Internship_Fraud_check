from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re


app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load("internship_scam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    text_lower = text.lower()

    # ---------- URL detection ----------
    contains_url = "http://" in text_lower or "https://" in text_lower or "www." in text_lower

    # Suspicious URL patterns
    suspicious_url_keywords = [
        "bit.ly", "tinyurl", "free", "offer", "pay", "verify",
        "login", "secure", "bonus", "reward"
    ]

    trusted_domains = [
    # Big Tech & Companies
     "google.com", "microsoft.com", "amazon.com", "apple.com",
    "meta.com", "facebook.com", "instagram.com", "whatsapp.com",
    "twitter.com", "x.com", "linkedin.com", "github.com",
    "gitlab.com", "bitbucket.org", "stackoverflow.com",
    "openai.com", "ibm.com", "oracle.com", "salesforce.com",
    "adobe.com", "intel.com", "nvidia.com", "amd.com",

    # Job & Internship Platforms
    "linkedin.com", "internshala.com", "unstop.com", "devpost.com",
    "naukri.com", "indeed.com", "glassdoor.com", "monster.com",
    "freshersworld.com", "angel.co", "wellfound.com",

     "razorpay.com", "paytm.com", "phonepe.com",
    "stripe.com", "paypal.com",
    "googlepay.com", "upi.gov.in",
    # Education & Learning
    "coursera.org", "udemy.com", "edx.org", "skillshare.com",
    "udacity.com", "w3schools.com", "geeksforgeeks.org",
    "hackerrank.com", "leetcode.com", "kaggle.com",

    # Government & Official (India + Global)
    "gov.in", "nic.in", "niti.gov.in", "aicte-india.org",
    "ugc.ac.in", "isro.gov.in", "mygov.in",
    "usa.gov", "gov.uk", "canada.ca",

    # Academic Domains
    "edu.in", "ac.in", "edu", "mit.edu", "stanford.edu",
    "harvard.edu", "ox.ac.uk",

    # Startup & Tech Communities
    "github.com", "gitlab.com", "bitbucket.org",
    "stackoverflow.com", "medium.com",
    "dev.to", "hashnode.com"
]


    url_risky = False

    if contains_url:
        # Check for suspicious words
        for word in suspicious_url_keywords:
            if word in text_lower:
                url_risky = True

        # Check for trusted domains
        is_trusted = any(domain in text_lower for domain in trusted_domains)

        if not is_trusted:
            url_risky = True

    # ---------- ML prediction ----------
    cleaned = clean_text(text)
    X = vectorizer.transform([cleaned])
    prediction = model.predict(X)[0]

    # ---------- FINAL DECISION ----------
    if (
        prediction == "Scam"
        or url_risky
        or "pay" in text_lower
        or "payment" in text_lower
        or "urgent" in text_lower
        or "fee" in text_lower
    ):
        risk = "HIGH RISK"
    else:
        risk = "SAFE"

    return jsonify({
        "prediction": prediction,
        "risk_level": risk
    })

@app.route("/")
def home():
    return "Internship Fraud Risk API is running"

if __name__ == "__main__":
    app.run(debug=True)
