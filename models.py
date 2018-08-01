import pymysql

cnx = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='nhall',
    password='shutupPb0y',
    database="TCN"
)

cursor = cnx.cursor()

def store_data(timestamp, price, symbol):

    select_database = "USE TCN;"
    insert_price = """
        INSERT INTO binance_pricing_1sec (timestamp, price, symbol)
        VALUES ({}, {}, "{}");
    """.format(timestamp, price, symbol)
    cursor.execute(select_database)
    cursor.execute(insert_price)
    cnx.commit()
