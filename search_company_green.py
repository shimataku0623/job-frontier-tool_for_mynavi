import time
import requests
import loop_dif_green
import re
from bs4 import BeautifulSoup

# ここで全て（2000件）のidを取得すればいいじゃん
# extendなら、配列が入れ子にならない
# 重複を避けたいならset使えば良さげ
def getidlist():

    #loop数の取得
    loop = loop_dif_green.getloop()

    #初期化
    idlist = set()

    for i in range(1,loop):
        # 取得URL
        urlnum = i
        url = "https://www.green-japan.com/search_key/01?case=login&key=dol06b943yhp1l61vh0n&keyword=&page=" + str(urlnum)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
    
        # photo-element
        companyid = soup.find_all("div",class_="photo-element")
       # companyid = companypage.findAll("a", class_="rnn-linkText rnn-linkText--black")
        time.sleep(2)

#/noi
        for id in companyid:
            idnum = id.attrs['style'][28:32]
            if idnum=='/noi':            
                print("---noimageのためskip---")
            else:
                idlist.add(idnum.split('/')[0])

    return idlist