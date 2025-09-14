# ✈️ Flight Delay Monitoring System

A **Flask web application** that provides an interactive dashboard to analyze flight data, including delays and cancellations.  
The app reads data from a `flights.csv` file, generates real-time visualizations using **Matplotlib** and **Seaborn**, and presents them in a clean, responsive web interface.

---

## 🚀 Features

- 📊 **Data Preview** – Displays the first few rows of the dataset.  
- 📈 **Interactive Plots** – Dynamically generates charts:
  - Top airlines by average delay  
  - Number of cancelled flights by month  
  - Monthly average delay by cause (heatmap)  
- 🎯 **Data Filtering** – Filter plots by airline, month, and number of top entries.  
- 📥 **CSV Download** – Download the raw `flights.csv` dataset.  

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.x  
- pip (Python package manager)  

### Installation

Clone the repository:
```bash
git clone https://github.com/ishitachitranshi/Flight-Delay-Monitoring-System.git
cd Flight-Delay-Monitoring-System
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
▶️ Running the Application
Start the Flask development server:

bash
Copy code
python app.py
Open the app in your browser:
👉 http://localhost:5000

🌐 Deployment
This project can be easily deployed on Render (or similar platforms).

Procfile:

makefile
Copy code
web: gunicorn app:app
requirements.txt: Contains all dependencies (including Gunicorn).

📂 Project Structure
bash
Copy code
/ (project root)
├─ app.py                # Main Flask application
├─ flights.csv           # Flight dataset
├─ requirements.txt      # Python dependencies
├─ Procfile              # Deployment command for Render/Heroku
└─ templates/
   └─ index.html         # Dashboard HTML template

👩‍💻 Author
Ishita Chitranshi

⭐ If you found this project helpful, consider giving it a star on GitHub!


---

Do you also want me to **add badges** (like Python, Flask, Netlify/Render deploy) at the top to make your README look more professional?
