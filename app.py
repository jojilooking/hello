from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "Hello, 1plat is welcome here!"

@app.route("/callback", methods=["POST"])
def callback():
    data = request.json
    print("📬 Получен callback от 1plat:", data)
    # Можешь добавить тут сохранение в БД, проверку подписи, и т.д.
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
