import sqlite3

# to connect to database "gamestore.db"      
con = sqlite3.connect("gamestore.db")
print("database connection successful!")
print()
# to create a cursor object
cur = con.cursor()
cur.execute("CREATE TABLE customers(cust_id id INTEGER PRIMARY KEY,cust_name TEXT,ph_no INTEGER)")
cur.execute("CREATE TABLE games(game_id integer, game_name varchar(30), price integer,primary key(game_id))")
cur.execute("CREATE TABLE sales(order_id number, cust_id integer, game_id number , order_date varchar(10), primary key(order_id), foreign key(cust_id) references customers(cust_id) , foreign key(game_id) references games(game_id))")
n=int(input("enter the number of customers-"))
try:
    # intially database tables contain no rows
    # insert data into tables

    # 1. to insert data into customers table
    
    for i in range(1, n+1):
        cust_id = input("enter customer id for customer " + str(i) + ":")
        cust_name = input("enter customer name for customer " + str(i) + ":")
        ph_no = input("enter phone number for customer " + str(i) + ":")
        cur.execute("insert into customers (cust_id,cust_name,ph_no) values(?,?,?)", (cust_id, cust_name, ph_no))

    #to commit the inserted values
        con.commit()

    print('values inserted into customers')

    # to retrieve data from customers table

    print('CUSTOMERS TABLE')
    print()
    cur.execute("select * from customers")
    for row in cur.fetchall():
        print(row)
    print()
    #2. to insert data into games table
   
    for i in range(1, n+1):
        game_id = input('enter game id for game ' + str(i) + ':')
        game_name = input('enter game name for game ' + str(i) + ':')
        price = input('enter price for game ' + str(i) + ':')

        cur.execute("insert into games (game_id,game_name,price) values(?,?,?)", (game_id, game_name, price))
        con.commit()
    print("values inserted into games! ")

    # to retrieve data from games table

    print('GAMES TABLE')
    print()
    cur.execute("select * from games")
    for row in cur.fetchall():
        print(row)
    print()
    #3. to insert into sales table


    for i in range(1, n+1):
        order_id = input('enter order id for sale ' + str(i) + ':')
        cust_id = input('enter customer id for sale ' + str(i) + ':')
        game_id = input('enter game_id for sale ' + str(i) + ':')
        order_date = input('enter order date for sale ' + str(i) + ':')
        cur.execute("insert into sales (order_id,cust_id,game_id,order_date) values(?,?,?,?)",
                (order_id, cust_id, game_id, order_date))
        con.commit()
    print("values inserted into sales! ")

    # to retrieve data from sales table

    print('SALES TABLE')
    print()
    cur.execute("select * from sales")
    for row in cur.fetchall():
        print(row)
    print()

except Exception as ex:
    print('error:', ex)

finally:
    con.close()
    print("database connection terminated!")
