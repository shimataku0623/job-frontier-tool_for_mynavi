# coding: utf-8

############### cx_Freeze 用セットアップファイル ##########
# コマンドライン上で python setup.py buildとすると、exe化　#
# Mac用のAppを作成するには、buildをbdist_macとする        #
######################################################
 
import sys, os
from cx_Freeze import setup, Executable

#個人的な設定（コマンドライン上でファイルをぶっこみたい）
file_path = input("アプリ化したいpy：")

#TCL, TKライブラリのエラーが発生する場合に備え、以下を設定
#参考サイト：http://oregengo.hatenablog.com/entry/2016/12/23/205550
if sys.platform == "win32":
    base = None # "Win32GUI" ←GUI有効
    #Windowsの場合の記載　それぞれの環境によってフォルダの数値等は異なる
    # os.environ['TCL_LIBRARY'] = "C:\\Users\\[ユーザー名]\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
    # os.environ['TK_LIBRARY'] = "C:\\Users\\[ユーザー名]\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"
else:
    base = None # "Win32GUI"

#importして使っているライブラリを記載
packages = []

#importして使っているライブラリを記載（こちらの方が軽くなるという噂）
includes = [
    "time",
    "random",
    "gspread",
    "json",
    "datetime",
    "bs4",
    "sys",
    "os",
    "requests",
]

#excludesでは、パッケージ化しないライブラリやモジュールを指定する。
"""
numpy,pandas,lxmlは非常に重いので使わないなら、除く。（合計で80MBほど）
他にも、PIL(5MB)など。
"""
excludes = [
    "pandas",
    "lxml"
]

##### 細かい設定はここまで #####

#アプリ化したい pythonファイルの指定触る必要はない
exe = Executable(
    script = file_path,
    base = base
)
 
# セットアップ
setup(name = 'job_frontier',
      options = {
          "build_exe": {
              "packages": packages, 
              "includes": includes, 
              "excludes": excludes,
          }
      },
      version = '0.1',
      description = 'converter',
      executables = [exe])