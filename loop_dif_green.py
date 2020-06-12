import time
import requests
from bs4 import BeautifulSoup

def getloop():
    
    # #初期ページ
    # target_url = "https://www.green-japan.com/search_key/01?case=login&key=dol06b943yhp1l61vh0n&keyword=&page=1"
    # r = requests.get(target_url)
    
    # # 初期ページ内容の取得と解析
    # soup = BeautifulSoup(r.content, "html.parser")
    
    # #全体件数の取得
    # search_num = soup.find("span",{"id":"client_count"}).text
    # int(search_num.replace(',', ''))

    # #loop数の確定
    # loop = -(-int(search_num) // 10)
    loop = 20
    return loop