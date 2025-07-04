# AI-vs-Human Text Classification

## Prerequisites

1. Python 3.12+
2. Create & activate a virtualenv:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Proposed Problem

**Problem:** It’s hard to know if a given text was written by a human or generated by an AI.

**Solution:** Train a supervised model that labels each input text as `AI` or `Human`.

## Implementation Details & Solution

### Labels

* `Human`: real human-written documents
* `AI`: samples generated by GPT-type models

### Features

* TF–IDF vectors

### Training

1. Split data 80/20 (train/test)
2. Fit RandomForest on our feature set
3. Evaluation of **accuracy**, **precision**, **recall**, **F1**

## Why This Matters

* Automate moderation, integrity checks, spam filtering, and analytics on AI content.

## Usage

```bash
# Start the API
python webserver.py

# Example request
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"text":"Your text here"}'
```