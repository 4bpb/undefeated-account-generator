from selenium import webdriver
import time
from random import randint
import json


def getCurrentTime():
    return time.strftime("[%H:%M:%S]--------")
gmail      = "@gmail.com"#dont change

with open('config.json') as json_data_file:
	config = json.load(json_data_file)
CONFIG     = config["CONFIG"] 
beggmail   = CONFIG["beggmail"]
first_name =  CONFIG["first_name"]
last_name  = CONFIG["last_name"]
password   = CONFIG["password"]
url        = CONFIG["url"]
accounts   = CONFIG["accounts"]
IP         = CONFIG["IP"]

print("{}Config Loaded".format(getCurrentTime()))
print("{}Using Proxy".format(getCurrentTime()),IP)




#def Login():
#	driver = webdriver.Chrome()
#	driver.implicitly_wait(50)
#	driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
#	driver.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys("")
#	driver.find_element_by_xpath("""//*[@id="identifierNext"]/content/span""").click()
#	driver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys("")
#	time.sleep(1)
#	driver.find_element_by_xpath("""//*[@id="passwordNext"]/content/span""").click()
#	time.sleep(3)


 

def main():
	RGmail = "{}+{}_{}{}".format(beggmail,(randint(0,99)),(randint(0,99)),gmail)
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server='+IP)
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.implicitly_wait(50)
	driver.get(url)
	print("{}Loading Undefeated Inc".format(getCurrentTime()))
	driver.find_element_by_xpath("""//*[@id="email"]""").send_keys(RGmail)
	driver.find_element_by_xpath("""//*[@id="first_name"]""").send_keys(first_name)
	driver.find_element_by_xpath("""//*[@id="last_name"]""").send_keys(last_name)
	driver.find_element_by_xpath("""//*[@id="password"]""").send_keys(password)
	driver.find_element_by_xpath("""//*[@id="create_customer"]/div[6]/input""").click()
	print("{}Success!".format(getCurrentTime()))
	print("{}{}:{}".format(getCurrentTime(), RGmail,password))
	input("{}Press Enter after Captcha to continue...".format(getCurrentTime))
	driver.delete_all_cookies()
	driver.quit()


#Login()
for x in range(50):
	main()
	