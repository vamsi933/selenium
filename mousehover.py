from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ Create driver first
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# ✅ Then wait
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(10)

# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(3)

act = ActionChains(driver)

# Hover Admin
admin = driver.find_element(By.XPATH, "//span[normalize-space()='Admin']")
act.move_to_element(admin).perform()

# Hover User Management
usermng = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='User Management']")))
act.move_to_element(usermng).perform()

# Click Users
users = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Users']")))
users.click()

input("Press Enter to close browser...")