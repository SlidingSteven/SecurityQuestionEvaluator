# SecurityQuestionEvaluator

## Goal
* Provide a way for people with no background in computer security to gain insight on the security level of security questions.  
* Provide insight to users on how much information can be divulged from a small source of public information.

## Link
You can visit our site here- https://sqs-checker.herokuapp.com/

## CHECKPOINTS 
1. [x] Research Paper 
2. [x] Lightning Talk
3. [x] Meet with professor
4. [ ] Final Product 


## TODO
* Update README with how to run code locally.

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


## How to add things
### HTML Templates
You can add HTML templates to the "templates" folder.  They have to go there or else flask will not find them.
### Python Functions
These can be added to the file in one of two ways.  You can do it in the app.py file if you know what you are doing or you can add 
```
import filenameWithNoExtension
```
to the top of the app.py file.  To use the functions built in the new file on the app.py scripts you can type
```
filenameWithNoExtension.functionName(WhateverParameters, you, need)
```

If you would rather write JS functions straight on the HTML pages that works too, but you will have to figure out how to make it work.

