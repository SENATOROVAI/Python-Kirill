import datetime
import filecmp
import lxml
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



def collect_data(url):
    cur_time = datetime.datetime.now().strftime('%d-%m-%Y_%H_%M')
    ua = UserAgent()

    headers = {
        'Accept': "*/*",
        'User-Agent' : ua.random
    }

    response  = requests.get(url, headers=headers)
    src = response.text

    #with open("bybit.html", "w") as file:
        #file.write(src)

    
        

    soup = BeautifulSoup(src, 'lxml')
    advertiser_all = soup.find_all(class_="ant-space-item")
    print(advertiser_all)



collect_data("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=")