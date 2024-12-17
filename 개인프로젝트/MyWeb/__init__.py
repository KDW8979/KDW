import json
import pickle
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 모델 로드
model_path = r"C:\Users\kdp\Desktop\Work_권도운\개인프로젝트\MyWeb\models\shakespeare_full_model_logistic.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

# 단어 사전 로드
vocab_path = r"C:\Users\kdp\Desktop\Work_권도운\개인프로젝트\texts\vocab.json"
with open(vocab_path, "r", encoding="utf-8") as f:
    vocab = json.load(f)

TOTAL_FEATURES = 14050


def preprocess_text(text, vocab, total_features=TOTAL_FEATURES):
   
    text = text.lower().strip()

    tokens = text.split()

    feature_vector = [0] * total_features
    for token in tokens:
        token_id = vocab.get(token, len(vocab))  # 단어 인덱스 가져오기
        if token_id < total_features:  # 모델이 학습한 범위 내에서만 카운트
            feature_vector[token_id] += 1

    return feature_vector


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result", methods=["POST"])
def result():
    if "file" not in request.files:
        return redirect(url_for("home"))

    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("home"))

    text = file.read().decode("utf-8")
    processed_input = [preprocess_text(text, vocab)]

    prediction = model.predict(processed_input)[0]
    result = "희극" if prediction == 0 else "비극"

    # 랜덤 명언 리스트
    quotes = [
        "All the world's a stage, and all the men and women merely players.",
        "To be, or not to be, that is the question.",
        "Some are born great, some achieve greatness, and some have greatness thrust upon them.",
        "The better part of valour is discretion.",
        "Love all, trust a few, do wrong to none.",
        "Cowards die many times before their deaths. The valiants never taste of death but once.",
        "All that glisters is not gold."
    ]

    # 랜덤 명언 선택
    import random
    quote = random.choice(quotes)

    return render_template("result.html", prediction=result, quote=quote)


if __name__ == "__main__":
    app.run(debug=True)
