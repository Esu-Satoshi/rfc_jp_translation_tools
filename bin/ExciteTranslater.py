# -*- coding: utf-8 -*-
import sys
import re
import codecs
import mechanize
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
#sys.stdout = codecs.EncodedFile(sys.stdout, 'utf_8')
    

class ExciteTranslater():
    '''
    Exciteの翻訳ページを使用して英語から日本語へ
    翻訳をするためのクラス。
    
    startで翻訳を行う。
    '''
    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.open('http://www.excite.co.jp/world/english/')

    def beforeTextCnv(self, text):
        ''' 翻訳しやすいように文字列を操作する '''

        text = text.replace('MUST NOT', 'must not')
        text = text.replace('MUST', 'must')
        text = text.replace('REQUIRED', 'required')
        text = text.replace('SHALL NOT', 'shall not')
        text = text.replace('SHALL', 'shall')
        text = text.replace('SHOULD NOT', 'should not')
        text = text.replace('SHOULD', 'should')
        text = text.replace('RECOMMENDED', 'recommended')
        text = text.replace('MAY', 'may')
        text = text.replace('OPTIONAL', 'optional')
        
        return text
    
    def start(self, text):
        br = self.browser

        br.select_form(name="formTrans")
        br["before"] = self.beforeTextCnv(text)

        res2 = br.submit()
        f = br.global_form()
        after_text = f["after"]
        #print type(f["after"])

        #after_text = unicode(after_text, encoding='utf-8')

        return after_text


if __name__ == '__main__':

    test_data = "Whereas Ninja Scouting is passive in nature, with the Scout staying hidden and motionless, Active Scouting requires constant movement and is much more aggressive in nature. It is similar to Half Court Scouting but can occur anywhere on the battlefield. The goal is to keep enemy tanks lit up long enough for allied Arty or tanks to take them out. Techniques vary from peeking around corners or over ridgelines to racing around full throttle lighting up enemy as you zip about. As in most Spotting forms of Scouting, remember you are not the damage dealer - your team mates are."
    
    Translater = ExciteTranslater()
    print Translater.start(test_data)


