import gspread
import json
import datetime
import time

#基本設定
#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。def内に入れる必要ある？
from oauth2client.service_account import ServiceAccountCredentials

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('job-search-tool-275805-f8d51c89dd6c.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = '1pUWGAsSa11nn0XpMvhDMWATO3ztasDsg9Ud9LNuXwOs'

#共有設定したスプレッドシートのシート1を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)

def createsheet():
    d_today = str(datetime.date.today()) + "_rikunavi_agent"
    workbook.add_worksheet(title=d_today, rows=10000, cols=10)
    return d_today

def exportsheet(i,company,address,url,amount,employees,d_today):
    
    worksheet = workbook.worksheet(d_today)
    
    # 見出し
    if i==2:
        header_list = ["会社名","住所","URL","資本金","社員数"]
        worksheet.append_row(header_list)

        # worksheet.update_cell(1, 1, "会社名")
        # worksheet.update_cell(1, 2, "住所")
        # worksheet.update_cell(1, 3, "URL")
        # worksheet.update_cell(1, 4, "売上高")
        # worksheet.update_cell(1, 5, "社員数")

    # データ更新
    time.sleep(10)
    column_list = [company,address,url,amount,employees]
    worksheet.append_row(column_list)