from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import sys

def printTime(preText):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(preText, current_time)
    sys.stdout.flush()

# config
DRIVER_PATH = 'C:/Users/Mkiml/Documents/installs/chromedriver.exe'
s = Service(DRIVER_PATH)
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
options.add_argument('--no-proxy-server')
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument("--window-size=400,800")
options.add_argument("--log-level=2")
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
# config

# code execution
url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
try:
    printTime('Starting BestBuy Scrape at')
    driver.get(url)
    xPath = '/html/body/div[3]/main/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/button'
    xPathValue = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, xPath))
    )
    if (xPathValue.text == 'Sold Out'):
        print('Sold Out')
        driver.quit()
    else:
        print('Check Now')
        driver.quit()
except:
    print('Problem')
    driver.quit()
