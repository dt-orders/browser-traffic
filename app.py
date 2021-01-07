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

def get_geolocation():
  # https://stackoverflow.com/questions/31755633/fake-geolocation-in-chrome-automation
  # https://developers.google.com/web/tools/chrome-devtools/device-mode/geolocation
  location = random.randint(1,5)
  if location == 1:
    print("Setting Location to: Frankfurt")
    latitude = 50.1109
    longitude = 8.6821
  elif location == 2:
    print("Setting Location to: Berlin")
    latitude = 52.520007
    longitude = 13.404954
  elif location == 3:
    print("Setting Location to: London")
    latitude = 51.507351
    longitude = -0.127758
  elif location == 4:
    print("Setting Location to: San Fran")
    latitude = 37.774929
    longitude = -122.419416
  else:
    print("Setting Location to: Mumbai")
    latitude = 19.075984
    longitude = 72.877656

  return {
    "latitude": latitude,
    "longitude": longitude,
    "accuracy": 100
  }
    
def get_desired_capabilities():

  desired_capabilities = DesiredCapabilities.CHROME.copy()
  desired_capabilities['chrome.page.customHeaders.host'] = 'test.local'
  return desired_capabilities

def get_chrome_options(show_browser) -> None:
    chrome_options = Options()
    if(show_browser==False):
      print("Hiding Browser")
      chrome_options.add_argument("--headless")
    else:
      print("Showing Browser")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1200x600")
    chrome_options.add_argument("user-agent=whatever you want")
    chrome_options.add_argument("custom=rob jahn")
    #chrome_options.add_argument('--deny-permission-prompts')
    #chrome_options.add_argument("disable-geolocation")
    
    #prefs = {"profile.default_content_setting_values.geolocation" :2}
    #chrome_options.add_experimental_option("prefs",prefs)

    return chrome_options

def pause():
  time.sleep(2)

if __name__ == "__main__":

    # process args
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url",help="The base URL for the script. default is http://localhost")
    parser.add_argument("-n","--num_loops", type=int, help="Number of loops for the script to repeat.  Default is 1")
    parser.add_argument('--show', dest='show', action='store_true')
    
    args = parser.parse_args()
    if args.url:
      url = args.url
    else:
      url = "http://localhost"
    if args.num_loops:
      num_loops = args.num_loops
    else:
      num_loops = 1

    # setup driver
    print("============================================")
    print("url             : " + url)
    print("number of loops : " + str(num_loops))
    print("show browser    : " + str(args.show))
    print("============================================")

    chrome_options = get_chrome_options(args.show)
    desired_capabilities = get_desired_capabilities()
    driver = webdriver.Chrome(options=chrome_options,desired_capabilities=desired_capabilities)  

    #driver.implicitly_wait(10)

    # Basic Flow
    for loop in range(0, num_loops): 
      #location = get_geolocation()
      #driver.execute_cdp_cmd("Page.setGeolocationOverride", location)
      #driver.execute_cdp_cmd("Emulation.setGeolocationOverride", location)

      #driver.get("https://maps.google.com")
      #wait(driver, 10).until(EC.presence_of_element_located((By.ID, "widget-mylocation"))).click()
      #pause()

      print("Loop " + str(loop + 1) + " of " + str(num_loops) + "    Running with base URL: " + url)
      print("..Opening Home Page")
      driver.get(url)
      assert "Dynatrace Order Processing" in driver.title
      #pause()
      pause()
      pause()
      pause()
      pause()
      #print(driver.page_source)

      print("..Customer Flow")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Customer"))).click()
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/table/tbody/tr[1]/td[1]/a"))).click()
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home"))).click()
      pause()
      break
      """
      driver.find_element_by_link_text("Customer").click()
      pause()
      # first Link to detail record in the table
      driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[1]/a").click()
      pause()
      driver.find_element_by_link_text("Home").click()
      pause()
      """

      print("..Catalog Flow")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Catalog"))).click()
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/table/tbody/tr[1]/td[1]/a"))).click()
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home"))).click()
      pause()
      """
      driver.find_element_by_link_text("Catalog").click()
      pause()
      # first Link to detail record in the table
      driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[1]/a").click()
      pause()
      driver.find_element_by_link_text("Home").click()
      pause()
      """

      print("..Search Item Flow")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Search Items"))).click()
      pause()
      element = wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "query")))
      element.send_keys("iPod nano")
      element.send_keys(Keys.RETURN)
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home"))).click()
      pause()
      """
      driver.find_element_by_link_text("Search Items").click()
      pause()
      elem = driver.find_element_by_name("query")
      elem.clear()
      elem.send_keys("iPod nano")
      elem.send_keys(Keys.RETURN)
      pause()
      driver.find_element_by_link_text("Home").click()
      pause()
      """

      print("..Order Flow")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Order"))).click()
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add Order"))).click()
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "addLine"))).click()
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home"))).click()
      pause()
      """
      driver.find_element_by_link_text("Order").click()
      pause()
      driver.find_element_by_link_text("Add Order").click()
      pause()
      driver.find_element_by_name("addLine").click()    
      pause()
      driver.find_element_by_link_text("Home").click()
      pause()
      """

    # end of loop
    #driver.close()
