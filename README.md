# AI Mood Journal

A web app that analyzes the sentiment of your journal entries using AI, and tracks your mood over time with a visual chart.

🔗 **Live Demo:** https://mood-journal-14do.onrender.com

## What It Does

Type a journal entry, and the app analyzes whether it's Positive, Negative, or Neutral using sentiment analysis. Every entry is saved with a timestamp, and the last 7 entries are displayed as a mood chart.

## Tech Stack

- **Backend:** Python, Flask
- **Sentiment Analysis:** VADER Sentiment
- **Frontend:** HTML, CSS, JavaScript
- **Charting:** Chart.js
- **Deployment:** Render

## How to Run Locally

1. Clone this repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `python app.py`
6. Open `http://localhost:7860` in your browser

## Screenshot

(Add a screenshot here once you take one)

## What I Learned

This was my first full-stack project. I learned Flask routing, connecting a frontend to a backend with fetch(), basic NLP sentiment analysis, Git/GitHub workflows, and cloud deployment — including debugging a memory issue that required switching from a transformer-based model to a lighter rule-based one (VADER) to fit free-tier hosting limits.