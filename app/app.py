from flask import Flask, jsonify
from flask.templating import render_template

from .api import user_test

def create_app():
    # 플라스크 서버를 변수에 담자.
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행
    
    @app.route("/")  # 만들고있는 서버의 / (아무것도 안붙인주소) 로 접속하면 보여줄 내용
    def home():
        # return 내용 : HTML 등 웹 프론트엔드 태그.
        return "<h1>Hello World!!</h1>"  # Hello World 문장 리턴 => 이 내용을 사용자에게 보여주겠다.
    
    @app.route("/test") # 서버의 /test 주소로 오면 수행해줄 일을 작성.
    def test(): 
        return "이 곳은 테스트 페이지 입니다."
    
    @app.route("/web")
    def web_test():
        return render_template('web_test.html')  # templates 폴더 내부의 파일을 불러주는 역할.
    
    @app.route("/json")
    def json_test():
        # JSON : 양식 => "이름표" : 실제 값의 조합. => dict를 이용하면 작업이 편하다.
        test_dict = {}
        test_dict['name'] = '조경진'
        test_dict['birth_year'] = 1988
        test_dict['height'] = 187.7
        test_dict['is_male'] = True
        
        return jsonify(test_dict) # dict -> json 변경 함수 활용, JSON 응답 내려주기
    
    @app.route('/json2')
    def json_test2():
        hello_dict = {}
        hello_dict['korean'] = "안녕하세요"
        hello_dict['english'] = 'Hello'
        
        return hello_dict
    
    @app.route('/json3')
    def json_test3():
        
        user_dict = {}
        user_dict['name'] = 'CKJ'
        user_dict['birth_day'] = '1988-10-20'
        
        return {
            'code': 200,
            'message': 'json test ok',
            'data': user_dict
        }
        
    @app.route('/module_test')
    def module_test():
        return user_test()
    
    # 이 서버를 사용하도록 결과로 내보내자.
    return app