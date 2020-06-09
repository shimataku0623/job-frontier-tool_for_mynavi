#-*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty, ListProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
import japanize_kivy
import subprocess

# デフォルトに使用するフォントを変更する
#resource_add_path('./fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


class TextWidget(Widget):
    text  = StringProperty()
    color = ListProperty([1,1,1,1])

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = '実行したいサイトを選択してください'

    def commonexec(self):
        self.text = '実行中暫し待たれよ'

    def buttonClicked(self):
        # with open('rikunavi.command') as fp:
        #     cp = subprocess.Popen(['bash rikunavi.command'], stdin=fp,text=True, cwd="/Users/shimataku/workspace/job-frontier-tool_for_mynavi",shell = True)
        #     result = cp.communicate()
        #     self.text = result
        #result0なら
        self.text = 'doda実行完了'
        #TextWidget.commonexec(self)


    def buttonClicked2(self):
        TextWidget.commonexec(self)
        with open('rikunavi.command') as fp:
            cp = subprocess.Popen(['bash rikunavi.command'], stdin=fp,text=True, cwd="/Users/shimataku/workspace/job-frontier-tool_for_mynavi",shell = True)
            result = cp.communicate()
            self.text = result
        #result0なら
        self.text = 'リクナビ実行完了'

    def buttonClicked3(self):
        # with open('rikunavi.command') as fp:
        #     cp = subprocess.Popen(['bash rikunavi.command'], stdin=fp,text=True, cwd="/Users/shimataku/workspace/job-frontier-tool_for_mynavi",shell = True)
        #     result = cp.communicate()
        #     self.text = result
        self.text = 'リクナビエージェント実行完了'

    def buttonClicked4(self):
        # with open('rikunavi.command') as fp:
        #     cp = subprocess.Popen(['bash rikunavi.command'], stdin=fp,text=True, cwd="/Users/shimataku/workspace/job-frontier-tool_for_mynavi",shell = True)
        #     result = cp.communicate()
        #     self.text = result
        self.text = 'green実行完了'

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = '起動アプリ切り替えるくん'

if __name__ == '__main__':
    TestApp().run()


