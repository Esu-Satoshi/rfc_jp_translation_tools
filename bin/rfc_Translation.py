# -*- coding: utf-8 -*-
import sys
import codecs
import mechanize
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
#sys.stdout = codecs.EncodedFile(sys.stdout, 'utf_8')
    

class ExciteTranslation():
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



def headChack(src, text):
    if( src[:len(text)] == text ):
        return True
    return False


class RFCTranslation():
    def __init__(self):
        self.exciteTranslation = ExciteTranslation()
        self.outFild = open('dst.txt', 'wb')
        
    def pageMarg(self, srcFile):
        '''
        rfcのページ区切りを解析して1枚の文章として接続する
        '''
        
        lines = []
        cnt = 0
        for line in open(srcFile):

            if( cnt > 0 ):
                cnt = cnt - 1
                continue

            if( headChack(line, 'Lonnfors, et al.')):
                lines.pop()
                lines.pop()
                lines.pop()
                cnt = 4
                continue

            lines.append(line)

        self.rfc_lines = lines

    def translation(self):
        ''' 翻訳を行う '''

        end = False
        text = ''
        for line in self.rfc_lines :
            line = line.strip()
            text = text + ' ' + line

            if( line[-1:] == '.' ): end = True
            if( line[-1:] == ':' ): end = True
            if( len(line) == 0 and text != ''): end = True

            if( end == True ):
                '''' ここを分の区切りとする '''

                dst = self.exciteTranslation.start(text)
                print dst

                #print text+'\n'
                self.outFild.write(text+'\r\n')
                self.outFild.write(dst+'\r\n')

                text = ''
                end = False
                continue

if __name__ == '__main__':

    rfc = RFCTranslation()
    rfc.pageMarg('rfc2223.txt')
    rfc.translation()

