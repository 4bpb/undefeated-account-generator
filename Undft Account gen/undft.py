from selenium import webdriver
import time
from random import randint
#made by turtl aka snupreme #seleniumgang
##############################
beggmail = "johnsmith"#this is the start of your email before the @
gmail = "@gmail.com"#dont change
first_name = ""
last_name = ""
password = ""
url = "https://shop.undefeated.com/account/register"
accounts =  3 # number of accounts youd like to make
##############################



def getCurrentTime():
    return time.strftime("[%H:%M:%S]")

print("{}   Starting Undefeated Account Generator by turtl aka snupreme".format(getCurrentTime()))
print("{}   DONT FORGET TO ADD YOUR INFO IN THE SCRIPT!".format(getCurrentTime()))



driver = webdriver.Chrome()
driver.implicitly_wait(50)


                                        
count = 0 
while count < accounts:
	driver.delete_all_cookies()
	driver.get(url)
	driver.find_element_by_xpath("""//*[@id="email"]""").send_keys("{}+{}{}".format(beggmail,(randint(1,444)),gmail))
	driver.find_element_by_xpath("""//*[@id="first_name"]""").send_keys(first_name)
	driver.find_element_by_xpath("""//*[@id="last_name"]""").send_keys(last_name)
	driver.find_element_by_xpath("""//*[@id="password"]""").send_keys(password)
	driver.find_element_by_xpath("""//*[@id="create_customer"]/div[6]/input""").click()
	input("Press Enter To Continue After Solving Captcha...")


