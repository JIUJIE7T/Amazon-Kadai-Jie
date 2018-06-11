import sqlite3

conn = sqlite3.connect('storage.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE STORAGE
         (NAME TEXT PRIMARY KEY     NOT NULL,
         AMOUNT           INT    NOT NULL,
         SALES            REAL);''')

print "Operation successfully";

conn.close()

