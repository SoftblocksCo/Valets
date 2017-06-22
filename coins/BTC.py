from bitcoin import sha256
from bitcoin import privtopub
from bitcoin import pubtoaddr
from random import SystemRandom

class BitcoinWallet():
    def __init__(self):
        pass

    def get_private_key(self):
        return sha256(str(SystemRandom().randint(1, 115792089237316195423570985008687907852837564279074904382605163141518161494337)))

    def get_address(self, private_key):
        return pubtoaddr(privtopub(private_key))
