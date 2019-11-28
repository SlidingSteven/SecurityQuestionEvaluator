from flask import Flask, request, render_template
import newbs4
import publicInfoSearch
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        ruling = newbs4.checkURL(url)
        if ruling:
            return render_template('SSQ Checker/index.html', ruling = ruling)
            #return render_template('index.html', ruling = "SAFE")
        else:
            return render_template('SSQ Checker/index.html', ruling = "NO UNSAFE QUESTIONS FOUND")

            #return render_template('index.html', ruling = "NOT SAFE")
        
    else:
        #return render_template('SSQ Checker/index.html')#, ruling = "SAFE")
        return render_template('SSQ Checker/indexSearch.html')
        #return render_template('index.html')

@app.route('/Mothers-Maiden-Name-Demo', methods=['GET', 'POST'])
def MaidenNameDemo():
    if request.method == 'POST':
        first_name = request.form['first']
        last_name = request.form['last']
        zipcode = request.form['zipcode']

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
            return render_template('SSQ Checker/MaidenNameDemo.html', listOfPeople = maidenNames)
            #return render_template('index.html', ruling = "SAFE")
        else:
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


        listOfRecommendations = []
        numComponents = 0
        if component0:
            numComponents += 1
            if component1:
                numComponents += 1
                if component2:
                    numComponents += 1

        print(numComponents)
        return render_template('SSQ Checker/SecureOutput.html', listOfRecommendations = numComponents)

        
    else:
        return render_template('SSQ Checker/SecureInput.html')#, ruling = "SAFE")

        #return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
