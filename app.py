import os
from flask import Flask, request, jsonify, render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
from datetime import datetime

app = Flask(__name__)

analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json['text']

    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        label = 'POSITIVE'
    elif compound <= -0.05:
        label = 'NEGATIVE'
    else:
        label = 'NEUTRAL'

    entry = {
        'text': text,
        'label': label,
        'score': abs(compound),
        'timestamp': datetime.now().isoformat()
    }

    try:
        with open('entries.json', 'r') as f:
            entries = json.load(f)
    except FileNotFoundError:
        entries = []

    entries.append(entry)

    with open('entries.json', 'w') as f:
        json.dump(entries, f, indent=2)

    return jsonify(entry)

@app.route('/entries', methods=['GET'])
def get_entries():
    try:
        with open('entries.json', 'r') as f:
            entries = json.load(f)
    except FileNotFoundError:
        entries = []

    return jsonify(entries)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 7860)))