# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# driver.get("https://testautomationpractice.blogspot.com/")

# no_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
# no_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//th"))
# print("Number of rows: ", no_of_rows)
# print("Number of columns: ", no_of_columns)

# #specific row and column data
# data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[2]//td[1]").text
# print(data)

# data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[3]//td[1]").text
# print(data)

# #all data of the table
# for r in range(2, no_of_rows + 1):
#     for c in range(1, no_of_columns + 1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]//td[" + str(c) + "]").text
#         print(data, end=" ")
#     print()  # for new line after each row

# input("Press Enter to close browser...")







#another 2 way to print all data of the table

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(10)
#driver.minimize_window()

# find the table element
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)   




driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']").click()
time.sleep(3)

rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
columns = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']//div[@role='cell']")
print("Number of rows: ", len(rows))
print("Number of columns: ", len(columns))

input("Press Enter to close browser...")