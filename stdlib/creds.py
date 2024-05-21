import mysql.connector

def dbcred(db):
    data = {} 
    if db=="52":
        data = {
            "DB_host": "34.70.96.52",
            "DB_database": "order_acceptance",
            "DB_user": "order",
            "DB_password": "acceptance"
        }
    elif db=="59":    
        data = {
            "DB_host": "35.239.152.59",
            "DB_database": "ar_db",
            "DB_user": "root",
            "DB_password": "working1728"
        }
    elif db=="95":    
        data = {
            "DB_host": "192.168.2.95",
            "DB_database": "credentials",
            "DB_user": "sam",
            "DB_password": "working"
        }
    return data   

