
# 🚀 Crypto Trading Bot (Binance Futures Testnet)

This project provides both a **Streamlit dashboard** and a **command-line interface** to place trades on the **Binance Futures Testnet**. You can place `MARKET`, `LIMIT`, and `STOP_MARKET` orders, check balances, test API connections, and monitor your trade logs.

---

## 📸 Demo Preview

> A user-friendly dashboard to place crypto orders using your Binance Testnet API.

---

## 📁 Project Structure

```
crypto-trading-bot/
├── __pycache__      #stores compiled bytecode files(.pyc) for faster execution. 
├── .gitignore       # Files to ignore in Git
├── app.py           # Streamlit dashboard interface
├── bot.log          # Log file (auto-generated)
├── bot.py           # Core Binance API logic
├── main.py          # CLI-based trading interface
└── README.md        # This file 
└── requirements.txt # Project dependencies

```

---

## ✅ Features

- 🔐 Secure input of API Key and Secret
- 📈 Supports `MARKET`, `LIMIT`, and `STOP_MARKET` orders
- 🔄 Live balance check and connection testing
- 🧾 Detailed logging of all trade attempts (`bot.log`)
- 🧠 Smart error handling with helpful messages
- 🖥️ Streamlit web UI and command-line interface

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Yogita2002Bisht/crypto-trading-bot.git
cd crypto-trading-bot
```

### 2. Install dependencies

Make sure you have Python 3.7+ installed, then run:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Option 1: Streamlit Dashboard (Recommended)

```bash
streamlit run app.py
```

- Input your **Binance Futures Testnet API Key & Secret**
- Choose a symbol (e.g., BTCUSDT), side, order type, and amount
- Click **"Place Order"**
- Check **balance**, **logs**, and **connection status** from the sidebar

---

### Option 2: Command-Line Interface

```bash
python main.py
```

You will be prompted to enter all trade details in the terminal.

---

## 🧪 Binance Testnet Setup

1. Visit the [Binance Futures Testnet](https://testnet.binancefuture.com/)
2. Register an account and log in
3. Generate your **API Key** and **Secret**
4. Use these in the dashboard or CLI tool

> ✅ This bot is fully compatible with **Binance Futures Testnet** — real money is not used.

---

## 🔒 Notes on Quantity and Price Limits

Binance applies strict rules for trading:

- `quantity` must match allowed **minQty**, **maxQty**, and **stepSize**
- `price` must match allowed **minPrice**, **maxPrice**, and **tickSize**

This bot automatically fetches those limits for your selected symbol and displays them in the dashboard.

---

## 📄 Logging

All order actions (success and errors) are saved in `bot.log`.  
This helps you debug API issues or review order history.

---

## 🧑‍💻 Development Notes

- Built with [`streamlit`](https://streamlit.io)
- Binance API via [`python-binance`](https://python-binance.readthedocs.io/)
- Designed for clarity, logging, and educational use

---

## 📜 License

This project is for educational and personal testing purposes only.  
**Use responsibly. Not financial advice.**

---

## 🙋 Support or Questions?

Feel free to open an [issue](https://github.com/Yogita2002Bisht/crypto-trading-bot/issues) .
