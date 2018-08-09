
import MySQLdb


db= MySQLdb.connect(host="localhost",
                    user='demouser',
                    password='password',
                    db='testDB'
                    )

cur = db.cursor()

cur.execute("Select FirstName from Person where PersonID=2")
print(cur)
for row in cur.fetchall():
    print(row[0])

db.close()