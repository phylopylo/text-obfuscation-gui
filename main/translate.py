from bs4 import BeautifulSoup
import requests

def getDefinition(word):
    page = requests.get("https://www.google.com/search?q=define+" + word + "&oq=define+" + word + "&aqs=chrome.0.0l7j69i60.5886j1j9&sourceid=chrome&ie=UTF-8")
    soup = BeautifulSoup(page.content, "html.parser")
    for tag in soup.find_all('span'):
        if not tag.find_all():
            for word in enumerate(tag):
                if("synonyms:" in word[1]):
                    synonyms = word[1]
                    finalWord = synonyms.split()[1]
                    
                    if finalWord.endswith(","):
                        finalWord = finalWord[:-1]

                    return finalWord

def translateString(paragraph):
    programOutput = "" # Contains translatedmessage

    for word in paragraph.split():
        if not (word is None):
            translatedWord = getDefinition(word)
            if not (translatedWord is None):
                if (not (translatedWord == "")) and (not translatedWord == " "):
                    programOutput = programOutput + " " + translatedWord
                else:
                    programOutput = programOutput + " " + word
            else:    
                programOutput = programOutput + " " + word
            if word[len(word) - 1 ] == "." and word[len(word) - 2] != ")":
               programOutput = programOutput + "."
    
    
    return programOutput
                






