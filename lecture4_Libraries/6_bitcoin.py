# TODO: Revisit bitcoin.py once CoinCap v3 API access is smoother


import sys
import requests

API_KEY = "4e53f2b12f8b0706405124ada066a33cbdd14ee84247610308f0b831a6f2ed11"

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://api.coincap.io/v2/assets/bitcoin",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching data from CoinCap API")
    except (KeyError, ValueError):
        sys.exit("Invalid response data")

    total = bitcoins * price
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
