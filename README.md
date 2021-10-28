# Tired of Seeing RTX 8080 "Sold Out"?

This program will let you know when the RTX 8080 10 GB Graphics card
will be in stock, both by audio que, and a text. Designed to scrape 
the best buy website looking for changes to the "Sold Out" button it 
can determine if it needs to trigger an alarm.

## HOW TO USE

Designed and tested on a Window's Machine.

### Prerequisites:
* nodejs & npm installed
* python 1 installed
### Install Packages

Clone project to your directory

npm install \
pip install selenium \
pip install pygame
### Install Chrome Driver & replace path
1. Find your current chrome version type - chrome://settings/
2. download the corresponding driver from
https://chromedriver.chromium.org/downloads
3. copy full /xx/xx/.exe download path found when right-clicking Properties
4. <strong>REPLACE</strong> DRIVER_PATH on best_buy_scrape.py with your path

ex: DRIVER_PATH = 'C:/Users/Matt/Documents/installs/chromedriver.exe'

## Note
You will need to create Twilio API credentials and create a .env file in the root directory
and replace all process.env locations for texting services to work. Or comment out both sendText() functions
in triggerAlarm() & triggerAlert()

* Be sure to test .py scripts beforehand
## How to Run 
npm start
\
The program will cycle through every ~ 10 minutes until the data received from the scrape triggers the alarm

