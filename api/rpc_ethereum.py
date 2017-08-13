from web3 import Web3
from web3 import KeepAliveRPCProvider
from glob import glob
from os.path import expanduser
from time import sleep

class Ethereum_like_wallet():
    def __init__(self, name, parser):
        if name == 'ETH':
            self.ethereum_path = '/'.join([expanduser("~"), '.ethereum'])
        else:
            self.ethereum_path = '/'.join([expanduser("~"), '.ethereum-classic/mainnet'])

        self.HOST = parser.get(name, 'rpcbind')
        self.PORT = parser.get(name, 'rpcport')

        # Don't forget to launch geth of geth-classic
        self.web3 = Web3(KeepAliveRPCProvider(host=self.HOST, port=self.PORT)) # connect to RPC

    def get_address(self, passphase, sleep_sec=0):
        sleep(sleep_sec)
        return self.web3.personal.newAccount(passphase)

    def get_keystore_file(self, address, sleep_sec=0):
        sleep(sleep_sec)
        cropped_address = address.split('0x')[1]
        keystore_file_path = glob('/'.join([self.ethereum_path, 'keystore/*{}'.format(cropped_address)]))[0]

        with open(keystore_file_path, 'r') as keystore_file:
            keystore_content = keystore_file.read()

        return keystore_content
