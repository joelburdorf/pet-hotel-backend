from flask import Flask, request
import psycopg2
from flask import Flask

#connect to Db
con = psycopg2.connect(
    host = "localhost",
    database="pet_hotel",
)

#cursor
cur = con.cursor()

#execute query
cur.execute(
    "insert into pets (owner, pet, breed, color, checked_in) values (%s, %s, %s, %s, %s)", ('Melinda', 'Toast', 'Shihpo', 'Tan', 'no'))


# cur.execute("delete from accounts WHERE id='13'" )

cur.execute("SELECT * from pets")

# cur.execute("update accounts SET username ='me' WHERE id='12'")

# cur.execute("SELECT id, username, city from accounts")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} owner {r[1]} pet {r[2]} breed {r[3]} color {r[4]} checked_in {r[5]}")

# commit 
con.commit()

#close the curser
cur.close()

#close connection
con.close()
