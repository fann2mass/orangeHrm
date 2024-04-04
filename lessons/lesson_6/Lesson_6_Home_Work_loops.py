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

list_of_fields = []
items = driver.find_elements(By.CSS_SELECTOR,'label[for]')
time.sleep(5)

for i in items:
    list_of_fields.append(i.text)

print(list_of_fields)

driver.quit()
'''
Homework Assignment: Using Loops
Objective: Open the web application, log in, navigate to the "HR Administration" section via the side menu, and click on the "Add User" button. Once on the "Add User" page, your task is to retrieve and list all the names of input fields relevant to user information, such as employee name, username, etc. Use loops to iterate over elements and gather this information.

Steps:

Open the web application in a browser.
Log into the application with provided credentials.
From the side menu, navigate to the "HR Administration" section.
Click on the "Add User" button, usually represented by a big green button.
On the "Add User" form, identify all input fields related to user information.
Use a loop to iterate over these input fields and collect their names.
Print the list of field names you have collected.
'''
