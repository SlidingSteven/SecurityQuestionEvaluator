from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re


# This code will help to parse out the plain text from the html https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
def vis_tag(element):
    #discard invisible html because it does not matter to this project
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    #return visible
    if isinstance(element, Comment):
        return False
    return True

def html_to_text(body):
    #get the body of html
    soup = BeautifulSoup(body, 'html.parser')
    #find text
    texts = soup.findAll(text=True)
    #apply above filter to html
    visible_texts = filter(vis_tag, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def text_from_cards(body):
    soup = BeautifulSoup(body, 'html.parser')
    cards = soup.findAll("div", {"class": "card"})
    #texts = soup.findAll(text=True)
    visible_texts = filter(vis_tag, cards)  
    return u" ".join(t.strip() for t in visible_texts)



def SafeQuestions(listOfFlags, Questions):
    for word in listOfFlags:
        if word in Questions:#Not safe!
            return False
    return True #No flag word found

# followed tutorial to find this.  
# This was a hurdle because it seems some webpages will and wont be accessed with beautiful soup
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

#This is used to make a person object for each person the fastpeoplesearch returned
#since we have to investigate all possibilities we found this the easiest way to keep everything straight
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



#formats the url to include input from the user
def formatURL(url):
    base = 'https://www.fastpeoplesearch.com'
    base += url
    return base

#get high level details on each person returned
def highLevelDetails(url):
    #initialize new opener
    opener = AppURLopener()
    #read contents returned
    try: 
        html = opener.open(url).read()
    except:
        return ["FAILED TO OPEN HTML", "FAILED TO OPEN HTML", "FAILED TO OPEN HTML"]
    #get the soup
    soup = BeautifulSoup(html, 'html.parser')
    #grab the more in depth details link
    links = soup.findAll("a", {"class": "btn btn-primary link-to-details"}, href=True)
    listOfLinks = []
    for link in links:
        newLink = formatURL(link['href'])
        listOfLinks.append(newLink)


    h3s = soup.findAll("h3")
    listOfNames = []
    listOfAges = []
    cards = soup.findAll("div", {"class":"card-block"})
    for card in cards:

        name = card

        card_contents = name.get_text().split("\n")

        for el in card_contents:
            el.strip()

        card_contents = list(filter(None, card_contents))
        [x for x in card_contents if x]
        ctr = 0
        relatives_index = 100
        
        for el in card_contents:
            if "Age: " in el:
                curr_age = el.replace("Age: ", "")
                listOfAges.append(curr_age)
            if "Full Name: " in el:
                curr_name = el.replace("Full Name: ", "")
                listOfNames.append(curr_name)
            if "Mother, father" in el:
                relatives_index = ctr
            if ctr > relatives_index:
                if " • " in el:
                    family = el.split(" • ")
            ctr += 1

    # get the everyone's current address, plan to include this on the api in my TODO
    addresses = soup.findAll("a", {"title": re.compile('^Search people living at')}, text=True)
    listOfAddresses = []
    for address in addresses:
        listOfAddresses.append(address.contents)

    return listOfLinks, listOfNames, listOfAges

# the last function checked high level but returned a link to drill into each person found
def checkFurtherDetails(url):
    #initialize opener
    opener = AppURLopener()

    #open the link to the person
    html = opener.open(url).read()

    # make the soup
    soup = BeautifulSoup(html, 'html.parser')

    # find the relatives table, build a list of each relative element 
    relatives_table = soup.findAll("div", {"id": "relative-links"})
    relative_elements = relatives_table[0].findAll("div", {"class": "detail-box-content"})[0].find_all("dl", {"class": "col-sm-12 col-md-4"})    

    # build list of each relative from the list of elements
    listOfRevs = []
    for rel in relative_elements:
        listOfRevs.append(rel.get_text().replace("\n","").strip())

    # reformat the names to exclude the ages
    formattedFamily = []
    for member in listOfRevs:
        member_name = member.split("Age")[0].strip()
        formattedFamily.append(member_name)

    # compile a list of last names, maiden name is likely to be here
    mothersMaidenNames=[]    
    for member in formattedFamily:
        if member.split()[1] not in mothersMaidenNames:
            mothersMaidenNames.append(member.split()[1])
    
    spouse = soup.find("div", {"id":"aka-links"})
    listOfAliases = []
    aliases = spouse.find('h3').contents
    for alias in aliases:
        alias = str(alias).strip('\t\r\n')
        listOfAliases.append(alias)
    listOfAliases = listOfAliases[0].split(" • ")

    # compile a list of previous addresses
    addresses = soup.findAll("a", {"title": re.compile('^Search people who live at')})
    listOfAddresses = []
    for address in addresses:
        listOfAddresses += address.contents
    
    addresses = soup.findAll("div", {"class": "detail-box-address"})

    i=0
    newListOfAddresses = []
    for address in listOfAddresses:
        address = str(address).strip('\t\r\n')
        if "<br/>" not in address:
            newListOfAddresses.append(address)
    
    # return all that is found
    return(formattedFamily, listOfAliases, newListOfAddresses,mothersMaidenNames)


def publicInformation(first, last, zipcode):
    # build the url according to input
    url = "https://www.fastpeoplesearch.com/name/" + first.lower() + "-" + last.lower() + "_" + zipcode
    
    # fill out the high level details
    links, names, ages = highLevelDetails(url)
    if links in "FAILED TO OPEN HTML":
        return "FAILED TO OPEN HTML"
    # compile a list of people 
    peopleFound = []
    i =0
    for name in names:
        familyMembers,aliases,newListOfAddresses,mothersMaidenNames = checkFurtherDetails(links[i])

        # create a person object
        tempPerson = Person(name, ages[i], links[i], familyMembers, aliases, newListOfAddresses, mothersMaidenNames)

        # add the person to a list
        peopleFound.append(tempPerson)

        i += 1


    return peopleFound





