import time
import random
import search_company_agent
import export_agent
import requests
from bs4 import BeautifulSoup

print("リクナビエージェント検索中(2000件前後予想:7.0h)")

# 新シートの作成
d_today = export_agent.createsheet()

# 該当企業の読み込み（別ファイルで取得した方がいいかも）ここも含めてループに組み込む
idlist = search_company_agent.getidlist()
i=1

for id_num in idlist:
    i += 1
    # 出力変数の初期化
    company,address,url,amount,employees = "","","","",""

    ur = "https://next.rikunabi.com" + id_num
    r = requests.get(ur)    

    # ページ内容の取得と解析
    soup = BeautifulSoup(r.content, "html.parser")

    # 企業名取得
    company = soup.find("p",class_ = "rnn-offerInfoHeader__text rnn-textM").get_text()

    # 企業情報該当テーブルの特定
    table_tr = soup.find("div",{"class":"rnn-group rnn-group--xm js-cmpnyInfo"})
  
# 表の形式がtableの形の場合
    rows = table_tr.findAll("tr")
    # 欲しい情報を文字列検索しながら変数に代入
    for item in rows:
        if "事業所" in item.text:
            address = item.find("td").text.strip()
        if "URL" in item.text:
            url = item.find("td").text.strip()
        if "資本金" in item.text:
            amount = item.find("td").text.strip()
        if "従業員数" in item.text:
            employees = item.find("td").text.strip()

    # sheet出力
    export_agent.exportsheet(i,company,address,url,amount,employees,d_today)

    # 出力
    # print("企業名:",company)
    # print("住所:",address)
    # print("URL:",url)
    # print("売り上げ:",amount)
    # print("従業員数:",employees)
    # print()
    time.sleep(random.randint(1,3))