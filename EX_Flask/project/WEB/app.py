from flask import Flask
from main_view import mainBP  # Blueprint 임포트

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(mainBP)

if __name__ == "__main__":
    app.run(debug=True)
