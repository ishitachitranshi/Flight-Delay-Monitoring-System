✈️ Flight Delay Prediction System with AI Report Generator

A machine learning–powered web application that predicts flight delays and generates AI-based analytical insights. The system uses historical aviation data, weather conditions, and operational factors to estimate the likelihood of delay. Along with prediction, a Large Language Model (LLM) generates a readable, human-friendly explanation highlighting key reasons behind the prediction.

This project combines data science, ML model deployment, explainable AI (XAI), and an interactive UI built using Flask + Streamlit (depending on your deployment).

🚀 Features

✔ Flight Delay Prediction — Predicts whether a flight will be delayed based on input parameters.
✔ AI-Generated Report — LLM summarizes prediction reasoning and suggests improvements.
✔ Feature Analysis — Interprets the influence of weather, airline, time, and route conditions.
✔ Data Visualizations — Displays insights such as seasonal delays, airline comparison, route risk analysis, etc.
✔ Dataset Preview & Exploratory Analysis — View structured dataset highlights.
✔ Downloadable Insights — Export reports and analysis as text or PDF.

🧠 How It Works

The system processes the flight dataset and follows this pipeline:

User Input 
     ↓
Data Preprocessing & Feature Engineering
     ↓
Trained ML Model (Random Forest/XGBoost)
     ↓
Prediction (Delayed / On Time)
     ↓
Explainability + Report Generation using LLM

🛠️ Getting Started
Prerequisites

Python 3.x

pip

Internet access for LLM integration (optional if using local model)

Installation

Clone the repository:

git clone https://github.com/ishitachitranshi/Flight-Delay-Prediction-System.git
cd Flight-Delay-Prediction-System


Create a virtual environment:

python -m venv venv


Activate the environment:

Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

▶️ Running the Application

Start the application:

python app.py


Open the interface in your browser:

👉 http://localhost:5000/

🌐 Deployment

This project can be deployed using platforms like:

Render

Railway

Hugging Face Spaces

Streamlit Cloud

Heroku

Example Procfile (Render/Heroku):

web: gunicorn app:app

📂 Project Structure
/ (project root)
├─ app.py                     # Main Flask/Streamlit Application
├─ model.pkl                 # Trained ML Model
├─ flights.csv               # Dataset
├─ requirements.txt          # Dependencies
├─ README.md                 # Documentation
└─ templates/
   └─ index.html             # UI Template

📊 Sample Output

Prediction: 🚨 Likely Delayed
Confidence: 84.6%

AI Report Excerpt:

"The probability of delay is high due to unfavorable weather (storm), peak travel hour (6 PM), and the selected airline’s historical delay record. This route also experiences higher congestion during winter months. Passengers may expect gate changes or schedule adjustments."

👩‍💻 Author

Ishita Chitranshi

⭐ If this project inspired you, consider giving it a ⭐ on GitHub!
