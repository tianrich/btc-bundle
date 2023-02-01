import requests
import time

def check_wallet(wallet_address):
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{wallet_address}/balance"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['final_balance'] > 0:
            return True
    return False

def main():
    with open("generated.txt", "r") as f:
        wallets = f.readlines()
    found_wallets = []
    for wallet in wallets:
        address = wallet.strip()
        print(f"Checking wallet: {address}")
        if check_wallet(address):
            print(f"Transaction found in wallet: {address}")
            found_wallets.append(address)
        time.sleep(0.005) # 5ms delay
    with open("found.txt", "w") as f:
        for wallet in found_wallets:
            f.write(wallet + "\n")

if __name__ == "__main__":
    main()
