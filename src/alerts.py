import requests

COINS = ["bitcoin", "ethereum"]
THRESHOLD = {"bitcoin": 50000, "ethereum": 4000}

def get_price(symbol):
    url = "https://api.coingecko.com/api/v3/simple/price"
    r = requests.get(url, params={"ids": symbol, "vs_currencies": "usd"})
    r.raise_for_status()
    data = r.json()
    return data[symbol]["usd"]

if __name__ == "__main__":
    for coin in COINS:
        price = get_price(coin)
        if price > THRESHOLD[coin]:
            print(f"Alert! {coin} price is {price} USD")
        else:
            print(f"{coin} price is {price} USD - below threshold")
