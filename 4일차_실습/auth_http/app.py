from flask import Flask, jsonify, render_template
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# 사용자 정보
users = {
    "admin": "secret",
    "guest": "guest"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route('/protected')
@auth.login_required
def protected():
    return render_template('secret.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# - `@auth.verify_password` (사용자 인증)
#     사용자 이름과 비밀번호가 유효한지 확인하는 함수를 정의합니다. 여기서는 간단한 사전 **`users`**를 사용하여 사용자 이름과 비밀번호를 확인합니다. 실전 환경에서는 데이터베이스 또는 다른 안전한 저장소를 사용해야합니다.

# - `@auth.login_required` (라우트 보호)
#     인증된 사용자만 해당 라우트로 접근할 수 있도록하는 목적. 사용자 인증을 요구.

# - `@auth.error_handler` (오류 핸들링)
#     인증에 실패했을 때의 동작을 정의
#     위 코드에서는 403 상태 코드와 함께 오류 메시지를 반환