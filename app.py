import os
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import json
from datetime import datetime
app = Flask(__name__)

classifier = pipeline('sentiment-analysis',
    model='distilbert-base-uncased-finetuned-sst-2-english')


@app.route('/')
def home():
     return render_template('index.html')
@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json['text']
    result = classifier(text)[0]
    
    entry = {
        'text': text,
        'label': result['label'],
        'score': result['score'],
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
    app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))    