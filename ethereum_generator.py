from eth_account import Account
from mnemonic import Mnemonic

def generate():
    # Generate a random mnemonic phrase
    mnemonic = Mnemonic("english").generate(128)

    # Derive Trust Wallet address from mnemonic phrase
    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(mnemonic)
    trust_wallet_address = account.address

    return mnemonic, trust_wallet_address
