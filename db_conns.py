import pymysql
conn = pymysql.connect(
  host='corona-updates.cqeb1h33aftw.ap-south-1.rds.amazonaws.com',
  user='admin',
  password='Covid19Coronavirus_',
  port=3306,
  database = 'sample')

cursor = conn.cursor()

# cursor.execute('CREATE TABLE subscriber_details(name varchar(30), email varchar(40), country varchar(20))')
# Table created permanently
# pymysql.err.InternalError: (1050, "Table 'subscriber_details' already exists")
# Calling func again will raise the above error
# cursor.execute("INSERT INTO subscriber_details values ('gaurav', 'gaurav.bhagwanani@gmail.com', 'India')")

# primary key ke liye!
# cursor.execute('ALTER TABLE subscriber_details ADD PRIMARY KEY (email)')
# conn.commit()

def insert_to_db(name,email,country):
    try:
        insert_query = "INSERT INTO subscriber_details values (\'" + name + "\', \'" + email + "\', \'" + country + "\')"
        print(insert_query)
        cursor.execute(insert_query)
    except Exception as e:
        print('exception in insert_to_db method')
        print(e)
    conn.commit()

def view_subs():
    cursor.execute('SELECT * FROM subscriber_details')
    for row in cursor:
        print(row)

# insert_to_db('gaurav', 'gaurav.bhagwanani@gmail.com', 'China')
# view_subs()