import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Where you want to search")
print("1- FACEBOOK ")
print("2- INSTAGRAM")
print("3- LINKEDIN ")
print("4- GOOGLE")

a=input("Press the desired key ")

if a is "1":
			new =2
			tabUrl="https://www.facebook.com/search/top/?q="
			term=input("Enter search query ")

			webbrowser.open(tabUrl+term,new=new)


elif a is "2":
			new =2
			tabUrl="https://www.instagram.com/"
			term=input("Enter search query{Please Enter exact Username} ")

			webbrowser.open(tabUrl+term,new=new)


elif a is "3":
			new =2
			tabUrl="https://www.linkedin.com/search/results/index/?keywords="
			term=input("Enter search query ")

			webbrowser.open(tabUrl+term,new=new)


else :
			print("Which type of google search")
			print("1- TEXT")
			print("2- IMAGE")
			
			c=input("Press the desired key ")

			if c is "1":
						new =2
						tabUrl="http://google.com/?#q="
						term=input("Enter search query ")

						webbrowser.open(tabUrl+term,new=new)

			else :
						print("How you want to search")
						print("1- By URL")
						print("2 Upload Image")

						d=input("Press the desired key ")

						if d is "1":
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
