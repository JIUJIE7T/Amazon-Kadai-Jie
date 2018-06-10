import sqlite3

conn = sqlite3.connect('storage.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE STORAGE
         (NAME TEXT PRIMARY KEY     NOT NULL,
         AMOUNT           INT    NOT NULL,
         SALES            REAL);''')

print "Operation successfully";

conn.close()


import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");