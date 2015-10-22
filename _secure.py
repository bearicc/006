import mysql.connector

dbconfig = {
    'user': 'XXX',
    'password': 'XXX',
    'host': 'localhost',
    'database': 'XXX'
}

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name='XXX', pool_size=5, **dbconfig)
