import pymysql
db=pymysql.connect(host='localhost',user='root',password='',database='test003')
print(db)
mycur =db.cursor()
data="""
	CREATE TABLE student_info(Name char(45),Fname char(45),eng int,maths int,sci int)
"""
db.commit()
# mycur.execute("CREATE DATABASE schltool_db")
mycur.close()