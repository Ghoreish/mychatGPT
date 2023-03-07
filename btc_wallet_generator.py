import os
import binascii
from mnemonic import Mnemonic
from bip32utils import BIP32Key

# Generate a random 128-bit seed
seed = os.urandom(16)
# Convert the seed to a BIP39 mnemonic phrase
mnemonic = Mnemonic("english").to_mnemonic(seed)
print('Mnemonic:', mnemonic)

# Create a hierarchical deterministic wallet from the seed
wallet = BIP32Key.fromEntropy(seed)
# Derive the first receiving address from the wallet
address = wallet.ChildKey(0).ChildKey(0).Address()
print('Address:', address)
