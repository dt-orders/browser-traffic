from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

import argparse
import time 
import sys
import random
import logging

def get_random_username():
  userarray = ["Allison","Betty","Charlie","David","Eddy","Fransis","Gordon","Helen","Ingrid","Jason"]
  user = userarray[random.randint(0,9)]
  logging.debug("Setting User to: " + user)
  return user

def get_random_ip():
  location = random.randint(1,4)
  if location == 1:
    logging.debug("Setting Location to: Germany/Hamburg/Hamburg")
    ip = "111.111.111.0" 
  elif location == 2:
    logging.debug("Setting Location to: US/FLorida/Orlando")
    ip = "111.111.112.0"
  else:
    logging.debug("Setting Location to: United Kingdom/City of London/City of London")
    ip = "111.111.113.0"

  return ip
    
def get_desired_capabilities():
  desired_capabilities = DesiredCapabilities.CHROME.copy()
  desired_capabilities['chrome.page.customHeaders.host'] = 'test.local'
  return desired_capabilities

def get_chrome_options(show_browser) -> None:
    chrome_options = Options()
    if(show_browser==False):
      logging.debug("Hiding Browser")
      chrome_options.add_argument("--headless")
    else:
      logging.debug("Showing Browser")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1200x600")
    chrome_options.add_argument('--deny-permission-prompts')
    #chrome_options.add_argument("user-agent=whatever you want")
    
    #prefs = {"profile.default_content_setting_values.geolocation" :2}
    #chrome_options.add_experimental_option("prefs",prefs)

    return chrome_options
  
def pause(message="", num_seconds=2):
  logging.debug(message + " sleep: " + str(num_seconds) + " seconds")
  time.sleep(num_seconds)

if __name__ == "__main__":

    # process args
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url",help="The base URL for the script. default is http://localhost")
    parser.add_argument("-n","--num_loops", type=int, help="Number of loops for the script to repeat.  Default is 1")
    parser.add_argument('--showbrowser', dest='show_browser', action='store_true')
    parser.add_argument("-l","--log_level")
    
    args = parser.parse_args()
    if args.url:
      url = args.url
    else:
      url = "http://localhost"
    if args.num_loops:
      num_loops = args.num_loops
    else:
      num_loops = 1

    if args.log_level == "DEBUG":
      logging.basicConfig(level=logging.DEBUG)
    elif args.log_level == "WARNING":
      logging.basicConfig(level=logging.WARNING)
    elif args.log_level == "ERROR":
      logging.basicConfig(level=logging.ERROR)
    elif args.log_level == "CRITICAL":
      logging.basicConfig(level=logging.CRITICAL)
    else:
      logging.basicConfig(level=logging.INFO)

    # setup driver
    logging.info("============================================")
    logging.info("url             : " + url)
    logging.info("number of loops : " + str(num_loops))
    logging.info("show browser    : " + str(args.show_browser))
    logging.info("log level       : " + str(args.log_level))
    logging.info("============================================")

    chrome_options = get_chrome_options(args.show_browser)
    desired_capabilities = get_desired_capabilities()
    driver = webdriver.Chrome(options=chrome_options,desired_capabilities=desired_capabilities)  
    driver.implicitly_wait(10)

    # Basic Flow
    for loop in range(0, num_loops): 

      ip = get_random_ip()
      header = { "x-dt-orders": ip }
      logging.debug("Setting x-dt-orders ip to: " + str(header))
      driver.execute_cdp_cmd("Network.enable", {})
      driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": header})

      username = get_random_username()
      userurl =  url + "?username=" + username
      logging.debug("Loop " + str(loop + 1) + " of " + str(num_loops) + "    Running with base URL: " + userurl)
      logging.debug("..Opening Home Page")
      driver.get(userurl)
      assert "Dynatrace Order Processing" in driver.title
      pause("Home")

      logging.debug("..Customer Flow")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Customer"))).click()
      pause("Customer List")
      wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/table/tbody/tr[1]/td[1]/a"))).click()
      pause("First Customer")
      driver.get(url + "?username=" + username)
      #wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home"))).click()
      pause("Home")

      logging.debug("..Catalog Flow")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Catalog"))).click()
      pause("Catalog List")
      wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/table/tbody/tr[1]/td[1]/a"))).click()
      pause("First Catalog Item")
      driver.get(url + "?username=" + username)
      #wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home"))).click()
      pause("Home")

      logging.debug("..Search Item Flow")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Search Items"))).click()
      pause("Search Item Form")
      element = wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "query")))
      element.send_keys("iPod nano")
      element.send_keys(Keys.RETURN)
      pause("Search Item")
      driver.get(url + "?username=" + username)
      #wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home"))).click()
      pause("Home")

      logging.debug("..Order Flow")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Order"))).click()
      pause("Order Home Page")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add Order"))).click()
      pause("Add Order Form")
      wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "addLine"))).click()
      pause("Add Order Line Item")
      driver.get(url + "?username=" + username)
      #wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home"))).click()
      pause("Home")

    # end of loop
    driver.close()
