# DB에 있는, contacts 테이블을 표현하는 클래스.

class Contacts:
    # 생성자 -> dict를 넣으면 객체 변수를 자동 세팅.
    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.phone = data_dict['phone_num']  # DB의 컬럼 : phone_num, 변수이름 : phone
        self.memo = data_dict['memo']
        self.created_at = data_dict['created_at']
        
    # 내부 데이터 (객체 변수) 이용 => 앱에 전달하기 좋은 모양의 dict (object)로 재가공.
    def get_data_object(self):
        data = {
            'id': self.id,
            'name': self.name,
            'phone_num': self.phone,
            'memo': self.memo,
            'created_at': str(self.created_at)
        }
        
        return data
        