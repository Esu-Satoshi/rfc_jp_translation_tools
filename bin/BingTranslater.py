# -*- coding: utf-8 -*-
import sys,os
sys.path.append('./azure_translate_api')
#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '.\azure_translate_api')

import codecs
import azure_translate_api
import ConfigParser

inifile = ConfigParser.SafeConfigParser()
inifile.read("./config.ini")

client_id = inifile.get('BingTranslater','client_id')
client_secret = inifile.get('BingTranslater','client_secret')

class BingTranslater():
    '''
    Exciteの翻訳ページを使用して英語から日本語へ
    翻訳をするためのクラス。
    
    startで翻訳を行う。
    '''
    def __init__(self):
        self.client = azure_translate_api.MicrosoftTranslatorClient(client_id, client_secret)

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
        after_text = self.client.TranslateText(self.beforeTextCnv(text), 'en', 'ja')
        return after_text.strip("\"﻿\"")

if __name__ == '__main__':

    test_data = "Whereas Ninja Scouting is passive in nature, with the Scout staying hidden and motionless, Active Scouting requires constant movement and is much more aggressive in nature. It is similar to Half Court Scouting but can occur anywhere on the battlefield. The goal is to keep enemy tanks lit up long enough for allied Arty or tanks to take them out. Techniques vary from peeking around corners or over ridgelines to racing around full throttle lighting up enemy as you zip about. As in most Spotting forms of Scouting, remember you are not the damage dealer - your team mates are."
    
    Translater = BingTranslater()
    print Translater.start(test_data)
