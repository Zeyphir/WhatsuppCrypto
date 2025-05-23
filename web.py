# web.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
import os

app = FastAPI()
DATA_FILE = os.path.join(os.path.dirname(__file__), "prices.json")

def save_prices_to_file(prices):
    with open(DATA_FILE, "w") as f:
        json.dump(prices, f)

@app.get("/", response_class=HTMLResponse)
def home():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            prices = json.load(f)
    else:
        prices = {}

    html = """
    <html>
    <head>
        <title>Prix Crypto</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet" />
    </head>
    <body class="bg-gray-900 text-white p-8">
        <h1 class="text-4xl mb-6 font-bold">💸 Prix des Cryptomonnaies</h1>
        <ul class="space-y-3">
    """
    for name, data in prices.items():
        price = data.get("eur", "N/A")
        html += f'<li class="bg-gray-800 p-4 rounded shadow-md">🔹 <strong>{name.upper()}</strong> : {price} €</li>'
    html += """
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(html)
