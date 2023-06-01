# import sqlite3
# conn=sqlite3.connect("sqlite.db")
# conn.execute('''
#                 Create table student(
#                 st_id INT AUTO_INCREMENT PRIMARY KEY,
#                 st_name VARCHAR(50),
#                 st_class VARCHAR(10),
#                 st_email VARCHAR(30)
#                 )
#             ''')
# conn.close()


# import sqlite3

# conn = sqlite3.connect("sqlite.db")
# conn.execute('''
#     CREATE TABLE student(
#         st_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         st_name VARCHAR(50),
#         st_class VARCHAR(10),
#         st_email VARCHAR(30)
#     )
# ''')
# conn.close()

import sqlite3
conn=sqlite3.connect("sqlite.db")
ins='''
insert into student (st_id) VALUES
("1,2,3,4")
'''
conn.execute(ins)
conn.commit()
conn.close()

# import sqlite3
# conn=sqlite3.connect("sqlite.db")
# data=conn.execute("SELECT * FROM student")
# "STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL"

# for n in data:
#     print(n[0],"   ",n[1],"       ",n[2],"       ",n[3])

# import sqlite3
# conn=sqlite3.connect("sqlite.db")
# st_id=input("Enter the student Id:- ")
# conn.execute("DELETE FROM student where st_id="+st_id)
# conn.commit()
# conn.close()
