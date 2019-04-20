# review-scraper
A simple api end point to get reviews for a specified grubhub restaurant page.

## Requirements
+ Python 3.7
+ VirtualEnv (should comne with 3.7 by default)
+ pip (should come with 3.7 by default)

## Setup
Disclaimer: I develop in a windows environment, so the unix commands come straight from the flask installation/quickstart guide. I tested them using the linux shell in vs code, so they should work. HOWEVER I wasn't able to test the setups for Linux and Mac. In the worst case, see the links at the bottom to download the chrome drivers without using the setup files.

+ Navigate to project folder
+ Create virtual environment (please use venv so the chromedriver is in the correct place)
  + Unix: python3 -m venv venv
  + Windows: py -3 -m venv venv
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
+ Run setup file to install chrome driver
  + Windows: py setup_windows.py
  + Linux: python3 setup_linux.py
  + Mac: python3 setup_mac.py
+ Run application
  + All environments: flask run
+ Use the endpoint: http://127.0.0.1:5000/scrape_reviews (accepts a post, expecting 'url' in the body as form data)
  + curl -X POST -F 'url=https://www.grubhub.com/restaurant/burrito-king-408-e-green-st-champaign/262953' http://127.0.0.1:5000/scrape_reviews

## Tests
Tests are located in test folders under the folder the code being tested is located in. (for app.py, '/Review-Scraper/Tests/app-tests.py' etc)
I used nosetest to run them, which should be installed from the requirements.txt
Should just need to run "nosetests" in any environment.

## Chromedriver
In order to easily use selenium, I drop the chromedriver right next to the virtualenv python executable. While I tried to automate this as much as possible,
if you're on a different version of chrome or the Linux/Mac setup scripts don't work, I wanted to provide the links to download the chrome driver.
+ The main download page is here: http://chromedriver.chromium.org/downloads
+ If on Linux or Mac:
  + Drop the extracted executable into the /venv/bin folder
  + Run chmod 755 on the executable
+ If on Windows:
  + Drop the extracted executable into the /venv/Scripts folder