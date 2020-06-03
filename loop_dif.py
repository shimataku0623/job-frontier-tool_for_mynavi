import time
import requests
from bs4 import BeautifulSoup

def getloop():
    
    #初期ページ
    target_url = "https://next.rikunabi.com/area_wp0313100000/jb0505020000/crn1.html"
    r = requests.get(target_url)
    
    # 初期ページ内容の取得と解析
    soup = BeautifulSoup(r.content, "html.parser")
    
    #全体件数の取得
    search_num = soup.find("span",{"class":"js-resultCount"}).text
    int(search_num.replace(',', ''))

    #loop数の確定
    loop = -(-int(search_num) // 50)
    return loop