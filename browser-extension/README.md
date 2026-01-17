# FraudCheck Browser Extension

This browser extension is a part of the **Internship_Fraud_check** project.  
It helps users quickly analyze internship links directly from the browser and identify potential scam risks.

---

## 📌 Purpose

The extension allows users to:
- Automatically detect the URL of the currently active tab
- Check the link for suspicious patterns such as URL shorteners or payment-related keywords
- Get instant feedback indicating whether the link is **SAFE** or **HIGH RISK**

This makes it easier for students to verify internship links without manually copying and pasting them.

---

## 🧩 Files Overview

```text
browser-extension/
│
├── manifest.json   # Extension configuration file
├── popup.html      # Extension popup UI
├── popup.js        # JavaScript logic for URL detection and risk analysis
└── README.md       # Documentation for the browser extension
****


---

## ⚙️ How the Extension Works

1. User opens the extension from the browser toolbar
2. The extension fetches the URL of the active tab
3. The URL is analyzed using predefined risk rules
4. The result is displayed as:
   - **SAFE**
   - **HIGH RISK**

---

## 🧪 How to Load the Extension (Chrome)

1. Open Chrome and go to:
chrome://extensions
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select the `browser-extension` folder
5. The Internship_Fraud_check extension will be added to your browser

---

## 🔮 Future Improvements

- Connect the extension directly to the FraudCheck backend API
- Automatically scan links on job portals and emails
- Provide detailed risk explanations inside the popup

