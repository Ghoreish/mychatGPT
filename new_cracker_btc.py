from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic
import time
import os
import requests
import _thread


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
    os.system('rm -r ~/.bitcoinlib/Wallets/mywallet')
    passphrase = Mnemonic().generate(strength=128)

    wallname = 'a' + str(time.time()).replace('.', '')
    w = Wallet.create(wallname, witness_type='segwit', keys=passphrase, network='bitcoin')

    WalletKeys = (w.get_keys(number_of_keys=1))

    addr = WalletKeys[0].address
    if check_amount(str(addr)) == True:
        print(passphrase)
        print(addr)
        f = open('keys.txt', 'a')
        f.write(str(addr) + ' ' + str(passphrase) + '\n')
        f.close()

for i in range(20):
    _thread.start_new_thread(do, ())

while True:
    pass
