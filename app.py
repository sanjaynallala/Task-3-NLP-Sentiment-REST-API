from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("sentiment_model.pkl")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "IMDb Sentiment Analysis API is running",
        "status": "success"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not isinstance(data.get("review"), str):
        return jsonify({"error": "Provide a review as a string in JSON"}), 400

    review = data["review"].strip()

    if not review:
        return jsonify({"error": "Review cannot be empty"}), 400

    sentiment = model.predict([review])[0]

    return jsonify({
        "review": review,
        "sentiment": sentiment
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)