# main.py
import requests
from code import send_whatsapp_message
from web import save_prices_to_file

def get_crypto_prices():
    ids = "bitcoin,kaspa,ergo,ravencoin,nexa"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=eur"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def format_message(prices):
    lines = ["💸 Prix actuels des cryptos :"]
    for name, data in prices.items():
        price = data.get("eur", "N/A")
        lines.append(f"- {name.upper()} : {price} €")
    return "\n".join(lines)

def main():
    prices = get_crypto_prices()
    save_prices_to_file(prices)
    message = format_message(prices)
    send_whatsapp_message(message)

if __name__ == "__main__":
    main()
