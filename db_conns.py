import pymysql
import local_settings

def create_connection():
    conn = pymysql.connect(
        host = local_settings.db_host,
        user = local_settings.db_user,
        password = local_settings.db_password,
        port = local_settings.db_port,
        database = local_settings.db_database
    )
    cursor = conn.cursor()
    return conn, cursor

# cursor.execute('CREATE TABLE subscriber_details(name varchar(30), email varchar(40), country varchar(20))')
# Table created permanently
# pymysql.err.InternalError: (1050, "Table 'subscriber_details' already exists")
# Calling func again will raise the above error
# cursor.execute("INSERT INTO subscriber_details values ('gaurav', 'gaurav.bhagwanani@gmail.com', 'India')")

# primary key ke liye!
# cursor.execute('ALTER TABLE subscriber_details ADD PRIMARY KEY (email)')
# conn.commit()

def insert_to_db(name,email,country):
    conn, cursor = create_connection()
    try:
        insert_query = "INSERT INTO subscriber_details values (\'" + name + "\', \'" + email + "\', \'" + country + "\')"
        print(insert_query)
        cursor.execute(insert_query)
    except Exception as e:
        print('exception in insert_to_db method')
        print(e)
    conn.commit()

def get_subs():
    conn, cursor = create_connection()
    cursor.execute('SELECT * FROM subscriber_details')
    subs = []
    for row in cursor:
        subs.append(row)
    return subs

# insert_to_db('gaurav', 'gaurav.bhagwanani@gmail.com', 'China')
# view_subs()