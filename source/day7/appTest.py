from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0") # 호스트 옵션이고, 모든 아이피에 접속 할 수 있다
    
    