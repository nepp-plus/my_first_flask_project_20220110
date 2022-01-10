from flask import Flask

def create_app():
    # 플라스크 서버를 변수에 담자.
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행
    
    # 이 서버를 사용하도록 결과로 내보내자.
    return app