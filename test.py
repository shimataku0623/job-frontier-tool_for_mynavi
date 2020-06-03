import time
import random
import search_company
import export
import requests
import loop_dif
import re
from bs4 import BeautifulSoup

# #初期化
# idlist = list()

# # 取得URL
# urlnum = 1
# # url = "https://next.rikunabi.com/area_wp0313100000/jb0505020000/crn" + str(urlnum) + ".html"
# # r = requests.get(url)
# # soup = BeautifulSoup(r.content, "html.parser")

# # # 企業別ページをcompanyidに詰める
# # companyid = soup.findAll("a", class_="rnn-linkText rnn-linkText--black")
# # time.sleep(2)

# # for id in companyid:
# #     idurl = id.get("href")
# #     idlist.append(idurl[0:22])

# #     # id.attrs['href'][0:22]
# #     # idlist.append(id)
# # print(idlist)

# ur = "https://next.rikunabi.com/company/cmi2603257001/"
# r = requests.get(ur)

# # ページ内容の取得と解析
# soup = BeautifulSoup(r.content, "html.parser")


# # 出力変数の初期化
# company,address,url,amount,employees = "","","","",""
# company = soup.find_all(typeof = "v:Breadcrumb")[3].get_text()

# # 企業名取得
# #companyclass = soup.find(class_ = "rnn-breadcrumb")
# #company = soup.find_all(typeof = "v:Breadcrumb")[3].get_text()
# table_tr = soup.find("table",{"class":"rnn-detailTable"})

# #company = companyclass.select('ul > li:nth-of-type(4)').get_text()
# #companyclass = soup.find('script',type="application/ld+json") #.find(typeof = "rnn-breadcrumb")

# # 表の形式がtableの形の場合
# if table_tr:
#     rows = table_tr.findAll("tr")
#     # 欲しい情報を文字列検索しながら変数に代入
#     for item in rows:
#         if "事業所" in item.text:
#             address = item.find("td").text.strip()
#         if "URL" in item.text:
#             url = item.find("td").text.strip()
#         if "資本金" in item.text:
#             amount = item.find("td").text.strip()
#         if "従業員数" in item.text:
#             employees = item.find("td").text.strip()

# # 出力
# print("企業名:",company)
# print("住所:",address)
# print("URL:",url)
# print("売り上げ:",amount)
# print("従業員数:",employees)

# # print(table_tr)


url = "https://next.rikunabi.com/area_wp0313100000/jb0505020000/crn101.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

#periodterm = soup.findAll("div", class_="js-abScreen__postDate")

# # data-ntype="1"の求人広告だけを取得（ネクスト専用求人）
# companypage = soup.findAll(attrs={"data-ntype": "1"})
# print(companypage)

# # 企業別ページをcompanyidに詰める
# companyid = soup.findAll("a", class_="rnn-linkText rnn-linkText--black")
# time.sleep(2)

# for id in companyid:
#     idurl = id.get("href")
#     # print(id)
#     # print()



idlist = set()

# 取得URL
url = "https://next.rikunabi.com/area_wp0313100000/jb0505020000/crn101.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# 企業広告全体をcompanypageに、その中に含まれるURLをcompanyidに詰める
companyid = soup.find_all("a",href=re.compile("^/company"),class_="rnn-linkText rnn-linkText--blue rnn-m-l-sm")
# companypage = soup.find_all("a",class_="rnn-linkText rnn-linkText--black",href=re.compile("^/company"))
#attrs={"data-ntype": "1"}
#companyid = companypage.findAll("a", class_="rnn-linkText rnn-linkText--black")
time.sleep(2)

for id in companyid:
    idlist.add(id.get("href"))
        
print(idlist)