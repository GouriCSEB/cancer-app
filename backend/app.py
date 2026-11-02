from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import joblib

app = Flask(__name__, static_folder="dist", static_url_path="")

model = joblib.load("model.pkl")
genes = joblib.load("genes.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    try:
        df = pd.read_csv(request.files["file"], index_col=0)
        df = df.reindex(columns=genes, fill_value=0)
        preds = model.predict(df)
        probs = model.predict_proba(df).max(axis=1)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    results = [
        {"sample": str(s), "prediction": str(p), "confidence": round(float(c), 3)}
        for s, p, c in zip(df.index, preds, probs)
    ]
    return jsonify(results)


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)