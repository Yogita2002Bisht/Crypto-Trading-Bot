from bot import BasicBot

def main():
    print(">>> Starting bot")  # Debug line

    api_key = input("Enter API Key: ").strip()
    api_secret = input("Enter Secret Key: ").strip()

    print(">>> Initializing bot...")  # Debug line
    bot = BasicBot(api_key, api_secret)

    symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter Side (BUY/SELL): ").upper()
    order_type = input("Enter Order Type (MARKET/LIMIT/STOP_MARKET): ").upper()
    quantity = float(input("Enter Quantity: "))

    price = None
    stop_price = None
    
    print(" quantity must be >= minQty, <= maxQty, and match stepSize (e.g., 0.001 ," \
    "price must be >= minPrice, <= maxPrice, and match tickSize (e.g., 0.10)")
    
    if order_type == "LIMIT":
        price = float(input("Enter Limit Price: "))
    elif order_type == "STOP_MARKET":
        stop_price = float(input("Enter Stop Price: "))

    print(">>> Placing order...")  # Debug line
    result = bot.place_order(symbol, side, order_type, quantity, price, stop_price)

    if result:
        print("✅ Order placed successfully!")
    else:
        print("❌ Order failed.")

if __name__ == "__main__":
    main()


print(">>> End of script")
