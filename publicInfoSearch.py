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
    #print("LINKS---> ", links)
    h3s = soup.findAll("h3")
    listOfNames = []
    listOfAges = []
    cards = soup.findAll("div", {"class":"card-block"})
    for card in cards:
        #fill out a card object
        #name = soup.find("div", {"class":"card-block"})
        name = card
        #print(name)
        #name.h3.clear()
        print("PRINTING TEXT")
        #print(name.get_text())
        #print(name.get_text().split("\n"))
        card_contents = name.get_text().split("\n")
        print(card_contents)
        # for el in card_contents:
        #     print(el)
        for el in card_contents:
            el.strip()
        # for el in card_contents:
        #     print (el)
        card_contents = list(filter(None, card_contents))
        [x for x in card_contents if x]
        ctr = 0
        relatives_index = 100
        
        for el in card_contents:
            if "Age: " in el:
                print(el.replace("Age: ", ""))
                curr_age = el.replace("Age: ", "")
                listOfAges.append(curr_age)
            if "Full Name: " in el:
                print(el.replace("Full Name: ", ""))
                curr_name = el.replace("Full Name: ", "")
                listOfNames.append(curr_name)
            if "Mother, father" in el:
                relatives_index = ctr
            if ctr > relatives_index:
                if " • " in el:
                    print(el.split(" • "))
                    family = el.split(" • ")
            ctr += 1
    #print(card_contents)
    #exit(0)

    # for element in h3s:
    #     if "Full Name" in str(element):
    #         listOfNames += element
    #     if "Age" in str(element):
    #         age = str(element).replace("<h3>","").replace("</h3>","").replace("<strong>","").replace("</strong>","")
    #         listOfAges.append(age)

    #print("list of ages", listOfAges[0])


    listOfLinks = []
    for link in links:
        print("LINK---> ", link['href'])
        newLink = formatURL(link['href'])
        listOfLinks.append(newLink)
    #i = 0
    print("Size of list of names" + str(len(listOfNames)))
    for name in listOfNames:
        print(name)
    print("Size of list of links" + str(len(listOfLinks)))
    #exit()

    # get the everyone's current address
    addresses = soup.findAll("a", {"title": re.compile('^Search people living at')}, text=True)
    listOfAddresses = []
    for address in addresses:
        listOfAddresses.append(address.contents)

    i = 0
    for person in listOfNames:
        ##print("**********BEGGINING OF PERSON***********")
        ##print(person, listOfAges[i], listOfLinks[i], listOfAddresses[i])
        #print("listOfLinks[" + str(i)+ "] " + listOfLinks[i])
        familyMembers, aliases, newListOfAddresses, maidenNames = checkFurtherDetails(listOfLinks[i])
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
    relatives_table = soup.findAll("div", {"id": "relative-links"})
    print(len(relatives_table))
    #exit()
    relative_elements = relatives_table[0].findAll("div", {"class": "detail-box-content"})[0].find_all("dl", {"class": "col-sm-12 col-md-4"})
    print(len(relative_elements))
    
    #print(relative_elements)
    #text_of_elements = relative_elements.get
    listOfRevs = []
    for rel in relative_elements:
        print(rel.get_text().replace("\n","").strip())
        listOfRevs.append(rel.get_text().replace("\n","").strip())
    #exit()
    #or relative in relatives:
    # para = relatives[0].find('a')
    # spans = para.findAll('span')
    # listOfRevs = []
    # print("List of relatives--->")
    # for people in spans:
    #     listOfRevs += people.contents
    #     print(people.contents)
    # exit()
    formattedFamily = []
    for member in listOfRevs:
        member_name = member.split("Age")[0].strip()
        formattedFamily.append(member_name)


    mothersMaidenNames=[]    
    for member in formattedFamily:
        if member.split()[1] not in mothersMaidenNames:
            #print(member[:-2].split()[1])
            mothersMaidenNames.append(member.split()[1])
    spouse = soup.find("div", {"id":"aka-links"})
    print(spouse)
    ##print("**********ALIASES***********")
    listOfAliases = []
    aliases = spouse.find('h3').contents
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
    print(links)
    print(names)
    print(ages)
    #exit(0)
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


