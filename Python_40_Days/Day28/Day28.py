import translate 
import googletrans 

with open('Day27/text.txt', 'r') as f:
    sentence = f.read()
    translator = googletrans.Translator()
    res = translator.translate(sentence, dest='ja')
    print('Translate to Japanese using Googletrans lib:\n', res.text)

    translator = translate.Translator(from_lang='vi', to_lang='en')
    res = translator.translate(sentence)
    print('\nTranslate to English using Translate lib:\n', res)
