# 🛡️ Phishing Website Detection using Machine Learning

Detect and classify websites as either legitimate or phishing using machine learning. This project leverages a Random Forest model trained on engineered features from malicious and benign URLs. Includes an interactive Streamlit web dashboard for single and bulk URL analysis.

---

## 🚀 Key Features

### 🧪 URL-Based Phishing Detection
- Detects threats using only features extracted from URLs — no external content scraping.
- Supports detection of common attacks like:
  - SQL Injection (SQLi)
  - Cross-Site Scripting (XSS)

### ⚡ Real-time & Bulk Prediction
- 🔍 Paste a single URL to check its safety
- 📁 Upload a CSV file to classify URLs in bulk

### 🧠 ML Model
- Random Forest Classifier with 96%+ accuracy
- Trained on labeled phishing/legitimate URLs

---

## 🗂️ Project Structure

```bash
Phishing-Website-Detection/
├── app.py                  # Streamlit frontend
├── train.py                # Model training script
├── generate_test_csv.py    # Sample CSV generator (optional)
├── requirements.txt        # Dependencies list
├── model/
│   └── phishing_model.pkl  # Saved ML model
├── data/
│   └── phishing_data.csv   # Dataset file
└── README.md               # Project documentation
````

---

## ⚙️ Setup & Installation

1. Clone the repo:

```bash
git clone https://github.com/shreya2794/phishing-website-detector.git
cd phishing-website-detector
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Train the model:

```bash
python train.py
```

4. Launch the Streamlit app:

```bash
streamlit run app.py
```

---

## 📊 Dataset

* Format: `CSV` file with columns `URL`, `Label`
* Labels: `0 = Legitimate`, `1 = Phishing`
* Includes:

  * SQLi & XSS payloads
  * Random, obfuscated phishing URLs
* Modify or extend the dataset inside `/data/phishing_data.csv`

---

## 🧠 Features Used

* Length of URL
* Number of special characters
* Presence of suspicious tokens (e.g., script, select, alert)
* Entropy of query string
* Token pattern frequency
* Number of subdomains

---

## 🌐 Web App Interface

| Mode          | Description                                         |
| ------------- | --------------------------------------------------- |
| 🔗 Single URL | Paste a URL and instantly view prediction & score   |
| 📄 CSV Upload | Upload CSV with URLs and get bulk prediction output |

---

## 👩‍💻 Contributors

| Name           | GitHub Username                                  | 
| -------------- | ------------------------------------------------ | 
| Shreya Dandale | shreya2794 - (https://github.com/shreya2794)     | 
| Harshada Raut  | Harshada-77 - (https://github.com/Harshada-77)   |

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🚧 Future Enhancements

* 🌐 Real-time URL scraping & analysis
* 📈 Feature importance visualization
* 🤖 Deep learning (LSTM/CNN) phishing detectors
* ☁️ Deploy via Streamlit Cloud or HuggingFace Spaces

---

