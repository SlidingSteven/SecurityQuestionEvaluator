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
            #print(Questions)
            return False
    return True #No flag word found


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def checkURL(url):
    opener = AppURLopener()
    html = opener.open(url).read()
    #stringWithQuestions = re.compile(r'([A-Z][^\?]*[\?])', re.M)
    #stringWithQuestions = re.search('^[A-Z].*\?$', str(html))
    html = text_from_html(html)
    #print(html)
    stringWithQuestions = re.split('(?<=[.!?]) +', str(html))
    #stringWithQuestions = re.findall('[A-Z].*process.$', str(html))
    listOfQs = []
    for line in stringWithQuestions:
        if "?" in line:
            #print(line)
            listOfQs.append(line)
    #for q in listOfQs:
        #print(q)




    strg1 =""
    with open('out.txt', 'w') as f:
        strg = stringWithQuestions#.findall(text_from_html(html))
        for sentence in strg:
            strg1 = strg1 + sentence + "\n"
        print(strg1, file=f)

    listOfFlags1 = ["maiden", "address", "name"]
    dictOfWordsVals = {
        "maiden" : 2,
        "mother's maiden name" : 3,
        "address" : 2,
        "name" : 2,
        "school" : 1,
        "high school" : 2,
        "highschool" : 2,
        "college" : 2,
        "college major" : 2,
        "city" : 2,
        "state" : 2,
        "country" : 3,
        "occupation" : 1,
        "job" : 1,
        "town" : 2,
        "born" : 2,
        "hair color" : 3,
        "eye color" : 3,
        "favorite movie" : 1,
        "zipcode" : 3,
        "zip code" : 3,
        "zip-code" : 3,
        "born": 1,
        "spouse" : 2,
        "graduate" : 1,
        "favorite sport": 1
    }
    dictOfWordsReasons = {
        "maiden" : " A maiden name can be guessed quite easily using public records.",
        "mother's maiden name" : "A maiden name can be guessed quite easily using public records.",
        "address" :"Past addresses are quite easily found using public records.",
        "name" :"Public records keep a list of names suspected to be relatives.  Additionally if you keep a friends list on social media this can be used against you by an attacker.",
        "school" :"This is less likely to be found with a public records site but could easily be found through a person's social media.",
        "high school" :
        "This is less likely to be found with a public records site but could easily be found through a person's social media.",
        "highschool" : "This is less likely to be found with a public records site but could easily be found through a person's social media.",
        "college" : "This is less likely to be found with a public records site but could easily be found through a person's social media.",
        "college major" : "This is less likely to be found with a public records site but could easily be found through a person's social media.",
        "city" : "A list of cities stored in public record associated with your previous addresses could be used by an attacker to guess an answer to this question.",
        "state" : "A list of states stored in public record associated with your previous addresses could be used by an attacker to guess an answer to this question.",
        "country" : "A list of countries stored in public record associated with your previous addresses could be used by an attacker to guess an answer to this question.",
        "occupation" : "Public records do not track occupation but this is something that could easily be found through a LinkedIn account or really any form of social media.",
        "job" : "Public records do not track occupation but this is something that could easily be found through a LinkedIn account or really any form of social media.",
        "town" : "A list of towns stored in public record associated with your previous addresses could be used by an attacker to guess an answer to this question.",
        "born" : "Information regarding your birthdate or place of birth could be easily deduced by an attacker using public record",
        "hair color" : "An attacker could easily look up a victim's social media to find information regarding hair color.",
        "eye color" : "An attacker could easily look up a victim's social media to find information regarding eye color.",
        "favorite movie" : "If you have a list of liked movies on Facebook this can be found easily by an attacker.",
        "zipcode" : "A list of zipcodes stored in public record associated with your previous addresses could be used by an attacker to guess an answer to this question.",
        "zip code" : "A list of zipcodes stored in public record associated with your previous addresses could be used by an attacker to guess an answer to this question.",
        "zip-code" : "A list of zipcodes stored in public record associated with your previous addresses could be used by an attacker to guess an answer to this question.",
        "spouse" : "Spousal information can be found quite easily with public record.",
        "graduate" : "Graduation information can be found quite easily with a person's facebook.",
        "favorite sport": "If an attacker knows a victim's social media this may be used against them to find the favorite sport."
    }
    #print("list of questions, ", listOfFlags1)
    #print(dictOfWordsVals)
    #for key in dictOfWordsVals:
    #    print(key)
    stringOfOutput = []
    for line in listOfQs:
        for key in dictOfWordsVals:
            if key in line:
                stringTemp  = key + ": " + dictOfWordsReasons[key] + "\n " + line
                stringOfOutput.append(stringTemp)
                #print(key, " : ", dictOfWordsReasons[key], "\n", line, "\n")
                #listOfQs.append(line)

    for line in stringOfOutput:
        line = line.split('\n')
        print(line)

    return(stringOfOutput)
    #print(listOfQs)    print("are the questions safe?")
    ruling = SafeQuestions(listOfFlags1,strg1)
    if ruling:
        print("Safe!")
        #return True
    else:
        print("Not Safe!")
        #return False
    #strg1.split("\n")

    #print(sentence)



#checkURL('https://www.loginradius.com/blog/2019/01/best-practices-choosing-good-security-questions/')
