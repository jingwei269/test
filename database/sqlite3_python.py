import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL) ")
    conn.commit()
    conn.close()

def insert_data(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store values(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def update_data(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store set quantity=?, price=? WHERE item=?",(quantity,price,item,))
    conn.commit()
    conn.close()

def delete_data(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows 

# delete_data("Coffee Cup")
# insert_data("Coffee Cup",10,5)
update_data("Coffee Cup",6,9)
print(view())

