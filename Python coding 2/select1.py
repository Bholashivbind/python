
import sqlite3
conn=sqlite3.connect("sqlite.db")
# data=conn.execute("SELECT * FROM student")

# "STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL"

# for n in data:
#     print(n)


# import sqlite3
# conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student limit 0,4 ")
"STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL"

for n in data:
    print(n[0],"   ",n[1],"       ",n[2],"       ",n[3])