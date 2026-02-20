import sqlite3

# Connect to database (creates data.db if not exists)
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Create Students table
table = """
CREATE TABLE IF NOT EXISTS Students(
    name VARCHAR(30),
    class VARCHAR(10),
    marks INT,
    company VARCHAR(30)
)
"""
cursor.execute(table)

# Insert records
cursor.execute("""INSERT INTO Students VALUES('Sijo', 'BTech', 75, 'JSW')""")
cursor.execute("""INSERT INTO Students VALUES('Lijo', 'MTech', 69, 'TCS')""")
cursor.execute("""INSERT INTO Students VALUES('Rijo', 'BSc', 79, 'WIPRO')""")
cursor.execute("""INSERT INTO Students VALUES('Sibin', 'MSc', 89, 'INFOSYS')""")
cursor.execute("""INSERT INTO Students VALUES('Dilsha', 'MCom', 99, 'Cyient')""")

print("The inserted records:")
df = cursor.execute("""SELECT * FROM Students""")

for row in df:
    print(row)

# Commit and close
connection.commit()
connection.close()