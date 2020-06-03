import time
import requests
import loop_dif
import re
from bs4 import BeautifulSoup

# ここで全て（2000件）のidを取得すればいいじゃん
# extendなら、配列が入れ子にならない
# 重複を避けたいならset使えば良さげ
def getidlist():

    #loop数の取得
    loop = loop_dif.getloop()

    #初期化
    idlist = set()

    for i in range(0,loop-1):
        # 取得URL
        urlnum = 50*i +1
        url = "https://next.rikunabi.com/area_wp0313100000/jb0505020000/crn" + str(urlnum) + ".html"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
    
        # /companyから始まるURLをcompanyidに詰める(リクナビネクストに既刊掲載しているリスト)
        companyid = soup.find_all("a",href=re.compile("^/company"),class_="rnn-linkText rnn-linkText--blue rnn-m-l-sm")
       # companyid = companypage.findAll("a", class_="rnn-linkText rnn-linkText--black")
        time.sleep(2)

        for id in companyid:
            idlist.add(id.get("href"))

    return idlist