import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()
db.close()
##################################################################
# The difference between above and below code is we dont need to call cursor explicitly
# conn.execute will return cursor
conn = sqlite3.connect("contacts.sqlite")

for row in conn.execute("SELECT * FROM contacts"):
    print(row)

conn.close()

########################################################################
db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = 'update@update.com'"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()  # It is always better to commit using cursor connection commit because if we use
# db commit it might pick from the connection pool and commit the wrong connection. Since cursor knows what connection
# they are working on so better to commit that with cursor connection rather than db commit
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()

######################################################################
# If you provide a single value to tuple you have to follow the below syntax i.e (name,)
conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter your name")
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

conn.close()
