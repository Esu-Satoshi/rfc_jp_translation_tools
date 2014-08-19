import azure_translate_api

client = azure_translate_api.MicrosoftTranslatorClient('RFC_Translation_8989',  # make sure to replace client_id with your client id
                                                       'MtBFsDjvYSFlQDqnCljQ4xsiiTCY9q1hsgCe1fX31j8=') # replace the client secret with the client secret for you app.
print client.TranslateText('Good morning my lovely french friends!', 'en', 'fr')
print client.TranslateText('Good morning my lovely french friends!', 'en', 'fr')
