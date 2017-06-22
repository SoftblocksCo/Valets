# Valets - simple cryptocurrency wallets generator
Written in Python 3. Made with love inside the [Revain](https://revain.org) company.

## What is it?
Imagine that you have an application, with allows users to work with cryptocurrencies. So you need to give every user it's own address for deposits and withdraw.

## Features:
- Generate thousands of wallets for:
  - [Bitcoin](https://bitcoin.org/en/)
  - [Ethereum](https://www.ethereum.org/)
  - [Zcash](https://z.cash/)
  - [Monero](https://getmonero.org/home)
  - [Dash](https://www.dash.org/)
- Encrypt the private keys with the strongest cyphers (AES 128, DES coming soon)
- Use pass phrases for private key encryption
- You can generate, for example, 3 pass phrases for CEO, CTO and escrow. So private keys can be decrypted only after all 3 keys were given.

## Usage
### Install and launch third party apps
Valets use original cryptocurrency's clients, so you won't be able to use this app without installing bitcoind for Bitcoin, geth for Ethereum and so on.

#### Bitcoin
Installation guide - [here](https://askubuntu.com/questions/41001/how-do-i-install-bitcoin-in-ubuntu).

```
sudo apt install software-properties-common
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt update
sudo apt install bitcoind
```

Run bitcoin server:

```
bitcoind -daemon
```


#### Ethereum
Installation guide - [here](https://github.com/ethereum/go-ethereum/wiki/Installing-Geth)

```
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
```

#### Zcash
#### Monero
#### Dash
### Generate raw wallets
### Generate encrypted wallets

## Road map
- Multisig (unlock private keys with only a part of all pass phrases, e.g. 5 pass phrases from 7)
