import pymysql

mypass = "root"
mydatabase = "music"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

create_table_query = """
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40),
    age INT,
    grade_level INT
)
"""

cur.execute(create_table_query)
con.commit()
