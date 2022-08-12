import pymysql.cursors
import pymysql as pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='mydata',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


def update(sql):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
    finally:
        if connection.open:
            connection.close()


def query(sql):
    return_list = []
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    return_list.append(row)
                return return_list
    finally:
        if connection.open:
            connection.close()
            return return_list


