from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

class BinanceLogin():
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.authenticated = self.authenticate_login()
        
    def authenticate_login(self):
        try:
            client = Client(self.api_key, self.secret_key)
            client.get_account()
            return client
        except BinanceAPIException as e:
            print(f"Binance API Exception: {e.message}")
            exit()
        except BinanceOrderException as e:
            print(f"Binance Order Exception: {e.message}")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            exit()
            
        