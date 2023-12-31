from flask import Flask, jsonify, request
from transformers import AutoModelForSequenceClassification, pipeline


app = Flask(__name__)

classifier = pipeline(model="diegorossi/analysis-sentiment-MOOC")

@app.route('/',methods=['POST'])
def inferir_sentimento():
    content = request.get_json()
    result = classifier(content["message"])
    return jsonify(result[0])

if __name__ == '__main__':
    app.run(debug=True)