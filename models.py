import pymysql

cnx = pymysql.connect(
    host='198.199.93.158',
    port=3306,
    user='root',
    password='shutupPb0y',
    database="CRYPTO"

    # unix_socket="/var/run/mysqld/mysqld.sock"
)


cursor = cnx.cursor()

create_table = """
      create table PRICE2 (
      Symbol VARCHAR(255),
      Price FLOAT(7),
      Ti INTEGER);  
"""

create_database = """
    create database CRYPTO;
"""

insert_crypto = """
    INSERT INTO PRICE2 (symbol, price, Ti) 
    VALUES ("ETHUSDT", 486.006, 1);
"""


select_crypto = """
    select * from PRICE2;
"""
import pandas as pd

print(pd.read_sql(select_crypto, cnx))ls

# cursor.execute(insert_crypto)
# cnx.commit()