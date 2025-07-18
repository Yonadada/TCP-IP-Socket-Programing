from flask import Flask, request # Flask 라이브러리를 import 

app = Flask(__name__)   # Flask 앱 객체 생성

@app.route('/') # URL 경로를 지정(루트  URL)
def helloWorld():   #해당 URL에 접속 시 브라우저에 출력될 내용 반환
    return "hello world"

@app.route('/name')
def name():
    return"<h1>my name is Hong Yeo-Won</h1>"

@app.route('/age')
def age():
    return "<h1>my age is 30 year's old</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) 
    # 서버실행 → host="0.0.0.0"으로 설정하면 외부에서 접속 가능
