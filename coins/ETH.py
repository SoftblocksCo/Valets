from web3 import Web3
from web3 import KeepAliveRPCProvider

class EthereumWallet():
    def __init__(self):
        # DON'T FORGET TO LAUNCH GETH
        self.web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8545')) # connect to RPC
        self.web3.eth.accounts # Just checking
    def get_address(self, passphase):
        return self.web3.personal.newAccount(passphase)
