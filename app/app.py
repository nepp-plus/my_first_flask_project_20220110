from flask import Flask, jsonify
from flask.templating import render_template

from .api import user_test, login_test

def create_app():
    # 플라스크 서버를 변수에 담자.
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행
    
    @app.route("/")  # 만들고있는 서버의 / (아무것도 안붙인주소) 로 접속하면 보여줄 내용
    def home():
        # return 내용 : HTML 등 웹 프론트엔드 태그.
        return "<h1>Hello World!!</h1>"  # Hello World 문장 리턴 => 이 내용을 사용자에게 보여주겠다.
    
    @app.route('/module_test')
    def module_test():
        return user_test() # 다른 모듈의 함수의 실행결과를 내보내자. => 로직을, 다른 모듈에서만 작성하면 됨.
    
    @app.route('/login_test')
    def login_01():
        return login_test( 'admin', 'qwer' )
    
    # 이 서버를 사용하도록 결과로 내보내자.
    return app