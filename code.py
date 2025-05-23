from twilio.rest import Client
import requests
import os

ACCOUNT_SID = "ACbc13e02cf4702a2fbe90165eb6e98a42"
AUTH_TOKEN = "8593eb002a201e62feef13fed830af30"
FROM_WHATSAPP = 'whatsapp:+14155238886'
TO_WHATSAPP = 'whatsapp:+33771176547'

def get_crypto_prices():
    ids = "bitcoin,kaspa,ergo,ravencoin,nexa"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=eur"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erreur API CoinGecko : {response.status_code}")
    return response.json()

def format_message(prices):
    lines = ["💸 Prix actuels des cryptos :"]
    for name, data in prices.items():
        price = data.get("eur", "N/A")
        lines.append(f"- {name.upper()} : {price} €")
    return "\n".join(lines)

def send_whatsapp_message(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=FROM_WHATSAPP,
        body=message,
        to=TO_WHATSAPP
    )
    print(f"Message envoyé, SID : {message.sid}")

def main():
    prices = get_crypto_prices()
    message = format_message(prices)
    send_whatsapp_message(message)

if __name__ == "__main__":
    main()
