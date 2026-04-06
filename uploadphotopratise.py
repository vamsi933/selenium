from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(10)

# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
print("Login Done")

# Open PIM
driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
time.sleep(2)

# Add Employee
driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
time.sleep(2)

# 🔥 REMOVE CLICK → directly upload
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
    r"C:\Users\Vamsi\OneDrive\Pictures\Screenshots\Screenshot 2024-07-09 102546.png"
)

print("Photo Uploaded")


driver.find_element(By.NAME, "firstName").send_keys("Vamsi")
driver.find_element(By.NAME, "middleName").send_keys("Kumar")
driver.find_element(By.NAME, "lastName").send_keys("Reddy")


driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
print("Employee Added")


input("Press Enter to close browser...")