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
            try:
                t = self.client.get_server_time()['serverTime']
                for s in self.symbols:

                    data = self.client.get_ticker(symbol=s)
                    models.store_data(t,
                                      s,
                                      data['lastPrice'],
                                      data['lastQty'],
                                      data['askPrice'],
                                      data['askQty'],
                                      data['bidPrice'],
                                      data['bidQty'])
                    time.sleep(1)

            except Exception as e:
                print("Failed at ", datetime.datetime.now())
                print(e)







s = Scraper()
s.run()