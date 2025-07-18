from flask import Flask, request

app = Flask(__name__)

@app.route('/') # 라우터를 통해 get함수와 연결됨
# 루트 주소에 GET 요청이 들어오면 아래 함수 실행 

def get():
    value1 = request.args.get('이름', 'user') # '이름' 파라미터가 없으면 기본값 'user' 
    value2 = request.args.get('주소', '부산') # '주소' 파라미터가 없으면 기본값 '부산'
    return value1 + " : " + value2 # 브라우저에 "이름 : 주소" 형식으로 출력 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) # 모든 네트워크에서 접근 가능 + debug 모드

