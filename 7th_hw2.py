import sqlite3
db = sqlite3.connect('student.db')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY,
name VARCHAR,
surname TEXT,
data_of_birth DATE,
hobby TEXT,
homework_points INTEGER
)''')

c.execute('''INSERT INTO student VALUES ('1','Santiago','Koelho','2003','travelling','20')''')
c.execute('''INSERT INTO student VALUES ('2','Adel','Karabay','2004','reading books','21')''')
c.execute('''INSERT INTO student VALUES ('3','Seher','Cholak','2002','learning languages','13')''')
c.execute('''INSERT INTO student VALUES ('4','Anne','Sherley','2001','singing','19')''')
c.execute('''INSERT INTO student VALUES ('5','Kasiyet','Imankulova','2004','photograph','9')''')
c.execute('''INSERT INTO student VALUES ('6','Karina','Bayastan','2005','chess','7')''')
c.execute('''INSERT INTO student VALUES ('7','Saliha','Sagyn','2007','design','5')''')
c.execute('''INSERT INTO student VALUES ('8','Sumaya','Kenzhebek','2000','knitting','12')''')
c.execute('''INSERT INTO student VALUES ('9','Hiko','Sagynbekov','1999','videogames','11')''')
c.execute('''INSERT INTO student VALUES ('10','Venera','Kaya','1995','drawing','14')''')

c.execute('''SELECT * FROM student WHERE LENGTH(surname) > 10''')

print(c.fetchall())

c.execute('''UPDATE student SET name = 'genius' WHERE homework_points > 10''')

c.execute('''SELECT * FROM student WHERE name = "genius"''')

for i in c.fetchall():
    print(i)

c.execute('''DELETE FROM student WHERE id % 2 = 0''')

db.commit()
db.close()
