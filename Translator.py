class Translate:
    def __init__(self,text,in_lang,f_lang):
        self.text = text
        self.in_lang = in_lang
        self.f_lang = f_lang
    
    def translate(self):
        import requests
        url = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"
        querystring = {"langpair":self.in_lang+"|"+self.f_lang,"q":self.text,"mt":"1","onlyprivate":"0","de":"a@b.c"}

        headers = {
        "X-RapidAPI-Key": "e162fd8152msh0cf46da1ab186adp1c7ab1jsn86ae92313f36",
        "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
    }
        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()
            translation = data["responseData"]["translatedText"]
            print("Translated text:",translation)
