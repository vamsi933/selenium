from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://admin-demo.nopcommerce.com/")

driver.implicitly_wait(10)
driver.find_element(By.NAME, "Email").clear()
print("Cleared email field")

driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
print("Cleared password field")
driver.find_element(By.NAME, "Password").send_keys("admin")
driver.find_element(By.XPATH, "//*[@id='main']/div/section/div/div[2]/div[1]/div/form/div[3]/button").click()


print("Login Done")


input("Complete verification manually and press Enter...")

act_title = driver.title
print(act_title)

if "Dashboard" in act_title:
    print("Login test passed")
else:
    print("Login test failed")



input("Press Enter to close browser...")
driver.close()
