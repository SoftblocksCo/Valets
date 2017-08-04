from configparser import ConfigParser
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
from importlib import import_module

from api.rpc_bitcoin import Bitcoin_like_wallet
from api.rpc_ethereum import Ethereum_like_wallet

import logging

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

# General Valets options
parser.add_argument('-d', '--dir', help="Directory to store wallets", default="_valets_{}".format(urandom(8).hex()))
parser.add_argument('-c', '--coins', help="Specify coins for wallets generation, e.g. '-c BTC 100'", required=True, type=str, nargs='+', action='append')
parser.add_argument('-i', '--ini', help="Path to the .ini file", default="./Valets/config.ini")

if __name__ == "__main__":
    options = parser.parse_args()

    parser = ConfigParser()
    parser.read(options.ini)

    try: # Trying to init NEW directory for storing wallets
        makedirs(options.dir)
        logger.info("Wallets folder: {}/".format(options.dir))
    except Exception as e:
        _exit(e)

    for coin, wallets_amount in options.coins: # Iterate on every coin
        wallets_amount = int(wallets_amount)

        logger.info("Generating {} {} wallets".format(wallets_amount, coin))

        full_wallet_file = open("{}/full_{}.csv".format(options.dir, coin), 'a')
        full_wallet_writer = writer(full_wallet_file)

        save_wallet_file = open("{}/save_{}.csv".format(options.dir, coin), 'a')
        save_wallet_writer = writer(save_wallet_file)

        if coin in ['ETH', 'ETC']:
            full_wallet_writer.writerow(('Passphase', 'Address', 'Keystore'))
            save_wallet_writer.writerow(('Passphase', 'Address', 'Keystore'))
            w = Ethereum_like_wallet(name=coin, parser=parser)
        else:
            full_wallet_writer.writerow(('Private_key', 'Address'))
            save_wallet_writer.writerow(('Private_key', 'Address'))
            w = Bitcoin_like_wallet(name=coin, parser=parser)

        # Generate adresses & private keys
        for i in range(1, wallets_amount + 1):
            if coin in ['ETH', 'ETC']: # Ethereum, Ethereum classic
                passphase = urandom(16).hex()
                address = w.get_address(passphase)
                keystore = w.get_keystore_file(address)

                full_wallet_writer.writerow((passphase, address, keystore)) # Store full wallet info
                save_wallet_writer.writerow(('passphase', address, 'keystore')) # Store save wallet info
            else: # Bitcoin, Litecoin, Dash, Dogecoin, ....
                address = w.get_address()
                private_key = w.get_private_key(address)

                full_wallet_writer.writerow((private_key, address)) # Store full wallet info
                save_wallet_writer.writerow(('private_key', address)) # Store save wallet info

            write_same_line("New {} address ({}): {}".format(coin, i, address))

        print ("") # Because 'write_same_line' don't use \n

        full_wallet_file.close()
        save_wallet_file.close()

        logger.info("{} {} addresses generated successfully".format(wallets_amount, coin))
