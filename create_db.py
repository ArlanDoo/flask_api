import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

db_host = "127.0.0.1"
db_port = 5432 #Enter port to DB (default - 5432)
db_user = "postgres"
db_password = "postgres"  #Enter pass of ypur DB
db_name = "flask_blogers"    #Enter DB name

def connection_to_db():
    try:
        # Connect to current DB
        connection = psycopg2.connect(database = db_name,
                                    user = db_user,
                                    password = db_password,
                                    host = db_host,
                                    port = db_port)
        # Run autocommit DB
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Create cursor of DB for create query
        cursor = connection.cursor()

        print("Check connect to DB")
        cursor.execute("SELECT version()")
        print(f"Query result: {cursor.fetchone()}")
        
        return cursor
        
    except (Exception, Error) as error:
        
        print(f"PostgreSQL error: {error}")
        return error
    
# Create table (nouns) DB
def create_noun_user():
    
    cursor = connection_to_db()
    
    try:
        cursor.execute("""
                    CREATE TABLE users (
                        id serial primary key,
                        first_name varchar(50) NOT NULL,
                        last_name varchar(128) NOT NULL,
                        age integer,
                        email varchar(256)
                    )
                    """)
        
        print(f"Table USERS created successfully")
    
    except (Exception, Error) as error:
        
        print(f"Create error: {error}")
        return error

def create_noun_post():
    
    cursor = connection_to_db()
    
    try:
        cursor.execute("""
                    CREATE TABLE posts (
                        id serial primary key,
                        author varchar(256) NOT NULL,
                        description text,
                        created date NOT NULL,
                        update date NOT NULL
                    )
                    """)
        
        
        print(f"Table POSTS created successfully")
    
    except (Exception, Error) as error:
        
        print(f"Create error: {error}")
        return error
    # finally:
    #     if connection:
    #         cursor.close()
    #         connection.close()
    #         print("Соединение с PostgreSQL закрыто")
    
def create_tables():
    create_noun_user()
    create_noun_post()

def add_request_str(tablename, values):
    return f"INSERT INTO {tablename} VALUES ({values})"

def test():
    
    testArr = [{"id": 3, "author": "Test 1"}, {"id": 22, "author": "Test 2"}, {"id": 55, "author": "Test 55"}, {"id": 9, "author": "Test 22"}]
    print()