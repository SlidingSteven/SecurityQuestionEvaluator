# SecurityQuestionEvaluator

## Introduction
This application was built to demonstrate how security questions on personal accounts pose a [serious weakness](https://www.wired.com/2016/09/time-kill-security-questions-answer-lies/) to the actual security of the account.  This app tackles the problem from a few angles -
1. If you are in the account creation process, you can go to the [Home Page](https://sqs-checker.herokuapp.com/) and enter the URL.  This app will then scrape all questions from the page and will check if the questions contain key words we found in many "weak" questions. 
2. If you want a demo of what public information is available on you, navigate to the [Public Info Demo](https://sqs-checker.herokuapp.com/Full-Public-Info-Search) and enter your name and zipcode.  The app will then pass that info to [FastPeopleSearch.com](fastpeoplesearch.com) and scrape the public info from the page using beautiful soup. 
3. Another demo we have is to show the weakness of the common security question- ["What is your mother's maiden name?"](https://sqs-checker.herokuapp.com/Mothers-Maiden-Name-Demo)  For this we perform the same search and scrape technique as we did in the public info search, but this time we look a little deeper and pull the family list of the person entered and return each unique last name of all of the family memnbers.  
4. If you are in need of a [secure answer](https://sqs-checker.herokuapp.com/Secure-Answers) and don't know what to do, you can use our app to give one idea.  On this page we take in a few answer components and return each permutation of that combination.  It is not the most ideal solution but for some questions it is better than giving the most accurate answer.

This is not meant to be a complete solution but it should give users a good idea of what is out there and one potential fix for how to avoid issues with weak account questions.



## Goal
* Provide a way for people with no background in computer security to gain insight on the security level of security questions.  
* Provide insight to users on how much information can be divulged from a small source of public information.

## Link
You can visit our site here- https://sqs-checker.herokuapp.com/ 

Or view an API of the public info demo here- https://sqs-checker.herokuapp.com/Full-Public-Info-Search?first_name=&last_name=&zipcode= 

Example of the formatting- https://sqs-checker.herokuapp.com/Full-Public-Info-Search?first_name=Bobby&last_name=Sue&zipcode=12345 

## CHECKPOINTS 
1. [x] Research Paper 
2. [x] Lightning Talk
3. [x] Meet with professor
4. [x] Final Product 


## How To Run
This flask app runs on Python 3.  When I downloaded Python 3 it makes me use "python3" in the shell to run it, some people may only need to use 'python'.  You can use pipenv to install dependencies and activate the shell-

```
python3 -m pipenv install 
python3 -m pipenv shell
```

Next navigate to the folder with the file app.py and run
```
python3 app.py
```
Then go to http://127.0.0.1:5000/ to see the index page

# Explanation of each page
## Home Page
To check the strength of a set of particular security questions on a particular page
* enter the URL into the input. 
* Select 'Run checker' to see if unsafe questions were found or not.

## The Team
Visit this page to learn more about our team and their roles in the creation of the SQS Checker.

## Demo Mothers Maiden Name
To find if your mother maiden name can be found, enter first name, last name, zip code.
* Select 'Run checker' to view results.

## Creating a Secure answer
In the case that you have no other option but to answer a weak question then the best thing you can do is to add components to your answer. You can add up to 5 components, and the SQS Checker will generate various passwords related to your mothers maiden name. They will contain special characters, which will make your security question harder to crack.
* Enter mothers name for component 1
* mothers birthday for component 2
and so on.

## Public Info Demo
* Enter First name, last name and zipcode
* Select run checker to check if your public information can be found by the SQS Checker
