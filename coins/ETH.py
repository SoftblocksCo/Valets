from web3 import Web3
from web3 import KeepAliveRPCProvider
from glob import glob
from os.path import expanduser

class EthereumWallet():
    def __init__(self, ethereum_path='/'.join([expanduser("~"), '.ethereum'])):
        self.ethereum_pass = ethereum_path
        # DON'T FORGET TO LAUNCH GETH
        self.web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8545')) # connect to RPC
        self.web3.eth.accounts # Just checking

    def get_address(self, passphase):
        return self.web3.personal.newAccount(passphase)

    def get_keystore_file(self, address):
        cropped_address = address.split('0x')[1]
        keystore_file_path = glob('/'.join([self.ethereum_pass, '/keystore/*{}'.format(cropped_address)]))[0]

        with open(keystore_file_path, 'r') as keystore_file:
            keystore_content = keystore_file.read()

        return keystore_content
