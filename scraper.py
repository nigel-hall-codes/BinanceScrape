from binance.client import Client
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time



class Scraper:
    def __init__(self):
        self.api_key = '7tDBYdWpcmbHLSmJJKVd2aCVbzyGwdQ3hDgSfw5MrrXSpjAoufMW5Tkk02W1JiPv'
        self.api_secret = '98BCmuZh6yFLJUYtJ7WtZtCqiMeNTuauxKfzrRQQ82RNnG01HJdxmuXzxZ5SSnyU'
        self.client = Client(self.api_key, self.api_secret)

    def run(self):
        while True:
            tickers = self.client.get_all_tickers()
            server_time = self.client.get_server_time()
            print(server_time)
            for t in tickers:
                if t['symbol'] in ["ETHUSDT", "BTCUSDT"]:
                    print(t['symbol'], ": ", t['price'])
            time.sleep(1)

    def tickers(self):
        return self.client.get_all_tickers()

# s = Scraper()

s = Scraper()
print(s.tickers())