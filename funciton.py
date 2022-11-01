# -*- coding: utf-8 -*-  
import pymysql,sqlite3,time,requests
from web3 import Web3

# mysql数据库链接
sql_conn = sqlite3.connect('dev_config.sqlite3')



def get_time_now():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 代理ip
proxies = {"http": "socks5://127.0.0.1:10808","https": "socks5://127.0.0.1:10808",}
# proxies=None

#用于测试的地址列表
eth_test_address=Web3.toChecksumAddress("0x655BDcb8F1d2CeD98d521a6B8f23badd892a2D98")
bsc_test_address=Web3.toChecksumAddress("0x72b61c6014342d914470ec7ac2975be345796c2b")
polygon_test_address=Web3.toChecksumAddress("0x33c2E4d8975950fe0c04146f39794C3f00569382")
address_list=[eth_test_address,bsc_test_address,polygon_test_address]

# 发送tg消息
def send_tg_message_get(text):
    url = 'https://api.telegram.org/bot1352370684:AAHrnyW26IPupau93pfE4b3ExfdJuOfErA8/sendMessage'
    data = {'chat_id': -1001215971015,'text': text, "parse_mode": "HTML",}
    requests.get(url, data=data,proxies=proxies,timeout=10)

#eth-web3
eth_web3=Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/7906bef1634f4e24b1665f47b0e0ad6f",request_kwargs={"proxies":proxies}))
eth_web3_ropsten=Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/7906bef1634f4e24b1665f47b0e0ad6f",request_kwargs={"proxies":proxies}))
#bsc_web3
bsc_web3=Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/",request_kwargs={"proxies":proxies}))
bsc_testnet_web3=Web3(Web3.HTTPProvider("https://data-seed-prebsc-1-s1.binance.org:8545/",request_kwargs={"proxies":proxies}))
