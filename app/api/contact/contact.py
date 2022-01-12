from pymysql import connect
from pymysql.cursors import DictCursor

# 연락처에 관련된 로직을 담당하는 파일.
# db 연결 / cursor 변수
db = connect(
    host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='admin',
    passwd='Vmfhwprxm!123',  # 프로젝트!123  첫글자만 대문자로.
    db='test_phone_book',
    charset='utf8',
    cursorclass=DictCursor
)

cursor = db.cursor()


def add_contact_to_db(params):
    
    # 사전 검사 : user_id 파라미터의 값이, 실제 사용자 id가 맞는지? 그런 사용자 있는지?
    sql = f"SELECT * FROM users WHERE id={params['user_id']}"
    cursor.execute(sql)
    
    user_result = cursor.fetchone()
    
    if user_result == None:
        return {
            'code': 400,
            'message': '해당 사용자 id값은 잘못되었습니다.'
        }, 400
    
    # 연락처 추가 등록 쿼리
    sql = f"INSERT INTO contacts (user_id, name, phone_num, memo) VALUES ({params['user_id']}, '{params['name']}',  '{params['phone']}', '{params['memo']}')"
        
    cursor.execute(sql)
    db.commit()
    
    return {
        'code': 200,
        'message': '연락처 등록 성공',
    }
    
def get_contacts_from_db(params):
    # 기본 : 해당 사용자의 모든 연락처를 목록으로 리턴.
    # 응용1 : 파라미터에 최신순/이름순 정렬 순서를 받자. => 그에 맞게 리턴.
    # 응용2 : 한번에 10개씩만 내려주자. (게시판처럼 페이징 처리)
    
    sql = f"SELECT * FROM contacts WHERE user_id = {params['user_id']}"
    
    cursor.execute(sql)
    
    # DB의 실행 결과 목록이 담긴 변수.
    query_result = cursor.fetchall()
    
    # 클라이언트에게 전해줄 목록.
    contacts_arr = []
    
    # DB실행결과 한줄 => (가공) => 클라이언트에게 전해줄 목록에 담기도록.
    for row  in query_result:
        # 클라이언트가 받아들이기 편리한 구조로 가공된 연락처를 담을 dict
        contact = {}
        # contact의 내용을 채우자
        contact['id'] = row['id']
        contact['name'] = row['name']
        contact['phone_num'] = row['phone_num']
        contact['memo'] = row['memo']
        
        # datetime으로 오는 데이터를 -> str로 가공해서 담아보자.
        # datetime -> str : strftime 활용. (2022-01-08 01:01:00 양식)
        contact['created_at'] = str(row['created_at'])
        # 내용이 채워진 contact를 리스트에 추가
        contacts_arr.append(contact) 
    
    return {
        'code': 200,
        'message': '내 연락처 목록',
        'data': {
            'contacts': contacts_arr  # 리스트를 통째로 응답으로 -> JSONArray를 응답으로.
        }
    }