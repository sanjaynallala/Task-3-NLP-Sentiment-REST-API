# IMDb Sentiment Analysis REST API

## Project Overview
A Natural Language Processing (NLP) project that classifies movie reviews as positive or negative using TF-IDF vectorization and Logistic Regression. The trained model is deployed through a Flask REST API.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Flask REST API
- Joblib

## Dataset
- 19,500 IMDb movie reviews
- 9,750 positive reviews
- 9,750 negative reviews
- No missing values after cleaning

## Model Performance
- Test accuracy: **87.82%**
- Training data: 15,600 reviews
- Testing data: 3,900 reviews

## API Endpoints

### Home
`GET /`

Returns the API status.

### Predict Sentiment
`POST /predict`

Request body:

```json
{
  "review": "This movie was fantastic and entertaining!"
}
```

Example response:

```json
{
  "review": "This movie was fantastic and entertaining!",
  "sentiment": "positive"
}
```

## Installation

```bash
pip install -r requirements.txt
python app.py
```

The API runs locally at `http://127.0.0.1:5000`.

## Project Structure

- `app.py` — Flask API
- `sentiment_model.pkl` — Trained ML pipeline
- `requirements.txt` — Python dependencies
- `IMDB Dataset.csv` — Optional dataset sample

## Note
This model is intended for educational and demonstration purposes. Predictions may not always reflect the intended sentiment of a review.
