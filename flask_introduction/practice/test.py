import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute(" DROP TABLE COMPANY" )
conn.commit()

print "Operation done successfully";
conn.close()