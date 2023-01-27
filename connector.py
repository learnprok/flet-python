import json
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='brian123',
                             database='prueba',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM user;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(type(result))


j = json.dumps(result)
print(j)

with open("student_objects.js", "w") as f:
    f.write(j)

