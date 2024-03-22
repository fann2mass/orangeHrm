from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://portnov_admin-trials711.orangehrmlive.com/client/#/dashboard")

driver.find_element(By.CSS_SELECTOR, "input[id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[id='txtPassword']").send_keys("qTJn5@5APu")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)
driver.find_element(By.XPATH, "//li[@id='left_menu_item_10']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@data-tooltip='Add User']/a").click()
time.sleep(5)


driver.find_element(By.XPATH, "//label[contains(text(),'Disabled')]").click()
time.sleep(5)

if driver.find_element(By.XPATH, "//label[contains(text(),'Disabled')]").is_enabled():
   driver.find_element(By.XPATH, "//label[contains(text(),'Enabled')]")

driver.quit()
'''
Homework Assignment: Applying Conditions
Objective: Perform the same initial steps as the previous assignment to log into the application and navigate to the "Add User" page. Instead of listing input fields, you will find the user status option (which by default is set to "Enabled"). If the status is not set to "Disabled," change it to "Disabled." This task requires you to apply conditions to interact with web elements.

Steps:

Open the web application in a browser.
Log into the application with provided credentials.
From the side menu, navigate to the "HR Administration" section.
Click on the "Add User" button.
Locate the user status option on the "Add User" form.
Check the current status of the user. If it is not "Disabled," you need to select the "Disabled" option.
Ensure your script can handle both conditions: if the status is already "Disabled," it remains unchanged; otherwise, change it to "Disabled."
'''
