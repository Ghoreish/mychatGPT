import os
import binascii
from mnemonic import Mnemonic
from bip32utils import BIP32Key
import requests
import json
import _thread

n = 0


def make():
    # Generate a random 128-bit seed
    seed = os.urandom(16)
    # Convert the seed to a BIP39 mnemonic phrase
    mnemonic = Mnemonic("english").to_mnemonic(seed)

    # Create a hierarchical deterministic wallet from the seed
    wallet = BIP32Key.fromEntropy(seed)
    # Derive the first receiving address from the wallet
    address = wallet.ChildKey(0).ChildKey(0).Address()
    return (mnemonic, address)


def check_amount(x):
    r = requests.get('https://blockchain.info/q/getreceivedbyaddress/{}'.format(str(x)))
    r = r.text
    if r.isnumeric():
        if int(r) > 0:
            return True
        else:
            return False
    else:
        return False


def do():
    global n
    while True:
        words, addr = make()
        res = check_amount(addr)
        if res == True:
            print(words)
            print(address)
            print('finally..........\n\n\n')
        n += 1


for i in range(20):
    _thread.start_new_thread(do, ( ))

while True:
    if n % 1000 == 0:
        print(n)
        n += 1
