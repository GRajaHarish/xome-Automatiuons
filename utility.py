from dotenv import load_dotenv
import os
from mysql.connector import pooling, Error
import mysql.connector
load_dotenv()

def create_connection(db_identifier):
    db_config = get_db_config(db_identifier)
    try:
        connection =pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            pool_reset_session=True,
            host=db_config['host'],
            port=db_config['port'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['name']
        )
        if connection:
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def get_db_config(db_identifier):
    if db_identifier == 'acceptance':
        return {
            'host': os.getenv('DB1_HOST'),
            'port': os.getenv('DB1_PORT'),
            'user': os.getenv('DB1_USER'),
            'password': os.getenv('DB1_PASSWORD'),
            'name': os.getenv('DB1_NAME')
        }
    elif db_identifier == 'Rpad':
        return {
            'host': os.getenv('DB2_HOST'),
            'port': os.getenv('DB2_PORT'),
            'user': os.getenv('DB2_USER'),
            'password': os.getenv('DB2_PASSWORD'),
            'name': os.getenv('DB2_NAME')
        }
    elif db_identifier == 'otp':
        return {
            'host': os.getenv('DB3_HOST'),
            'port': os.getenv('DB3_PORT'),
            'user': os.getenv('DB3_USER'),
            'password': os.getenv('DB3_PASSWORD'),
            'name': os.getenv('DB3_NAME')
        }
    elif db_identifier == 'Client':
        return {
            'host': os.getenv('DB4_HOST'),
            'port': os.getenv('DB4_PORT'),
            'user': os.getenv('DB4_USER'),
            'password': os.getenv('DB4_PASSWORD'),
            'name': os.getenv('DB4_NAME')
        }
    else:
        raise ValueError("Invalid database identifier")
def ExecuteQuery(query,DB):
    pool = None
    try:
        pool=create_connection(DB)
        connection = pool.get_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchone()
            return results
    except Error as e:
        print(f"Error executing query: {e}")
        return None

    finally:
        if connection:
            connection.close()
