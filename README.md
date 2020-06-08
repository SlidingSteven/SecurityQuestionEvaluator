# SecurityQuestionEvaluator

## Introduction
In today’s world, technology has become quite prevalent, and is frequently used to make life easier. People can access their bank accounts, or check important emails from the comfort of their homes. It’s all at their fingertips. However, this comes at a cost. With technology having such a large impact on people’s lives, people have become more concerned about their privacy and security. This is why security questions were initially implemented, to ensure the security of a user’s account. The answers to these questions are supposed to be unique to the user. The answers are supposed to be things that only the user would know. These questions are useful for user authentication, as well as backup for when someone forgets a password. However, these questions are proving to be counterproductive. Hackers and breachers are continuously seeking ways to extract personal information. The main element of security that this problem directly relates to is confidentiality. Nowadays, attackers can easily guess the answers to users’ security questions and gain access to their accounts. Instead of questions being a source of security for the user, they are becoming a source of concern. Hackers and breachers are always coming up with new ways to extract people’s personal information. As the world continues to advance, people are developing a greater dependency on technology. However, along with this dependency, more and more concerns about computer security are beginning to arise.

## Goal
* Provide a way for people with no background in computer security to gain insight on the security level of security questions.  
* Provide insight to users on how much information can be divulged from a small source of public information.

## Link
You can visit our site here- https://sqs-checker.herokuapp.com/
Or view an API of the public info demo here- https://sqs-checker.herokuapp.com/Full-Public-Info-Search?first_name=&last_name=&zipcode=

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

# Directions to Run SQS Checker
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
