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
from time import sleep
import sys


def printTime(preText):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(preText, current_time)
    sys.stdout.flush()

params = {
    "latitude": float(sys.argv[1]),
    "longitude": float(sys.argv[2]),
    "accuracy": 100,
}
# params = {
#     "latitude": 45.03996,
#     "longitude": -93.02489,
#     "accuracy": 100,
# }

# config
DRIVER_PATH = "C:/Users/Mkiml/Documents/installs/chromedriver.exe"
s = Service(DRIVER_PATH)
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.headless = False
options.add_argument("--no-proxy-server")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--blink-settings=imagesEnabled=false")
options.add_argument("--window-size=1800,1200")
options.add_argument("--log-level=2")
driver = webdriver.Chrome(options=options, service=s)
driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
driver.maximize_window()
# xpath's
StoreLocationXPath = '//*[@id="lt-container"]/div/div/span/span/button/span[2]'
buttonXPath = "/html/body/div[3]/main/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/button"

# code execution
url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
try:
    printTime("Starting BestBuy Scrape at")
    driver.get(url)
    sleep(5)
    MyStoreElement = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, StoreLocationXPath))
    )
    print('Store Checked: ', MyStoreElement.text)
    ButtonElement = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, buttonXPath))
    )
    # print('Store Location: ')
    # print(MyStoreElement.text)
    if ButtonElement.text == "Sold Out":
        print("Sold Out")
        driver.quit()
    else:
        print("Check Now")
        driver.quit()
except Exception as e:
    print("Problem: ", e)
    driver.quit()
