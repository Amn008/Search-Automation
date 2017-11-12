from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("How you want to search")
print("1- By URL")
print("2 Upload Image")

a = input("Press the desired key\n")

if a is "1":
	term=input("Paste the URL here  ")

	driver = webdriver.Chrome("Z:\python\chromedriver.exe")
	driver.get('https://www.images.google.com')
	driver.find_element_by_xpath('.//*[@id="qbi"]').click()

	driver.find_element_by_xpath('.//*[@id="qbui"]').send_keys(term)

	driver.find_element_by_xpath('.//*[@id="qbbtc"]/input').click()

else:
	driver = webdriver.Chrome("Z:\python\chromedriver.exe")
	driver.get('https://www.images.google.com')
	driver.find_element_by_xpath('.//*[@id="qbi"]').click()

	driver.find_element_by_xpath('.//*[@id="qbug"]/div/a').click()

	driver.find_element_by_xpath('.//*[@id="qbfile"]').click()
