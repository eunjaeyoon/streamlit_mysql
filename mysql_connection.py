import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yhdb.cvtuufc0they.ap-northeast-2.rds.amazonaws.com',
        database = 'streamlit_db',
        user = 'admin',
        password = 'dms230145'
    )
    return connection
