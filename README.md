# review-scraper
A simple api end point to get reviews for a specified grubhug restaurant page.

## Requirements
+ Python 3.7
+ VirtualEnv (should comne with 3.7 by default)
+ pip (should come with 3.7 by default)

## Setup
Disclaimer: I develop in a windows environment, so the unix commands come straight from the flask installation/quickstart guide. I tested them using the linux shell in vs code, so they should work.

+ Navigate to project folder
+ Create venv
  + Unix: python3 -m venv venv
  + Windows: py -3 m venv venv
+ Activate venv
  + Unix: . venv/bin/activate
  + Windows: venv\Scripts\activate
+ Install requirements
  + pip install -r requirements.txt
+ Set application path
  + Unix: export FLASK_APP=app.py
  + Windows
    + cmd: set FLASK_APP=app.py
    + Powershell: $env:FLASK_APP = "app.py"
+ Run application
  + All environments: flask run
+ Hit the endpoint: http://127.0.0.1:5000/scrape_reviews (accepts a post, expecting 'url' in the form data)

## Tests
Tests are located in test folders under the folder the code being tested is located in. (for app.py, '/Review-Scraper/Tests/app-tests.py' etc)
I used nosetest to run them, which should be installed from the requirements.txt
Should just need to run "nosetests" in any environment.