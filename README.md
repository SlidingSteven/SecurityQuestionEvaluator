# SecurityQuestionEvaluator

## CHECKPOINTS 
1. Research Paper
2. Lightning Talk
3. Meet with professor
4. Final Product

## TODO
* Research common security questions and determine what is weak/strong

	* Compile a list of websites that use security questions.  Looking for banks, emails, social media accounts for a starting point.
	* Google has done research on this that may be useful for getting started.

* Build a flask app to evaluate all questions on a website given a URL

	User should input a url and we will automatically scrape the HTML on the page using Python to find security questions and extract them.  
	* We will need to first make a simple flask app
	* Next need some front end constructed
	* Start small and evaluate a question on input
	* Eventually get rid of the question on input and just use a URL or html upload, if possible.  I have a concern if we will be able to see the page contents at that point or if they will be locked and need a password to get to.  Maybe we will need to upload a file.

## How To Run
This flask app runs on Python 3.  When I downloaded Python 3 it makes me use "python3" in the shell to run it, some people may only need to use 'python'.  You can use pipenv to install dependencies and activate the shell-

```
python3 -m pipenv install 
pyhton3 -m pipenv shell
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
