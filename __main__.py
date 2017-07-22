from argparse import ArgumentParser
from Crypto.Cipher import AES
from getpass import getpass
from sys import exit
from smtplib import SMTP
from random import randint
from os import makedirs
from os import urandom
from termcolor import colored
from csv import writer
from utils import write_same_line
from signal import signal
from signal import SIGINT

import logging

from coins.BTC import BitcoinWallet
from coins.ETH import EthereumWallet

def _exit(msg):
    logger.error(msg)
    exit(1)

def handler(signum, frame):
    print("")
    _exit("Ctrl+C pressed, exit")
signal(SIGINT, handler=handler)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

parser = ArgumentParser(description='Revain wallets generator')

parser.add_argument('-btc', help="Generate BTC (Bitcoin) wallets", default=0, type=int)
parser.add_argument('-eth', help="Generate ETH (Ethereum) wallets", default=0, type=int)
parser.add_argument('-dash', help="Generate DASH (Dash) wallets", default=0, type=int)
parser.add_argument('-xmr', help="Generate XMR (Monero) wallets", default=0, type=int)
parser.add_argument('-zcash', help="Generate ZEC (ZCash) wallets", default=0, type=int)
parser.add_argument('-d', '--dir', help="Directory to store wallets", default="_valets_{}".format(urandom(8).hex()))

if __name__ == "__main__":
    options = parser.parse_args()
    try: # Trying to init NEW directory for storing wallets
        makedirs(options.dir)
        logger.info("Wallets folder: {}/".format(colored(options.dir, "green")))
    except Exception as e:
        _exit(e)

    # ==================================================================
    # ==================== GENERATE BTC WALLETS ========================
    # ==================================================================
    if options.btc > 0:
        logger.info("Generating {} {} wallets".format(options.btc, colored("Bitcoin", "green")))
        try: # Trying to init bitcoind and check bitcoin-cli
            w = BitcoinWallet()
        except Exception as e:
            _exit(e)

        # Open file for BTC addresses and private keys
        BTC_file = open("{}/BTC.csv".format(options.dir), "a") # SAFETY IS NUMBER ONE PRIORITY !1
        BTC_writer = writer(BTC_file)
        BTC_writer.writerow(('Private_key', 'Address'))

        # Generate adresses & private keys
        for i in range(options.btc):
            address = w.get_address()
            private_key = w.get_private_key(address)
            BTC_writer.writerow((private_key, address))
            write_same_line("New {} address: {}".format(colored("Bitcoin", "green"), address))

        print ("")
        BTC_file.close()

        logger.info("{} {} addresses generated successfully".format(options.btc, colored("Bitcoin", "green")))

    # ==================================================================
    # ==================== GENERATE ETH WALLETS ========================
    # ==================================================================
    if options.eth > 0:
        logger.info("Generating {} {} wallets".format(options.eth, colored("Ethereum", "green")))
        try: # Checking all stuff works correct
            w = EthereumWallet()
        except Exception as e:
            _exit(e)

        # Open file for BTC addresses and private keys
        ETH_file = open("{}/ETH.csv".format(options.dir), "ab") # SAFETY IS NUMBER ONE PRIORITY !1
        ETH_writer = writer(ETH_file, quotechar = "'")
        ETH_writer.writerow(('Passphase', 'Address', 'Keystore'))

        # Generate adresses & private keys
        for i in range(options.eth):
            passphase = urandom(16).hex()
            address = w.get_address(passphase)
            keystore = w.get_keystore_file(address)
            ETH_writer.writerow((passphase, address, keystore))
            write_same_line("New {} address: {}".format(colored("Ethereum", "green"), address))

        print ("")
        ETH_file.close()

        logger.info("{} {} addresses generated successfully".format(options.eth, colored("Ethereum", "green")))
