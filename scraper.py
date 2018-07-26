from binance.client import Client
import datetime
import time
import models



class Scraper:
    def __init__(self):
        self.api_key = '7tDBYdWpcmbHLSmJJKVd2aCVbzyGwdQ3hDgSfw5MrrXSpjAoufMW5Tkk02W1JiPv'
        self.api_secret = '98BCmuZh6yFLJUYtJ7WtZtCqiMeNTuauxKfzrRQQ82RNnG01HJdxmuXzxZ5SSnyU'
        self.client = Client(self.api_key, self.api_secret)

    def run(self):
        while True:
            try:
                tickers = self.client.get_all_tickers()
                server_time = self.client.get_server_time()['serverTime']
                print(server_time)
                for t in tickers:
                    if t['symbol'] in ["ETHUSDT", "BTCUSDT"]:
                        print(t['symbol'], ": ", t['price'])
                        models.store_data( int(server_time), float(t['price']), t['symbol'])
                time.sleep(1)
            except Exception as e:
                print(e)
    def tickers(self):
        return self.client.get_all_tickers()

# s = Scraper()

if __name__ == '__main__':
    s = Scraper()
    s.run()