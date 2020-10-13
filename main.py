from selenium import webdriver

driver = webdriver.Chrome("D:\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.netflix.com/in/login")

username_field = driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
username_field.send_keys("Username")

password_field=driver.find_element_by_xpath('//*[@id="id_password"]')
password_field.send_keys("Password")

sumbit_btn = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
sumbit_btn.click()

