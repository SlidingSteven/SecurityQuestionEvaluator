from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re


# This code will help to parse out the plain text from the html https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
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

def text_from_cards(body):
    soup = BeautifulSoup(body, 'html.parser')
    cards = soup.findAll("div", {"class": "card"})
    #texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, cards)  
    return u" ".join(t.strip() for t in visible_texts)



def SafeQuestions(listOfFlags,Questions):
    for word in listOfFlags:
        if word in Questions:#Not safe!
            return False
    return True #No flag word found


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

class Person:
    def __init__(self, name,age,link,family,aliases,addresses, mothersMaidenNames):
        self.name = name
        self.age = age
        self.link = link
        self.family = family
        self.aliases = aliases
        self.addresses = addresses
        self.mothersMaidenNames = mothersMaidenNames
    def get_age(self):
        return(self.age)
    def get_name(self):
        return(self.name)
    def get_link(self):
        return(self.link)
    def get_family(self):
        return(self.family)
    def get_aliases(self):
        return(self.aliases)
    def get_addresses(self):
        return(self.addresses)
    def get_Mothers_Maiden_Name(self):
        return(self.mothersMaidenNames)




def formatURL(url):
    base = 'https://www.fastpeoplesearch.com'
    base += url
    return base

def highLevelDetails(url):
    opener = AppURLopener()
    html = opener.open(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.findAll("a", {"class": "btn btn-primary link-to-details"}, href=True)
    h3s = soup.findAll("h3")
    listOfNames = []
    listOfAges = []
    for element in h3s:
        if "Full Name" in str(element):
            listOfNames += element
        if "Age" in str(element):
            age = str(element).replace("<h3>","").replace("</h3>","").replace("<strong>","").replace("</strong>","")
            listOfAges.append(age)
    #print("list of ages", listOfAges[0])
    listOfLinks = []
    for link in links:
        newLink = formatURL(link['href'])
        listOfLinks.append(newLink)
    #i = 0

    addresses = soup.findAll("a", {"title": re.compile('^Search people living at')}, text=True)
    listOfAddresses = []
    for address in addresses:
        listOfAddresses += address.contents
    

#checkFurtherDetails(listoflinks[0])

    #print(listOfAddresses)
    i = 0
    for person in listOfNames:
        ##print("**********BEGGINING OF PERSON***********")
        ##print(person, listOfAges[i], listOfLinks[i], listOfAddresses[i])
        
        familyMembers,aliases,newListOfAddresses,maidenNames = checkFurtherDetails(listOfLinks[i])
        ##print("**********RELATIVES***********")
        
        formattedFamily = []
        for member in familyMembers:
            formattedFamily.append(member[:-2])
            #print(member[:-2])
        ##print(formattedFamily)
        ##print("**********POTENTIAL MOTHERS MAIDEN NAMES***********")    
        #mothersMaidenNames=[]    
        #for member in familyMembers:
        #    if member[:-2].split()[1] not in mothersMaidenNames:
        #        #print(member[:-2].split()[1])
        #        mothersMaidenNames.append(member[:-2].split()[1])
        #print("Maiden Names////////////////////////////////////////////////")

        #print(mothersMaidenNames)
        ##print("**********End OF PERSON***********")


        i +=1
    return listOfLinks, listOfNames, listOfAges


def checkFurtherDetails(url):
    opener = AppURLopener()
    html = opener.open(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    relatives = soup.findAll("div", {"id": "relative-links"})
    #or relative in relatives:
    para = relatives[0].find('p')
    spans = para.findAll('span')
    listOfRevs = []
    for people in spans:
        listOfRevs += people.contents
        #print(people.contents)
    formattedFamily = []
    for member in listOfRevs:
        formattedFamily.append(member[:-2])

    mothersMaidenNames=[]    
    for member in formattedFamily:
        if member.split()[1] not in mothersMaidenNames:
            #print(member[:-2].split()[1])
            mothersMaidenNames.append(member.split()[1])
    spouse = soup.find("div", {"id":"aka-links"})
    ##print("**********ALIASES***********")
    listOfAliases = []
    aliases = spouse.find('p').contents
    for alias in aliases:
        alias = str(alias).strip('\t\r\n')
        listOfAliases.append(alias)
    listOfAliases = listOfAliases[0].split(" • ")
    ##print(listOfAliases)

    addresses = soup.findAll("a", {"title": re.compile('^Search people who live at')})
    listOfAddresses = []
    for address in addresses:
        listOfAddresses += address.contents
        #print(address.contents)
    
    #print(addresses)
    addresses = soup.findAll("div", {"class": "detail-box-address"})
    ##print("**********ADDRESSES***********")
    #listOfAddresses = listOfAddresses[0:3]
    #print(listOfAddresses)
    i=0
    newListOfAddresses = []
    for address in listOfAddresses:
        address = str(address).strip('\t\r\n')
        if "<br/>" not in address:
            newListOfAddresses.append(address)
            #print(address)
    ##print(newListOfAddresses)
    return(formattedFamily, listOfAliases, newListOfAddresses,mothersMaidenNames)


def publicInformation(first, last, zipcode):
    #first = "Angela"
    #last = "Tucker"
    #zipcode = "74012"

    url = "https://www.fastpeoplesearch.com/name/" + first.lower() + "-" + last.lower() + "_" + zipcode
    links, names, ages = highLevelDetails(url)

    peopleFound = []
    i =0
    for name in names:
        print("_________________BEGIN NEW OUTPUT___________")
        #print(name, "\n", ages[i], "\n", links[i], "\n")
        familyMembers,aliases,newListOfAddresses,mothersMaidenNames = checkFurtherDetails(links[i])

        #mothersMaidenNames=[]    
        #for member in familyMembers:
        #    if member.split()[1] not in mothersMaidenNames:
                #print(member[:-2].split()[1])
        #           mothersMaidenNames.append(member.split()[1])
                #mothersMaidenNames.append(member[:-2].split()[1])
        #print("Family- ", familyMembers, "\nAliases- ", aliases, "\nAddresses", newListOfAddresses, "\nPotential Mother's Maiden Names- ", mothersMaidenNames)
        tempPerson = Person(name, ages[i], links[i], familyMembers, aliases, newListOfAddresses, mothersMaidenNames)
        #print(type(name), type(ages[i]), type(links[i]), type(familyMembers), type(aliases), type(newListOfAddresses), type(mothersMaidenNames))

        peopleFound.append(tempPerson)
        #print(  peopleFound[i].get_name(), "\n",
        #    peopleFound[i].get_age(), "\n",
        #    peopleFound[i].get_addresses(), "\n", 
        #    peopleFound[i].get_aliases(), "\n",
        #    peopleFound[i].get_family(),"\n",
        #    peopleFound[i].get_link(),"\n",
        #    peopleFound[i].get_Mothers_Maiden_Name())
        i += 1


    return peopleFound



#publicInformation("Steven", "Tucker", "74012")


