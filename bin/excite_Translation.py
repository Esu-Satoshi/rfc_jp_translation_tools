# -*- coding: utf-8 -*-
import sys
import codecs
import mechanize
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
#sys.stdout = codecs.EncodedFile(sys.stdout, 'utf_8')
    
TEXT = '''
MAY evaluate the Publication Content Rules Presence Source View and re-publish a presence document satisfying the Publication Content Rules Presence Source View.
'''
class ExciteTranslation():
    '''
    Exciteの翻訳ページを使用して英語から日本語へ
    翻訳をするためのクラス。
    
    startで翻訳を行う。
    '''
    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.open('http://www.excite.co.jp/world/english/')

    def start(self, text):
        br = self.browser

        br.select_form(name="formTrans")
        br["before"] = text

        res2 = br.submit()
        f = br.global_form()
        after_text = f["after"]
        #print type(f["after"])

        #after_text = unicode(after_text, encoding='utf-8')

        return after_text

def Textcnv( text ):
    text = text.replace('SHALL', 'shall')
    text = text.replace('MAY', 'may')
    return text



if __name__ == '__main__':

    
    ET = ExciteTranslation()

    f = open('src.txt')
    #w = open('dst.txt')
    line = f.readline()
    while line:
        print line
        print ET.start(Textcnv(line))
        line = f.readline()

    f.close()
    
    #aa = ET.start(Textcnv(TEXT))
    #print aa
        
