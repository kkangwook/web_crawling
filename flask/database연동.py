# db 연동
pip install cx_Oracle
pip install oracledb     #이거 사용도 가능(얘가 더 편할수도)/ 자동되는 원리도 cx와 비슷

import cx_Oracle
import oracledb
import pandas

# Oracle DB 연결 정보 설정
username = "c##scott"
password = "tiger"
dsn='127.0.0.1:1521/XE'  # or "host:port/service_name"

# DB 연결
conn = oracledb.connect(username, password, dsn='127.0.0.1:1521/XE',encoding='utf-8')
cursor = conn.cursor()   #커서는 다중행 테이블

# 간단한 쿼리 실행
# ; 사용X!!!!!
cursor.execute("SELECT * FROM dual")  # 오라클 문으로 작성
result = cursor.fetchone()   #첫번째 행만 가져
print(result)

#이 외에도 
cursor.fetchall()    #:모든 행 리스트 형태로
cursor.fetchmany(n)     #: n개 

#이것도 가능
for i in cursor:
    print(i)

#DML문도 실행가능
data = [('a',1), ('b',2), ('c',3), ('d',4), ('e',5)]
cursor.executemany("insert into table(a_col,b_col) values(:1,:2)", data) 
# data의 각 튜플이 :1, :2에 바인딩되어 반복 실행됨을 의미

conn.commit()   #commit필요, cur.execute('commit')도 가
conn.rollback()
#이떄 cursor.executemany로 여러행 insert, update가능

# :x는 바인딩 변수라고 함/ f'{}'대신 사용하기를 권장
sql = "select * from dual where a = :0 , b= :1"
cursor.execute(sql, [280 , 'facility'])  #리스트, 딕셔너리의 형태로 넣음-인덱스 순서대로 인식
#리스트 안의 개수와 바인딩 변수의 개수는 같아야


#레코드 삭제 
data=[50]
query = "delete from dept01 where deptno=:1" # 부서테이블  
cursor.execute(query,data)


#pandas에 저장
row=cursor.fetchall()
df=pd.Dataframe(row)   #row가 리스트 형태이므로 가
print(df)


# 연결 종료
cursor.close()
conn.close()


#추가: 전체과정
try :
    # db 연동 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger') 
    # sql문 실행 객체 
    cursor = conn.cursor()    
    data=[10,30]
    # 4. 레코드 수정 
    query = "update dept01 set dname='NONE' where deptno in(:1,:2)" # 부서테이블  
    cursor.execute(query,data)   
    cursor.execute('select * from dept01')
    dataset = cursor.fetchall() # 전체 레코드 
    
    print('-'*40)
    print('code\t name\t\t\t  loc')
    print('-'*40)
    for row in dataset :
        print("{0:^4}\t{1:<12}\t{2:<5}".format(row[0],row[1],row[2]))
        
    print('-'*40)
    print('전체 레코드 수 : ', len(dataset))        

except Exception as e :
    print('db error :', e)        
finally :
    cursor.close()
    conn.close()
