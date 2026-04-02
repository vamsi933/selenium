
""" example :- 

first open the website https://testautomationpractice.blogspot.com/ and go to search bar and type
'Selenium' and click on search button and to see some resut each result will be opened in new tab and 
then find id of each website and print it in console and then close the browser.'''
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://testautomationpractice.blogspot.com/")

# search for 'Selenium' in search bar and click on search button
driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Selenium")
driver.find_element(By.CLASS_NAME, "wikipedia-search-button").click()


# find all the search results and open each result in new tab
time.sleep(3)  # wait for results

result = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']//a")

links = []
for r in result:
    links.append(r.get_attribute("href"))

for link in links:
    driver.execute_script("window.open(arguments[0]);", link)

#find id of each website and print it in console
time.sleep(3)  # wait for all tabs to open

    
print(driver.window_handles)  # print all window handles (ids)

#switching to each tab and printing the title of each tab
for handle in driver.window_handles:
    driver.implicitly_wait(5)  # wait for the page to load
    driver.switch_to.window(handle)
    print(driver.title)


input("Press Enter to close browser...")


