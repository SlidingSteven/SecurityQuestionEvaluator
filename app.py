from flask import Flask, request, render_template
import newbs4
import publicInfoSearch
import itertools 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        ruling = newbs4.checkURL(url)
        if ruling:
            return render_template('SSQ Checker/resultsUnsafe.html', ruling = ruling)
            #return render_template('index.html', ruling = "SAFE")
        else:
            return render_template('SSQ Checker/resultsSafe.html', ruling = "NO UNSAFE QUESTIONS FOUND")

            #return render_template('results.html', ruling = "NOT SAFE")
        
    else:
        #return render_template('SSQ Checker/index.html')#, ruling = "SAFE")
        return render_template('SSQ Checker/index.html')
        #return render_template('index.html')



@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('SSQ Checker/team.html')
    #return render_template('index.html')

        

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
                i+=1
            print(newList)
            #maidenNames = []
            #for person in PeopleFound:
             ##   tempNames = person.get_Mothers_Maiden_Name()
             #   for tempName in tempNames:
              #      if tempName not in maidenNames:
               #         maidenNames.append(tempName)
            #print("FROM APP- ", maidenNames)
            #exit()
            if PeopleFound:
                return render_template('SSQ Checker/FullSearchDemo.html', PeopleFound = newList)
                #return render_template('index.html', ruling = "SAFE")
            else:
                return render_template('SSQ Checker/FullSearchDemo.html', Error = "No Potential Information Found", flag = True)
        except ValueError:
            return render_template('SSQ Checker/FullSearchDemo.html', Error = "No Potential Information Found")
    else:
        return render_template('SSQ Checker/FullSearchDemo.html')


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
            #print("FROM APP- ", maidenNames)
            #exit()
            if PeopleFound:
                return render_template('SSQ Checker/MaidenDemoSearch.html', listOfPeople = maidenNames)
                #return render_template('index.html', ruling = "SAFE")
            else:
                return render_template('SSQ Checker/MaidenNameDemo.html', listOfPeople = "No Potential Maiden Names Found", flag = True)
        except ValueError:
            return render_template('SSQ Checker/MaidenNameDemo.html', listOfPeople = "No Potential Maiden Names Found")

            #return render_template('index.html', ruling = "NOT SAFE")
        
    else:
        return render_template('SSQ Checker/MaidenDemoSearch.html')#, ruling = "SAFE")

        #return render_template('index.html')

@app.route('/Secure-Answers', methods=['GET', 'POST'])
def secureAnswers():
    if request.method == 'POST':
        component0 = request.form['component0']
        component1 = request.form['component1']
        component2 = request.form['component2']
        component3 = request.form['component3']
        component4 = request.form['component4']



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
        for i in list(perm): 
            betterFormattedList.append(i[0]+"--"+i[1]+"--"+i[2])
        print(betterFormattedList)
        return render_template('SSQ Checker/SecureInput.html', betterFormattedList = betterFormattedList)

        
    else:
        return render_template('SSQ Checker/SecureInput.html')#, ruling = "SAFE")

        #return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
