# import time
# import random
# import search_company_green
# import export_green
import requests
# import loop_dif_green
# import re
# #import tkinter
from bs4 import BeautifulSoup
# import main_green

#初期化
idlist = set()

#初期ページ
target_url = "https://www.green-japan.com/search_key/01?case=login&key=dol06b943yhp1l61vh0n&keyword=&page=1"
r = requests.get(target_url)

# 初期ページ内容の取得と解析
soup = BeautifulSoup(r.content, "html.parser")
companyid = soup.find_all("div",class_="photo-element")
for id in companyid:
    idlist.add(id.attrs['style'][28:32])
    
print(idlist)