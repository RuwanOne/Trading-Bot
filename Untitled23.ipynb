{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "610be3f4-f74a-4f8b-8381-3464898c1e19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Using Binance server time: 1740312567900\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "import requests\n",
    "\n",
    "# Get Binance server time\n",
    "server_time = requests.get(\"https://api.binance.com/api/v3/time\").json()[\"serverTime\"]\n",
    "\n",
    "# Use the server time for your API request\n",
    "params = {\n",
    "    \"timestamp\": server_time,  # Instead of using local system time\n",
    "    \"recvWindow\": 5000,  # Increase recvWindow to 5000-10000 if needed\n",
    "}\n",
    "\n",
    "print(\"Using Binance server time:\", server_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "90b8439b-4eb0-49d3-bfef-c7a91210f408",
   "metadata": {},
   "outputs": [],
   "source": [
    "params = {\n",
    "    \"timestamp\": server_time,\n",
    "    \"recvWindow\": 50000,  # 50 seconds\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "36c38266-5130-4f2a-ba7c-cf947e01926c",
   "metadata": {},
   "outputs": [],
   "source": [
    "time_offset = server_time - int(time.time() * 1000)\n",
    "adjusted_timestamp = int(time.time() * 1000) + time_offset\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22da917a-fd54-41f7-b735-70dfd45700f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ BUY order executed at 96078.01: {'info': {'symbol': 'BTCUSDT', 'orderId': '37506292276', 'orderListId': '-1', 'clientOrderId': 'x-R4BD3S82d274b29cb0ad63f8cd138f', 'transactTime': '1740312635923', 'price': '0.00000000', 'origQty': '0.00010000', 'executedQty': '0.00010000', 'origQuoteOrderQty': '0.00000000', 'cummulativeQuoteQty': '9.60780200', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'workingTime': '1740312635923', 'fills': [{'price': '96078.02000000', 'qty': '0.00010000', 'commission': '0.00000010', 'commissionAsset': 'BTC', 'tradeId': '4582391509'}], 'selfTradePreventionMode': 'EXPIRE_MAKER'}, 'id': '37506292276', 'clientOrderId': 'x-R4BD3S82d274b29cb0ad63f8cd138f', 'timestamp': 1740312635923, 'datetime': '2025-02-23T12:10:35.923Z', 'lastTradeTimestamp': 1740312635923, 'lastUpdateTimestamp': 1740312635923, 'symbol': 'BTC/USDT', 'type': 'market', 'timeInForce': 'GTC', 'postOnly': False, 'reduceOnly': None, 'side': 'buy', 'price': 96078.02, 'triggerPrice': None, 'amount': 0.0001, 'cost': 9.607802, 'average': 96078.02, 'filled': 0.0001, 'remaining': 0.0, 'status': 'closed', 'fee': {'currency': 'BTC', 'cost': 1e-07}, 'trades': [{'info': {'price': '96078.02000000', 'qty': '0.00010000', 'commission': '0.00000010', 'commissionAsset': 'BTC', 'tradeId': '4582391509'}, 'timestamp': None, 'datetime': None, 'symbol': 'BTC/USDT', 'id': '4582391509', 'order': None, 'type': None, 'side': None, 'takerOrMaker': None, 'price': 96078.02, 'amount': 0.0001, 'cost': 9.607802, 'fee': {'currency': 'BTC', 'cost': 1e-07}, 'fees': [{'currency': 'BTC', 'cost': 1e-07}]}], 'fees': [{'currency': 'BTC', 'cost': 1e-07}], 'stopPrice': None, 'takeProfitPrice': None, 'stopLossPrice': None}\n",
      "✅ First buy executed at 96078.01\n",
      "ℹ️ No sell condition met. Current price 96078.02 is below target 105685.811.\n"
     ]
    }
   ],
   "source": [
    "import ccxt\n",
    "import time\n",
    "import numpy as np\n",
    "\n",
    "# Binance API credentials (replace with your own)\n",
    "api_key = \"Sk2Y03rcJ2lcLWJzDJs8RcRX9bO82CcF1qT9tH0fPE8OekXLcYBVfMFHdZqkDtgw\"\n",
    "api_secret = \"DGGzCIt04vurMZvZYOeBhaPfGwOUrWRqecrjpdGxDHRwqoxHUSdi0SJHKL3eYqxm\"\n",
    "\n",
    "# Initialize Binance\n",
    "exchange = ccxt.binance({\n",
    "    'apiKey': api_key,\n",
    "    'secret': api_secret,\n",
    "    'enableRateLimit': True\n",
    "})\n",
    "\n",
    "# Trading parameters\n",
    "symbol = 'BTC/USDT'\n",
    "trade_amount = 10  # Amount in USDT per trade\n",
    "buy_levels = []  # Stores buy prices\n",
    "btc_holding = 0\n",
    "\n",
    "\n",
    "def fetch_current_price():\n",
    "    \"\"\"Fetch the latest BTC price.\"\"\"\n",
    "    ticker = exchange.fetch_ticker(symbol)\n",
    "    return ticker['last']\n",
    "\n",
    "\n",
    "def get_balance(asset):\n",
    "    \"\"\"Fetch balance of a given asset.\"\"\"\n",
    "    balance = exchange.fetch_balance()\n",
    "    return balance['total'].get(asset, 0)\n",
    "\n",
    "\n",
    "def place_order(side, amount):\n",
    "    \"\"\"Execute a market order.\"\"\"\n",
    "    try:\n",
    "        price = fetch_current_price()\n",
    "        order = exchange.create_market_order(symbol, side, amount)\n",
    "        print(f\"✅ {side.upper()} order executed at {price}: {order}\")\n",
    "        return price\n",
    "    except ccxt.BaseError as e:\n",
    "        print(f\"❌ Order failed: {e}\")\n",
    "        return None\n",
    "\n",
    "\n",
    "def check_trade():\n",
    "    global btc_holding, buy_levels\n",
    "    \n",
    "    last_price = fetch_current_price()\n",
    "    usdt_balance = get_balance(\"USDT\")\n",
    "    btc_balance = get_balance(\"BTC\")\n",
    "    \n",
    "    if not buy_levels:\n",
    "        btc_amount = trade_amount / last_price\n",
    "        executed_price = place_order('buy', btc_amount)\n",
    "        if executed_price:\n",
    "            buy_levels.append(executed_price)\n",
    "            btc_holding += btc_amount\n",
    "            print(f\"✅ First buy executed at {executed_price}\")\n",
    "    else:\n",
    "        last_buy_price = buy_levels[-1]\n",
    "        next_buy_price = last_buy_price * 0.95\n",
    "        if last_price <= next_buy_price:\n",
    "            btc_amount = trade_amount / last_price\n",
    "            executed_price = place_order('buy', btc_amount)\n",
    "            if executed_price:\n",
    "                buy_levels.append(executed_price)\n",
    "                btc_holding += btc_amount\n",
    "                print(f\"✅ Additional buy executed at {executed_price}\")\n",
    "            else:\n",
    "                print(\"❌ Additional buy attempt failed.\")\n",
    "        else:\n",
    "            print(f\"ℹ️ Price has not dropped 5% from the last buy price {last_buy_price}.\")\n",
    "    \n",
    "    if buy_levels and btc_holding > 0:\n",
    "        average_buy_price = np.mean(buy_levels)\n",
    "        target_sell_price = average_buy_price * 1.1\n",
    "        if last_price >= target_sell_price:\n",
    "            print(f\"✅ Selling all BTC at {last_price}, target reached.\")\n",
    "            place_order('sell', btc_holding)\n",
    "            buy_levels.clear()\n",
    "            btc_holding = 0\n",
    "        else:\n",
    "            print(f\"ℹ️ No sell condition met. Current price {last_price} is below target {target_sell_price}.\")\n",
    "\n",
    "\n",
    "while True:\n",
    "    try:\n",
    "        check_trade()\n",
    "        time.sleep(60)  # Check market every minute\n",
    "    except Exception as e:\n",
    "        print(f\"⚠️ Error: {e}\")\n",
    "        time.sleep(10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74b8a2ee-0f68-47cd-9719-456d9780f9bf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
