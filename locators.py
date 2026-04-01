'''from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/")


driver.implicitly_wait(10)
driver.minimize_window()

driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
print("Login Done")


#link test and partial link test

driver.find_element(By. LINK_TEXT, "Forgot your password?").click()


driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()


input("Press Enter to close browser...")
'''


#class name and tag name

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://facebook.com/")


driver.implicitly_wait(10)
driver.minimize_window()

driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("your_email")
input("Press Enter to close browser...")




#relative xptha

