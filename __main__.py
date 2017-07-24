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
from coins.LTC import LitecoinWallet
from coins.ETC import EthereumClassicWallet

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
parser.add_argument('-etc', help="Generate ETC (Ethereum classic) wallets", default=0, type=int)
parser.add_argument('-ltc', help="Generate LTC (Litecoin) wallets", default=0, type=int)
parser.add_argument('-dash', help="Generate DASH (Dash) wallets", default=0, type=int)
parser.add_argument('-xmr', help="Generate XMR (Monero) wallets", default=0, type=int)
parser.add_argument('-zcash', help="Generate ZEC (ZCash) wallets", default=0, type=int)
parser.add_argument('-d', '--dir', help="Directory to store wallets", default="_valets_{}".format(urandom(8).hex()))

if __name__ == "__main__":
    options = parser.parse_args()
    try: # Trying to init NEW directory for storing wallets
        makedirs(options.dir)
        logger.info("Wallets folder: {}/".format(options.dir))
    except Exception as e:
        _exit(e)

    if options.btc > 0: # Generate Bitcoin wallets
        logger.info("Generating {} {} wallets".format(options.btc, "Bitcoin"))
        try: # Trying to init bitcoind and check bitcoin-cli
            w = BitcoinWallet()
        except Exception as e:
            _exit(e)

        with open("{}/BTC.csv".format(options.dir), "a") as BTC_file:
            BTC_writer = writer(BTC_file)
            BTC_writer.writerow(('Private_key', 'Address'))

            # Generate adresses & private keys
            for i in range(options.btc):
                address = w.get_address()
                private_key = w.get_private_key(address)
                BTC_writer.writerow((private_key, address))
                write_same_line("New {} address: {}".format("Bitcoin", address))
            print ("")

        logger.info("{} {} addresses generated successfully".format(options.btc, "Bitcoin"))

    if options.eth > 0: # Generate Ethereum wallets
        logger.info("Generating {} {} wallets".format(options.eth, "Ethereum"))
        try: # Checking all stuff works correct
            w = EthereumWallet()
        except Exception as e:
            _exit(e)

        with open("{}/ETH.csv".format(options.dir), "a") as ETH_file:
            ETH_writer = writer(ETH_file, quotechar = "'")
            ETH_writer.writerow(('Passphase', 'Address', 'Keystore'))

            # Generate adresses & private keys
            for i in range(options.eth):
                passphase = urandom(16).hex()
                address = w.get_address(passphase)
                keystore = w.get_keystore_file(address)
                ETH_writer.writerow((passphase, address, keystore))
                write_same_line("New {} address: {}".format("Ethereum", address))
            print ("")

        logger.info("{} {} addresses generated successfully".format(options.eth, "Ethereum"))

    if options.ltc > 0: # Generate Litecoin wallets
        logger.info("Generating {} {} wallets".format(options.btc, "Litecoin"))
        try: # Trying to init litecoind and check litecoin-cli
            w = LitecoinWallet()
        except Exception as e:
            _exit(e)

        with open("{}/LTC.csv".format(options.dir), "a") as LTC_file:
            LTC_writer = writer(LTC_file)
            LTC_writer.writerow(('Private_key', 'Address'))

            # Generate adresses & private keys
            for i in range(options.ltc):
                address = w.get_address()
                private_key = w.get_private_key(address)
                LTC_writer.writerow((private_key, address))
                write_same_line("New {} address: {}".format("Litecoin", address))
            print ("")

        logger.info("{} {} addresses generated successfully".format(options.ltc, "Litecoin"))

    if options.etc > 0: # Generate Ethereum-classic wallets
        logger.info("Generating {} {} wallets".format(options.etc, "Ethereum-classic"))
        try: # Checking all stuff works correct
            w = EthereumClassicWallet()
        except Exception as e:
            _exit(e)

        with open("{}/ETC.csv".format(options.dir), "a") as ETC_file:
            ETC_writer = writer(ETC_file, quotechar = "'")
            ETC_writer.writerow(('Passphase', 'Address', 'Keystore'))

            # Generate adresses & private keys
            for i in range(options.etc):
                passphase = urandom(16).hex()
                address = w.get_address(passphase)
                keystore = w.get_keystore_file(address)
                ETC_writer.writerow((passphase, address, keystore))
                write_same_line("New {} address: {}".format("Ethereum-classic", address))
            print ("")

        logger.info("{} {} addresses generated successfully".format(options.etc, "Ethereum-classic"))
