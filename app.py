from flask import Flask, request, render_template, jsonify
import newbs4
import publicInfoSearch
import itertools 
import os
from collections import OrderedDict
from pprint import pprint
import json
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#Url entry page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        ruling = newbs4.checkURL(url)
        if ruling:
            return render_template('SSQ Checker/resultsUnsafe.html', ruling = ruling)
        else:
            return render_template('SSQ Checker/resultsSafe.html', ruling = "NO UNSAFE QUESTIONS FOUND")        
    else:
        return render_template('SSQ Checker/index.html')


# team page
@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('SSQ Checker/team.html')





# Page for the demonstration of a full public search
@app.route('/Full-Public-Info-Search', methods=['GET', 'POST'])
def fullSearch():
    if request.method =='POST':
        first_name = request.form['first']
        last_name = request.form['last']
        zipcode = request.form['zipcode']
        try: 
            PeopleFound = publicInfoSearch.publicInformation(first_name, last_name, zipcode)
            i=0
            newList = []
            data_list = []
            json_obj = {}
            for person in PeopleFound:
                newString = ""
                newString += PeopleFound[i].get_name() + "<br/>"
                newString += PeopleFound[i].get_age() +  "<br/>"
                addresses = PeopleFound[i].get_addresses() 
                for address in addresses:
                    addy = address + "<br/>"
                    newString += addy
                aliases = PeopleFound[i].get_aliases()
                for alias in aliases:
                    ali = alias + "<br/>"
                    newString += ali
                familyMembers = PeopleFound[i].get_family()
                for family in familyMembers:
                    fam = family + "<br/>"
                    newString += fam
                newList.append(newString)
                curr_person = {
                    "name": PeopleFound[i].get_name(),
                    "age": PeopleFound[i].get_age(),
                    "addresses": PeopleFound[i].get_addresses()
                }
                data_list.append(json.dumps(curr_person))
                i+=1
            for el in data_list:
                print(el)
            #pprint(data_list)
            if PeopleFound:
                return render_template('SSQ Checker/FullSearchDemo.html', PeopleFound = newList)
            else:
                return render_template('SSQ Checker/FullSearchDemo.html', PeopleFound = "No Potential Information Found", flag = True)
        except ValueError:
            return render_template('SSQ Checker/FullSearchDemo.html', Error = "No Potential Information Found")
    # else = GET request
    else:
        # check for query params (section following the ? in the url below)
        # https://sqs-checker.herokuapp.com/Full-Public-Info-Search?first_name=Bobby&last_name=Sue&zipcode=12345
        # by checking for these particular params, I am forcing the user to also use those particular params 
        # In other words, this is how the params  are set to 'first_name', 'last_name' and 'zipcode'
        if 'first_name' in request.args and 'last_name' in request.args and 'zipcode' in request.args:
            # if the params exist then try to do a search with their contents
            try: 
                # get the params from the url
                first_name = request.args['first_name']
                last_name = request.args['last_name']
                zipcode = request.args['zipcode']

                # perform the same search as we did with the post request 
                PeopleFound = publicInfoSearch.publicInformation(first_name, last_name, zipcode)
                i=0

                # declare a list to put person results in 
                data_list = []

                # for each person in the list that was found, add their person info
                for person in PeopleFound:
                    curr_person = {
                        "name": PeopleFound[i].get_name(),
                        "age": PeopleFound[i].get_age(),
                        "addresses": PeopleFound[i].get_addresses(),
                        "aliases": PeopleFound[i].get_aliases(),
                        "family": PeopleFound[i].get_family()
                    }

                    #add the person to the list
                    data_list.append(curr_person)
                    i+=1
                
                # return the list as a json object
                return jsonify(data_list)

            # if 1- the contents are formatted incorrectly, or 2- the contents return no results then return an error message
            except:
                return """Error: A field is missing or no data was returned.  
                See below for formatting-\n
                https://sqs-checker.herokuapp.com/Full-Public-Info-Search?first_name=Bobby&last_name=Sue&zipcode=12345
                
                If you think you have it properly formatted you can try searching your name on fastpeoplesearch.com which is where I scrape from."""
        
        # if there are no query params then just return the html for the entry
        return render_template('SSQ Checker/FullSearchDemo.html')

#Mother's maiden name demo
@app.route('/Mothers-Maiden-Name-Demo', methods=['GET', 'POST'])
def MaidenNameDemo():
    if request.method == 'POST':
        first_name = request.form['first']
        last_name = request.form['last']
        zipcode = request.form['zipcode']
        try: 
            PeopleFound = publicInfoSearch.publicInformation(first_name, last_name, zipcode)
            maidenNames = []
            for person in PeopleFound:
                tempNames = person.get_Mothers_Maiden_Name()
                for tempName in tempNames:
                    if tempName not in maidenNames:
                        maidenNames.append(tempName)
            if PeopleFound:
                return render_template('SSQ Checker/MaidenDemoSearch.html', listOfPeople = maidenNames)
            else:
                return render_template('SSQ Checker/MaidenNameDemo.html', listOfPeople = "No Potential Maiden Names Found", flag = True)
        except ValueError:
            return render_template('SSQ Checker/MaidenNameDemo.html', listOfPeople = "No Potential Maiden Names Found")
    else:
        return render_template('SSQ Checker/MaidenDemoSearch.html')#, ruling = "SAFE")

#Secure answer builder demo
@app.route('/Secure-Answers', methods=['GET', 'POST'])
def secureAnswers():
    if request.method == 'POST':
        component0 = request.form['component0']
        component1 = request.form['component1']
        component2 = request.form['component2']
        component3 = request.form['component3']
        component4 = request.form['component4']

        #
        #
        #   COPY SECTION FOR API
        #
        #
        # TODO FOR API: COPY FROM HERE
        listOfRecommendations = []
        numComponents = 0
        if component0:
            numComponents += 1
            listOfRecommendations.append(component0)
            if component1:
                numComponents += 1
                listOfRecommendations.append(component1)
                if component2:
                    numComponents += 1
                    listOfRecommendations.append(component2)
                    if component3:
                        numComponents += 1        
                        listOfRecommendations.append(component3)
                        if component4:
                            numComponents += 1
                            listOfRecommendations.append(component4)
        perm = itertools.permutations(listOfRecommendations) 
        betterFormattedList = []
        if numComponents == 1:
            for i in list(perm): 
                betterFormattedList.append(i[0])
            print(betterFormattedList)
        if numComponents == 2:
            for i in list(perm): 
                betterFormattedList.append(i[0]+"--"+i[1])
            print(betterFormattedList)        
        if numComponents == 3:
            for i in list(perm): 
                betterFormattedList.append(i[0]+"--"+i[1]+"--"+i[2])
            print(betterFormattedList)
        if numComponents == 4:
            for i in list(perm): 
                betterFormattedList.append(i[0]+"--"+i[1]+"--"+i[2]+"--"+i[3])
            print(betterFormattedList)
        if numComponents == 5:
            for i in list(perm): 
                betterFormattedList.append(i[0]+"--"+i[1]+"--"+i[2]+"--"+i[3]+"--"+i[4])
            print(betterFormattedList)
        # TODO FOR API: TO HERE
        #
        #
        #   COPY SECTION FOR API
        #
        #

        return render_template('SSQ Checker/SecureInput.html', betterFormattedList = betterFormattedList)

        
    else:
        # check if query params exist (If it were me I'd check for "component1, component2... so on, just like in the post method above.")
            # if the query params exist then run the code from line 170-208 (I have comments around the code), return the jsonify-ed list
            # else return error message
 
        return render_template('SSQ Checker/SecureInput.html')#, ruling = "SAFE")


#runs the app
if __name__ == '__main__':
    app.debug = True
    app.run()#port = os.environ["PORT"])
