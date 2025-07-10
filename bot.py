print(">>> bot.py loaded")  # Debug to confirm the file is being run

from binance.client import Client
from binance.enums import *
ORDER_TYPE_STOP_MARKET = 'STOP_MARKET'  # Add missing constant for STOP_MARKET order type
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        print(">>> Inside BasicBot constructor")  # Debug line
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'  # Use Futures Testnet

        # Setup logging
        logging.basicConfig(
            filename='bot.log',
            filemode='a',
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        print(">>> Placing order inside class")  # Debug line

        try:
            # Prepare order parameters
            params = {
                "symbol": symbol,
                "side": SIDE_BUY if side == 'BUY' else SIDE_SELL,
                "type": order_type,
                "quantity": quantity
            }

            # Add price and timeInForce if LIMIT order
            if order_type == ORDER_TYPE_LIMIT:
                if price is None:
                    raise ValueError("Limit order requires a price.")
                params["price"] = price
                params["timeInForce"] = TIME_IN_FORCE_GTC

            # Add stopPrice if STOP_MARKET order
            if order_type == ORDER_TYPE_STOP_MARKET:
                if stop_price is None:
                    raise ValueError("Stop-Market order requires a stop price.")
                params["stopPrice"] = stop_price

            # Send the order to Binance Futures Testnet
            order = self.client.futures_create_order(**params)

            print("✅ Order placed successfully:")
            print(order)
            logging.info(f"✅ Order placed: {order}")
            return order

        except Exception as e:
            print("❌ Order failed with error:", e)
            logging.error(f"❌ Order failed: {e}")
            return None
