✈️ Flight Delay Prediction System with AI Report Generator

This project is an AI-powered web application that predicts flight delays and provides intelligent, human-readable explanations. Using historical aviation data and machine learning, the system forecasts whether a flight is likely to be delayed. A Large Language Model (LLM) generates interpretive reports explaining the reasoning behind predictions and highlighting key contributing factors such as weather, airport congestion, season, and airline delay history.

🚀 Features

Flight Delay Prediction using a trained ML model

AI-Generated Report explaining why a prediction occurred

Feature Importance Analysis showing major contributing factors

Data Visualization Dashboards highlighting airline, seasonal, and route-based delays

Dataset Preview and Filtering

Downloadable Insights (Predictions and reports can be exported)

🧠 System Workflow
User Input 
       ↓
Preprocessing & Feature Engineering
       ↓
ML Model Prediction (Random Forest / XGBoost)
       ↓
LLM-Based Explanation & Report Generation

🛠️ Tech Stack

Python

Flask / Streamlit

Scikit-Learn

Pandas / NumPy

Matplotlib / Seaborn

OpenAI / Llama-based LLM integration

📥 Installation

Clone the repository:

git clone https://github.com/ishitachitranshi/Flight-Delay-Prediction-System.git
cd Flight-Delay-Prediction-System


Create and activate a virtual environment:

Windows:

python -m venv venv
venv\Scripts\activate


macOS/Linux:

python -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

▶️ Run the Application
python app.py


Then open in browser:

👉 http://localhost:5000/

🌐 Deployment

This application can be deployed to:

Render

Railway

Streamlit Cloud

Heroku

Example Procfile:

web: gunicorn app:app

📂 Directory Structure
/ (project root)
├─ app.py                      # Main application  
├─ model.pkl                   # Trained ML model  
├─ flights.csv                 # Dataset  
├─ requirements.txt            # Dependencies  
├─ templates/                  # UI  
│   └─ index.html              
└─ README.md                   

📊 Sample Output

Prediction: ✔️ On-Time
Confidence: 79.3%

AI-Generated Explanation:

Based on the input parameters, this flight has a high probability of being on schedule. Weather conditions are clear, the route has a low congestion rating, and the selected airline shows strong on-time performance for similar flights. Morning departures historically show fewer delays on this route.

👩‍💻 Author

Ishita Chitranshi

⭐ If this project helped or inspired you, consider giving it a star on GitHub!
