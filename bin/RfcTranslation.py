# -*- coding: utf-8 -*-
import sys
import re
import codecs
import mechanize


# Exciteを使用する場合の取り込み
#from ExciteTranslater import *
#Translater = ExciteTranslater()

# Bingを使用する場合
#from BingTranslater import *
#Translater = BingTranslater()

#sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
#sys.stdout = codecs.EncodedFile(sys.stdout, 'utf_8')

class RfcTranslation():
    def __init__(self, translater):
        self.translater = translater
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

            # ページの最終行を検出
            if re.search( '\[Page [0-9]+\]$', line ):
                #if( headChack(line, 'Lonnfors, et al.')):
                lines.pop()
                lines.pop()
                lines.pop()
                cnt = 4
                continue

            lines.append(line)

        self.rfc_lines = lines

    def start(self):
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

                dst = self.translater.start(text)
                print dst

                #print text+'\n'
                self.outFild.write(text+'\r\n')
                self.outFild.write(dst+'\r\n')

                text = ''
                end = False
                continue

if __name__ == '__main__':
    # Exciteを使用する場合の取り込み
    from ExciteTranslater import *
    rfc = RfcTranslation(ExciteTranslater())

    # Bingを使用する場合
    #from BingTranslater import *
    #rfc = RfcTranslation(BingTranslater())
    
    rfc.pageMarg('rfc5262.txt')
    rfc.start()

