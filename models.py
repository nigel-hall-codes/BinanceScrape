import pymysql

cnx = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='nhall',
    password='shutupPb0y',
    database="TCN"
)

cursor = cnx.cursor()

def store_data(timestamp, symbol, lastprice, lastqty, askprice, askqty, bidprice, bidqty):

    select_database = "USE TCN;"
    insert_price = """
        INSERT INTO binance_pricing_1sec (timestamp, symbol, lastprice, lastqty, askprice, askqty, bidprice, bidqty)
        VALUES ({}, "{}", {}, {}, {}, {}, {});
    """.format(timestamp, symbol, lastprice, askprice, askqty, bidprice, bidqty)
    cursor.execute(select_database)
    cursor.execute(insert_price)
    cnx.commit()


def create_pricing_table():
    select_database = "USE TCN;"
    create_table_q = """
        CREATE TABLE binance_pricing_1sec (timestamp BIGINT, symbol VARCHAR(10),lastprice FLOAT, lastqty FLOAT, 
        askprice FLOAT, askqty FLOAT, bidprice FLOAT, bidqty FLOAT);
    """

