from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def SafeQuestions(listOfFlags,Questions):
    
    for word in listOfFlags:
        if word in Questions:#Not safe!
            return False
    return True #No flag word found


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def checkURL(url):
    opener = AppURLopener()
    html = opener.open(url).read()
    stringWithQuestions = re.compile(r'([A-Z][^\?]*[\?])', re.M)

    strg1 =""
   # with open('out.txt', 'w') as f:
    strg = stringWithQuestions.findall(text_from_html(html))
    for sentence in strg:
        strg1 = strg1 + sentence + "\n"
    #print(strg1, file=f)

    listOfFlags1 = ["maiden", "address"]
    #print("list of questions, ", listOfFlags1)
    print("are the questions safe?")
    ruling = SafeQuestions(listOfFlags1,strg1)
    if ruling:
        print("Safe!")
        return True
    else:
        print("Not Safe!")
        return False
    print(strg1)

    
