import streamlit as st
from bot import BasicBot

st.set_page_config(page_title="Crypto Trading Bot", layout="centered")
st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>Crypto Trading Bot (Binance Futures Testnet)</h1>
    <hr>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("API Credentials")
    api_key = st.text_input("API Key", type="password")
    api_secret = st.text_input("API Secret", type="password")


# Streamlit does not support native HTML form POST handling, so we use the Streamlit widgets for backend logic
with st.form("order_form"):
    # NOTE:
# Binance Futures enforces strict quantity and price rules:
# - quantity must be >= minQty, <= maxQty, and match stepSize (e.g., 0.001)
# - price must be >= minPrice, <= maxPrice, and match tickSize (e.g., 0.10)
# Violating these will cause errors like:
# "APIError(code=-1013): Filter failure: LOT_SIZE"
# "APIError(code=-4013): Price less than min price"
#
# To find valid ranges, use bot.get_quantity_limits(symbol) and bot.get_symbol_limits(symbol)


    symbol = st.text_input("Symbol (e.g., BTCUSDT)")
    side = st.selectbox("Side", ["BUY", "SELL"])
    order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_MARKET"])
    quantity = st.number_input("Quantity", min_value=0.001, format="%f")
    price = None
    stop_price = None
    if order_type == "LIMIT":
        price = st.number_input("Limit Price", min_value=0.0, format="%f")
    if order_type == "STOP_MARKET":
        stop_price = st.number_input("Stop Price", min_value=0.0, format="%f")
    submitted = st.form_submit_button("Place Order")

if submitted:
    if not all([api_key, api_secret, symbol, side, order_type, quantity]):
        st.error("All fields except price/stop price are required.")
    else:
        try:
            bot = BasicBot(api_key, api_secret)
            result = bot.place_order(symbol.upper(), side.upper(), order_type.upper(), quantity, price, stop_price)
            if result:
                st.success(f"Order placed successfully!\n")
            else:
                st.error("Order failed. Check logs for details.")
        except Exception as e:
            st.error(f"Order failed: {e}")
