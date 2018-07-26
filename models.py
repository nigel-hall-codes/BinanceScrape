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
      Ti INTEGE);  
"""





def store_data(timestamp, price, symbol):

    select_database = "USE CRYPTO;"


    insert_price = """
        INSERT INTO binance_pricing (symbol, price, timestamp)
        VALUES ("{}", {}, {});
    """.format(symbol, price, timestamp)
    print(insert_price)
    cursor.execute(select_database)
    cursor.execute(insert_price)
    cnx.commit()

# cursor.execute(insert_crypto)
# cnx.commit()