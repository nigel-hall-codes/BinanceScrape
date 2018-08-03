from binance.client import Client
import datetime
import time
import models



class Scraper:
    def __init__(self):
        self.api_key = '4q1Tmp8ATgJ49AqubnH7NU6nm1P23k3QDibHmVAfXpO0x1CBb5TMYMb0gsPLyH6Y'
        self.api_secret = "CxpRkkyab0S2hxAS9uiQiE6quLf8xZQFfPBK6caIsTLHwfUvQFrOmiFb5AzqyTpn"
        self.client = Client(self.api_key, self.api_secret)
        self.symbols = ["BTCUSDT", "ETHUSDT"]


    def run(self):
        while True:
            for 
            try:

                btc = self.client.get_ticker(symbol="BTCUSDT")
                eth = self.client.get_ticker(symbol='ETHUSDT')

                server_time = self.client.get_server_time()['serverTime']

                for t in tickers:
                    if t['symbol'] in ["ETHUSDT", "BTCUSDT"]:

                        models.store_data(int(server_time), float(t['price']), t['symbol'])
                time.sleep(1)
            except Exception as e:
                print(e)
    def tickers(self):
        return self.client.get_all_tickers()

# s = Scraper()

if __name__ == '__main__':
    s = Scraper()
    s.run()