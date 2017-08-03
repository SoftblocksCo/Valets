# Valets - simple cryptocurrency wallets generator
Written in Python 3. Made with love inside the [Revain](https://revain.org) company.

## What is it?
Данный проект позволяет автоматически создавать тысячи адресов для 12 различных криптовалют. В добавок, все адреса автоматически индексируются клиентами каждой криптовалюты и можно использовать их RPC API для выяснения баланса, списка транзакций и так далее.

![General scheme](https://image.ibb.co/daDj2F/Payments.png)

## ⚠️ Warning ⚠️
**Не рекомендуется использовать Valets в реальных целях, на данный момент проект не протестирован должным образом.**

## Supported currencies
| Name (Coinmarketcap link)                | Status    | Volume (24h)    | Website                            | For developers                           |
| ---------------------------------------- | --------- | --------------- | ---------------------------------- | ---------------------------------------- |
| Bitcoin ([link](https://coinmarketcap.com/currencies/bitcoin/)) | **Ready** | 1.000.000.000 $ | https://bitcoin.org/               | [Bitcoin-cli](https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list) |
| Bitcoin cash ([link](https://coinmarketcap.com/currencies/bitcoin-cash/)) | In dev    | 360.000.000 $   | https://www.bitcoincash.org/       | [Bitcoin-cli](https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list) |
| Ethereum ([link](https://coinmarketcap.com/currencies/ethereum/)) | **Ready** | 785.000.000 $   | https://www.ethereum.org/          | [Geth](https://github.com/ethereum/go-ethereum/wiki/Managing-your-accounts) |
| Ethereum classic ([link](https://coinmarketcap.com/currencies/ethereum-classic/)) | **Ready** | 87.000.000 $    | https://ethereumclassic.github.io/ | [Geth-classic](https://github.com/ethereumproject/go-ethereum/releases) |
| Litecoin ([link](https://coinmarketcap.com/currencies/litecoin/)) | **Ready** | 119.000.000 $   | https://litecoin.com/              | [Litecoin-cli](https://litecoin.info/Litecoin_API) |
| Dash ([link](https://coinmarketcap.com/currencies/dash/)) | **Ready** | 23.000.000 $    | https://www.dash.org/              | [Dash-cli](https://dashpay.atlassian.net/wiki/display/COMMUNITY/Dash+Command-line+arguments) |
| Zcash ([link](https://coinmarketcap.com/currencies/zcash/)) | In dev    | 27.000.000 $    | https://z.cash/                    | [Zcash-cli](https://z.cash/download.html) |
| Reddcoin ([link](https://coinmarketcap.com/currencies/reddcoin/)) | In dev    | 970.000 $       | http://www.reddcoin.com/           | [Reddcoin-cli](https://www.reddcoin.com/#Wallets) |
| Namecoin ([link](https://coinmarketcap.com/currencies/namecoin/)) | In dev    | 145.000 $       | https://www.namecoin.org/          | [Namecoin-cli](https://wiki.namecoin.info/index.php?title=Install_and_Configure_Namecoin#3_Run_Namecoin) |
| Peercoin ([link](https://coinmarketcap.com/currencies/peercoin/)) | In dev    | 340.000 $       | http://www.peercoin.net/           | [Peercoind](https://github.com/peercoin/peercoin/wiki/Installation) |
| Dogecoin ([link](https://coinmarketcap.com/currencies/dogecoin/)) | In dev    | 5.000.000 $     | http://dogecoin.com/               | [Dogecoin-cli](https://github.com/dogecoin/dogecoin/releases) |
| Emercoin ([link](https://coinmarketcap.com/currencies/emercoin/)) | In dev    | 200.000 $       | http://emercoin.com/               | [Emercoin-cli](https://emercoin.com/EMERCOIND) |

## Usage
Все инструкции написаны для использования проекта из под Linux (Ubuntu).

### Clone & install dependencies
```
sudo apt-get update
sudo apt-get install virtualenv git python-dev python3 python3-pip

git clone https://github.com/Revain/Valets
cd Valets/
virtualenv --python python3 --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
```

### Install and launch third party apps
Valets использует оригинальные клиенты для каждой криптовалюты. Поэтому для генерации кошельков нужно предварительно установить и запустить клиенты для тех валют, которыми вы собираетесь пользоваться.

#### Bitcoin
```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt update
sudo apt install bitcoind

bitcoind -daemon # Run bitcoind
```

#### Ethereum
```bash
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum

geth --rpc --rpcaddr "127.0.0.1" --rpcapi "admin,debug,miner,shh,txpool,personal,eth,net,web3" console # Run
```

#### Ethereum classic

```bash
wget https://github.com/ethereumproject/go-ethereum/releases/download/v3.5.86/geth-classic-linux-v3.5.0.86-db60074.tar.gz
mv geth geth-clasic
sudo cp geth-classic /usr/bin # Make geth-classic systemwide available

geth-classic --rpc --rpcaddr "127.0.0.1" --rpcapi "admin,debug,miner,shh,txpool,personal,eth,net,web3" --port 30304 --rpcport 8546 console # Running on non-typical ports (30304 and 8546) for the purpose of collision avoidane with geth
```

#### Dash

```bash
wget https://www.dash.org/binaries/dashcore-0.12.1.5-linux64.tar.gz # https://www.dash.org/wallets/#linux
tar xfz dashcore-0.12.1.5-linux64.tar.gz
cd dashcore-0.12.1/bin
sudo cp * /usr/bin # Make binaries systemwide available

dashd -daemon # Run
```

#### Litecoin

```bash
wget https://download.litecoin.org/litecoin-0.14.2/linux/litecoin-0.14.2-x86_64-linux-gnu.tar.gz
tar xzf litecoin-0.14.2-x86_64-linux-gnu.tar.gz
cd litecoin-0.14.2/bin/
sudo cp * /usr/bin # Make binaries systemwide available

litecoind -daemon # Run
```

#### Reddcoin

```bash
wget https://github.com/reddcoin-project/reddcoin/releases/download/v2.0.0.0/reddcoin-2.0.0.0-linux.tar.gz
tar xzf reddcoin-2.0.0.0-linux.tar.gz
cd reddcoin-2.0.0.0-linux/bin/64/
sudo mv * /usr/bin # Make binaries systemwide available
```

#### ZCash

```bash
sudo apt-get install apt-transport-https
wget -qO - https://apt.z.cash/zcash.asc | sudo apt-key add -
echo "deb [arch=amd64] https://apt.z.cash/ jessie main" | sudo tee /etc/apt/sources.list.d/zcash.list
sudo apt-get update
sudo apt-get install zcash
```

#### Peercoin

```bash

```

#### Namecoin

```bash
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/p_conrad:/coins/xUbuntu_16.04/ /' > /etc/apt/sources.list.d/namecoin.list"
wget -nv http://download.opensuse.org/repositories/home:p_conrad:coins/xUbuntu_16.04/Release.key -O Release.key
sudo apt-key add - < Release.key
sudo apt-get update
sudo apt-get install namecoin
```

#### Emercoin

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv B58C58F4
sudo add-apt-repository 'deb http://download.emercoin.com/ubuntu xenial emercoin'
sudo apt-get update
sudo apt-get install emercoin
```

#### Bitcoin cash

```bash

```

#### Dogecoin

```bash
wget https://github.com/dogecoin/dogecoin/releases/download/v1.10.0/dogecoin-1.10.0-linux64.tar.gz
cd dogecoin-1.10.0/bin
sudo mv * /usr/bin
```

### Run Valets

```bash
$ python Valets/ -c BTC 1000 -c LTC 1000 -c ETH 1000 -c ETC 2000 -a PICK_YOUR_NICKNAME
```