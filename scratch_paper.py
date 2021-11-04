# Secure config
# chrome_DRIVER_PATH = str(pathlib.Path(__file__).parent.absolute()) + './chromedriver.exe'
# chrome_options = Options()
# # options.user_data_dir = "c:\\temp\\profile" # setting profile
# # # another way to set profile is the below (which takes precedence if both variants are used
# chrome_options.add_argument('--user-data-dir=c:\\temp\\zenProfile')
# chrome_options.add_argument('--no-first-run --no-service-autorun --password-store=basic') # ignore messages
# driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_DRIVER_PATH)
# Secure config

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from datetime import datetime
# import time
# import sys
# import os
# from os.path import join, dirname
# from dotenv import load_dotenv
# import pickle
# # Load env variables
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
# ZEN_USERNAME = os.environ.get("ZEN_USERNAME")
# ZEN_PASS = os.environ.get("ZEN_PASS")

# print(ZEN_USERNAME)
# print(ZEN_PASS)

# def printTime(preText):
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     print(preText, current_time)
#     sys.stdout.flush()

# # config
# DRIVER_PATH = 'C:/Users/Mkiml/Documents/installs/chromedriver.exe'
# s = Service(DRIVER_PATH)
# options = Options()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.headless = False
# options.add_argument('--no-proxy-server')
# options.add_argument("user-data-dir=ZenScrape") 
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument('--blink-settings=imagesEnabled=false')
# options.add_argument("--window-size=400,800")
# options.add_argument("--log-level=2")
# driver = webdriver.Chrome(options=options, service=s)
# driver.maximize_window()
# # config

# # code execution
# url = 'https://www.zenfolio.com/paulkimlinger/e/all-photos.aspx'
# try:
#     printTime('Starting Zenfolio Scrape at')
#     #Enter in Login Username
#     time.sleep(30)
#     print('entering username')
#     driver.quit()
# except:
#     print('Problem')
#     driver.quit()
# # code execution


# #load cookies
# cookies = pickle.load(open("./pickle_dumps/logged_in.pkl", "rb"))
# driver.get(url)
# for cookie in cookies:
#     driver.add_cookie(cookie)
# print('cookies loaded, fetching url...')
# print('page loaded')




    # SelectAllElement = WebDriverWait(driver, 300).until(
    #     EC.presence_of_element_located((By.XPATH, selectAllPhotos))
    # )
    # pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# config
DRIVER_PATH = 'C:/Users/Mkiml/Documents/installs/chromedriver.exe'
s = Service(DRIVER_PATH)
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = False
options.add_argument('--no-proxy-server')
options.add_argument("user-data-dir=Zenfolio") 
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument("--window-size=400,800")
options.add_argument("--log-level=2")
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
# config

# code execution
url = 'https://www.zenfolio.com/paulkimlinger/e/all-photos.aspx'
try:
    #Load url
    driver.get(url)
    print('Creating Zenfolio cookie')

    driver.quit()
except:
    print('Cookie Problem')
    driver.quit()
# code execution

# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from datetime import datetime
# from os.path import join, dirname
# from dotenv import load_dotenv
# from time import sleep
# import sys, pickle, os, getpass, pathlib

# # Load env variables
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
# ZEN_PATH = os.environ.get("ZEN_PATH")
# ZEN_USERNAME = os.environ.get("ZEN_USERNAME")
# ZEN_PASS = os.environ.get("ZEN_PASS")
# print(ZEN_USERNAME)
# print(ZEN_PASS)
# print(ZEN_PATH)

# def printTime(preText):
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     print(preText, current_time)
#     sys.stdout.flush()

# # function to take care of downloading file
# def enable_download_headless(browser,download_dir):
#     browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
#     params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
#     browser.execute("send_command", params)


# driver_path = 'C:/Users/Mkiml/Documents/installs/chromedriver.exe'
# s = Service(driver_path)
# chrome_options = Options()
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_options.headless = False
# chrome_options.add_argument("--window-size=400,800")
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--no-proxy-server')
# # chrome_options.add_argument("user-data-dir=Zenfolio") 
# chrome_options.add_argument("--proxy-server='direct://'")
# chrome_options.add_argument("--proxy-bypass-list=*")
# chrome_options.add_argument('--blink-settings=imagesEnabled=false')
# chrome_options.add_argument("--log-level=2")
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument('--disable-software-rasterizer')


# chrome_options.add_experimental_option("prefs", {
#         "download.default_directory": "./downloads",
#         "download.prompt_for_download": False,#disable download prompt 
#         "download.directory_upgrade": True,
#         "safebrowsing_for_trusted_sources_enabled": False,
#         "safebrowsing.enabled": False
# })

# driver = webdriver.Chrome(options=chrome_options, service=s)
# driver.maximize_window()

# download_dir = "./downloads"
# enable_download_headless(driver, download_dir)


# albumUrls = [
#     ''
# ]

# # Secure config
# # chrome_driver_path = str(pathlib.Path(__file__).parent.absolute()) + './chromedriver.exe'
# # chrome_options = Options()
# # # options.user_data_dir = "c:\\temp\\profile" # setting profile
# # # # another way to set profile is the below (which takes precedence if both variants are used
# # chrome_options.add_argument('--user-data-dir=c:\\temp\\zenProfile')
# # chrome_options.add_argument('--no-first-run --no-service-autorun --password-store=basic') # ignore messages
# # driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)
# # Secure config



# #zenHome_URL
# zenHome_URL = 'https://www.zenfolio.com/' + ZEN_PATH + '/e/all-photos.aspx'



# #XPaths
# UsrnmeX = '/html/body/div[2]/div/div[1]/form/div[2]/div/input'#Login Page
# passX = '/html/body/div[2]/div/div[1]/form/div[3]/div/input'
# submitButtonX = '/html/body/div[2]/div/div[1]/form/div[5]/a[2]'
# submitButtonX = '/html/body/div[2]/div/div[1]/form/div[5]/a[2]'#Creator Home Page

# allPhotosTreeX =  '/html/body/div[2]/div[2]/div/div[5]/div[1]/div[2]/div[1]/div'

# selectAllPhotos = '/html/body/div[2]/div[2]/div/div[6]/div/span/a[1]'
# PhotoActions = '/html/body/div[2]/div[2]/div/div[2]/a[1]'
# DownloadOriginalFiles = '/html/body/ul/li[13]'

# # CODE EXECUTION

# #Login to Zenfolio
# try:
#     driver.get(zenHome_URL) 
#     # Secure config
#     printTime('Starting Zenfolio Login Scrape at')
#     driver.get(zenHome_URL)
#     UsernameElement = WebDriverWait(driver, 300).until(
#         EC.presence_of_element_located((By.XPATH, UsrnmeX))
#     )
#     print('entering username')
#     UsernameElement.send_keys(ZEN_USERNAME) #Enter in Login Username
#     PasswordElement = driver.find_element(By.XPATH, passX)
#     print('entering password')
#     secure_pass = ZEN_PASS
#     print('secure_password: ', secure_pass)
#     PasswordElement.send_keys(secure_pass) #Enter in passwd
#     SubmitElement = driver.find_element(By.XPATH, submitButtonX)
#     SubmitElement = WebDriverWait(driver, 300).until(
#         EC.presence_of_element_located((By.XPATH, submitButtonX))
#     )
#     print('submitting..')
#     SubmitElement.click() #Submit Credentials
#     sleep(10)
# except:
#     print('Error Logging in to Zenfolio!')

# #Create URLS
# try:
#     print('found Tree buttons')
#     #Expand Folders
#     def expand_all_dir ():
#         TreeButtons = driver.find_elements_by_class_name('tree-collapsed')
#         if TreeButtons:
#             for CollapsedFolder in TreeButtons:
#                 OpenFolderIcon = CollapsedFolder.find_element_by_class_name("tree-btn")
#                 OpenFolderIcon.click();
#                 sleep(1)
#             return false
#         else:
#             print('No tree buttons found.')
#     def check_open_folders():
#         result = expand_all_dir ()




#     for CollapsedFolders in TreeButtons:
#         InnerAElement = CollapsedFolders.find_element_by_tag_name("a")
#         LinkHref = InnerAElement.get_attribute("href")
#         print(LinkHref)
# except:
#     print('Could not create URLS!')









#     #Download Zip Files 
#     SelectAllElement = WebDriverWait(driver, 300).until(
#         EC.presence_of_element_located((By.XPATH, selectAllPhotos))
#     )
#     driver.find_element(By.XPATH, selectAllPhotos).click()
#     sleep(10)
#     driver.find_element(By.XPATH, PhotoActions).click()
#     sleep(10)
#     driver.find_element(By.XPATH, DownloadOriginalFiles).click()
#     sleep(30)
#     # pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
#     driver.quit()
# except:
#     print('Problem')
#     driver.quit()
#     #     PhotoContainer.get_attribute("innerHTML")
#     # PhotosContainer = driver.find_elements_by_xpath(By.XPATH, allPhotosTreeX)
#     # for PhotoContainer in PhotosContainer:
# # code execution