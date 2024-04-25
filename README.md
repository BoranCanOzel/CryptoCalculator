## 💱 Crypto Price Converter

## 🌐 Overview
This Python script 🐍, fetches the latest cryptocurrency prices 📈 and calculates how much of a specific cryptocurrency you can buy with a given amount of USD 💵. Supported cryptocurrencies include Ethereum (ETH) 💎, Bitcoin (BTC) ₿, and Litecoin (LTC) 🌕.

## 🔍 How It Works
The script uses BeautifulSoup 🍲 and requests libraries 📚 to scrape cryptocurrency prices from the Bitflyer website 🌐. It then computes the equivalent amount of cryptocurrency for the specified USD amount 💲.

## 📋 Prerequisites
- Python 3.x 🐍
- BeautifulSoup library 🍲
- Requests library 📦

## ⚙️ Setup
1. Install the required Python libraries:
   pip install beautifulsoup4 requests

## 🚀 Usage
Run the script in your Python environment:
python <script_name>.py
Replace <script_name> with the name of the script file 📄.

## 🧮 Example
To find out how much Bitcoin you can buy with 100 USD:
print(calculateCrypto("BTC", 100))

## 📝 Note
This script is for educational purposes and the actual transaction rates may vary. Ensure to check the latest rates and fees from your cryptocurrency exchange.
