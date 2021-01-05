from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import argparse
import time 
import sys

def set_chrome_options(show_browser) -> None:
    chrome_options = Options()
    if(show_browser==False):
      print("Hiding Browser")
      chrome_options.add_argument("--headless")
    else:
      print("Showing Browser")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1200x600")
    #chrome_prefs = {}
    #chrome_options.experimental_options["prefs"] = chrome_prefs
    #chrome_prefs["profile.default_content_settings"] = {"images": 2}
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

    chrome_options = set_chrome_options(args.show)
    driver = webdriver.Chrome(options=chrome_options)
    #driver.implicitly_wait(10)

    # Basic Flow
    for loop in range(0, num_loops): 

      print("Loop " + str(loop + 1) + " of " + str(num_loops) + "    Running with base URL: " + url)
      print("..Opening Home Page")
      driver.get(url)
      assert "Dynatrace Order Processing" in driver.title
      #pause()
      #print(driver.page_source)

      print("..Customer Flow")
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Customer"))).click()
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/table/tbody/tr[1]/td[1]/a"))).click()
      pause()
      wait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home"))).click()
      pause()

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
    driver.close()
