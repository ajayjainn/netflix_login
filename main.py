# FIrst install selenium using command, "pip install selenium"
from selenium import webdriver

# Download webdriver for chrome using this link: https://chromedriver.chromium.org/
# Replace the location below with the location of where chromedriver is located.
driver = webdriver.Chrome("D:\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.netflix.com/in/login")

username_field = driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
username_field.send_keys("Username")
# Replace "Username" above with your username.

password_field=driver.find_element_by_xpath('//*[@id="id_password"]')
password_field.send_keys("Password")
# Replace "Password" above with your password.

sumbit_btn = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
sumbit_btn.click()

