# 🔍 ML-based Malicious URL Detector

> An end-to-end machine learning project that detects whether a URL is safe or malicious using NLP and classification techniques.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-18+-61DAFB?logo=react&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikitlearn)
![Accuracy](https://img.shields.io/badge/Accuracy-~96%25-brightgreen)

---

## 📌 Overview

Malicious URLs are a primary vector for phishing, malware delivery, and cyberattacks. This project identifies potentially harmful URLs by analyzing URL text patterns and classifying them as:

- ✅ `good` — Safe URL
- ❌ `bad` — Malicious / Suspicious URL

The system is composed of three parts:

| Component | Description |
|-----------|-------------|
| **MalURL_Model** | Jupyter notebook for model training + dataset |
| **MalURL_Backend** | Flask REST API that loads the model and serves predictions |
| **MalURL_Frontend** | React web interface for user interaction |

---

## 🗂️ Project Structure

```
ML-based-Malicious-URL-Detector/
├── MalURL_Backend/
│   ├── main.py               # Flask API server
│   ├── trained_model.pkl     # Serialized Logistic Regression model
│   └── vectorizer.pkl        # Serialized TF-IDF vectorizer
│
├── MalURL_Frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── package-lock.json
│
├── MalURL_Model/
│   ├── Detecting Malicious URL.ipynb   # Training notebook
│   └── urldata.csv                     # Labeled URL dataset
│
└── README.md
```

---

## ⚙️ How It Works

```
User Input (URL)
      ↓
React Frontend
      ↓  HTTP POST /verify
Flask Backend
      ↓
TF-IDF Vectorizer  →  Logistic Regression Model
      ↓
Prediction: "good" or "bad"
      ↓
SweetAlert2 Popup
```

1. The model is trained on a labeled dataset of URLs (`good` / `bad`)
2. URLs are tokenized and transformed into numerical features via **TF-IDF**
3. A **Logistic Regression** classifier is trained and achieves ~96% accuracy
4. The model and vectorizer are serialized as `.pkl` files
5. The **Flask API** loads these files and exposes a `/verify` endpoint
6. The **React frontend** sends URLs to the API and displays results

---

## 🧰 Tech Stack

### Frontend
- React
- Axios
- SweetAlert2
- React Router DOM

### Backend
- Python / Flask
- Flask-CORS
- Joblib
- Scikit-learn

### Machine Learning
- Pandas & NumPy
- TF-IDF Vectorizer
- Logistic Regression
- Jupyter Notebook

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm

---

### Backend Setup

```bash
# 1. Navigate to the backend folder
cd MalURL_Backend

# 2. Create and activate a virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install flask flask-cors joblib scikit-learn pandas numpy

# 4. Start the server
python main.py
```

The backend will be running at: **http://localhost:5000**

---

### Frontend Setup

```bash
# 1. Navigate to the frontend folder
cd MalURL_Frontend

# 2. Install dependencies
npm install

# 3. Start the React app
npm start
```

The frontend will be running at: **http://localhost:3000**

---

## 📡 API Reference

### `POST /verify`

Checks whether a given URL is safe or malicious.

**Request Body**
```json
{
  "url": "http://example.com"
}
```

**Response**
```json
{
  "result": "good"
}
```
or
```json
{
  "result": "bad"
}
```

---

## 🧪 Model Training

The notebook at `MalURL_Model/Detecting Malicious URL.ipynb` covers the full ML pipeline:

- Loading and exploring `urldata.csv`
- URL preprocessing and tokenization
- TF-IDF vectorization
- Train/test split
- Logistic Regression training
- Model evaluation (~96% accuracy)
- Saving model and vectorizer as `.pkl` files

---

## 💡 Example Use Cases

- Phishing URL detection
- Cybersecurity education and research
- Secure browsing assistants
- URL screening / validation tools
- ML + cybersecurity portfolio projects

---

## 🔮 Future Improvements

- [ ] Advanced feature engineering (domain age, WHOIS data, etc.)
- [ ] Ensemble methods (Random Forest, XGBoost) for improved accuracy
- [ ] URL reputation and domain-based features
- [ ] Docker support and cloud deployment
- [ ] Batch URL scanning
- [ ] Model confidence scores in API response
- [ ] Logging, analytics, and monitoring dashboard
- [ ] Improved frontend UI/UX

---

## ⚠️ Notes

- Ensure `trained_model.pkl` and `vectorizer.pkl` are present in `MalURL_Backend/` before starting the server.
- The frontend communicates with the backend on `localhost` update the endpoint URL before deploying to production.
- CORS is enabled for local development; review CORS settings before any public deployment.

---

## 👤 Author

**Kushan Bhagya**

---

## 📄 License

This project is intended for **educational and portfolio purposes only**.
