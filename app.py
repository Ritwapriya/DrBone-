from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "DrBone API Running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    
    # Save uploaded image
    filepath = "temp.jpg"
    file.save(filepath)

    # Dummy response (we'll connect model later)
    return jsonify({
        "prediction": "Fracture Detected",
        "confidence": "92%"
    })

if __name__ == "__main__":
    app.run()
