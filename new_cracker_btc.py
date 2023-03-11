from bitcoinlib.wallets import Wallet
import time
import os

os.system('rm -r ~/.bitcoinlib/Wallets/mywallet')
passphrase = 'gesture reform utility resource moral snap deputy enact catalog what want false'

wallname = str(time.time()).replace('.', '')
w = Wallet.create("Wallet1", witness_type='segwit', keys=passphrase, network='bitcoin')

WalletKeys = (w.get_keys(number_of_keys=1))

print(WalletKeys[0].address)
