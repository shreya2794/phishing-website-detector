# 🛡️ Phishing Website Detection using Machine Learning

Detect and classify websites as either **legitimate or phishing** using Machine Learning.  
This project uses a **Random Forest model** trained on a CSV dataset of malicious and benign URLs with engineered features.  
A **Streamlit dashboard** supports bulk classification by uploading test data in the same format.

---

## 🚀 Key Features

### 🧪 CSV-Based Phishing Detection
- Detects phishing threats using **pre-engineered features** from URLs
- ❌ No live URL pasting or web scraping

### ⚡ Bulk Prediction via CSV Upload
- 📁 Upload a CSV containing extracted features
- ✅ Get predictions with confidence scores
- 🧪 Ideal for offline testing and demonstrations

### 🧠 ML Model
- **Random Forest Classifier** with over **96% accuracy**
- Trained on a **Kaggle phishing dataset**
- Supports **probability-based** scoring

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
URL length

Number of special characters

Suspicious tokens (e.g., script, alert)

Query string entropy

Subdomain count

Pattern frequencies

> ⚠️ **Note:** Uploaded test CSVs **must match the training feature columns** exactly.

---

## 🌐 Streamlit App Interface

| Mode         | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| 📄 CSV Upload | Upload a CSV file with extracted features to classify multiple entries   |

> ❌ This version does **not support raw URL input or scraping**

---

## 👩‍💻 Contributors

| Name           | GitHub Username                                  | 
| -------------- | ------------------------------------------------ | 
| Shreya Dandale | shreya2794 - (https://github.com/shreya2794)     | 
| Harshada Raut  | Harshada-77 - (https://github.com/Harshada-77)   |

---

## 🚧 Future Enhancements

- 🌐 Raw URL input with automatic feature extraction  
- 📈 Feature importance visualization  
- 🤖 Deep learning models (LSTM/CNN)  
- ☁️ Deploy on Streamlit Cloud / HuggingFace Spaces

