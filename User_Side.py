from Translator import *

Input = input("Do you want the list of languages we take? (Y/N):")
if Input == "Y":
    print("""English: en
Spanish: es
French: fr
German: de
Italian: it
Chinese: zh
Japanese: ja
Russian: ru
Portuguese: pt
Arabic: ar
Dutch: nl
Korean: ko
Turkish: tr
Swedish: sv
Polish: pl
Norwegian: no
Danish: da""")

initial_lang = input("Enter the language of the text to be converted:")
final_lang = input("Enter the language that the text is to be converted in:")
text = input("Enter the text to be converted:")
trans = Translate(text,initial_lang,final_lang)

trans.translate()
