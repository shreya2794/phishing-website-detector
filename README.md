**Phishing Website Detection using Machine Learning**
This project detects phishing websites using a trained machine learning model based on extracted features from URLs. The app is built using Streamlit for the interface and Random Forest Classifier for detection. It classifies a given website URL as either Benign (safe) or Malicious (phishing).

**Features**
Classifies URLs as legitimate or phishing
Detects common attacks like SQL Injection (SQLi) and Cross-Site Scripting (XSS)
Lightweight and fast – uses only URL-based features
Interactive Streamlit dashboard for real-time or bulk URL prediction

**Project Structure**
Phishing-Website-Detection/
├── app.py ← Streamlit dashboard
├── train.py ← Model training script
├── generate_test_csv.py ← (Optional) script to create sample test CSVs
├── requirements.txt ← Python dependencies
├── model/
│ └── phishing_model.pkl ← Trained model
├── data/
│ └── phishing_data.csv ← Input dataset (URLs + labels)
└── README.md

**Installation:-**
Clone the repository

git clone  https://github.com/shreya2794/phishing-website-detector.git
cd phishing-website-detector

Install dependencies

pip install -r requirements.txt

Train the model

python train.py

Launch the web app

streamlit run app.py

**Dataset**
The dataset includes benign and phishing URLs, including injection payloads like SQLi and XSS.
Format: CSV file with columns URL, Label
Label: 0 = Benign, 1 = Malicious

You can customize or expand the dataset inside the /data folder.

**Model**
Model Used: Random Forest Classifier

**Features Extracted:**
Number of query tokens
Query string entropy
Presence of suspicious keywords (like script, or, and)
Special characters or XSS indicators
Length and pattern of tokens

**Web App Modes**
Single URL Prediction
Enter a URL manually and view its classification in real-time.

Bulk Prediction via CSV Upload
Upload a CSV file of URLs and get their classification results instantly.

**Contributors:-**
(1)Name: Shreya Dandale
GitHub: https://github.com/shreya2794

(2)Name: Harshada Raut
GitHub: https://github.com/Harshada-77



**License**
This project is licensed under the MIT License. See LICENSE file for details.

**Future Enhancements**
Integrate real-time URL scrapers
Visualize feature importance
Add deep learning-based detection for advanced phishing attempts
Deploy app using Streamlit Cloud or Hugging Face Spaces
