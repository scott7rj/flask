import sqlite3
from sqlite3 import Error

try:

    conn = sqlite3.Connection('database.db3')
    conn.execute("insert into employee(employee_code) values(upper('c999999'))")
    conn.commit()

except Error as err:
    print(err)
else:
    conn.close()
