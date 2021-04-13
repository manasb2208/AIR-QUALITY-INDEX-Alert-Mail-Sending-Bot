cd = "C:\\Users\\Manas\\Desktop\\chromedriver.exe" #chrome driver path
import time
import pandas as pd # for the beautiful soup we have to send the source code for the page.
from selenium import webdriver
import smtplib, ssl
browser=webdriver.Chrome(cd)

browser.get("https://www.aqi.in/dashboard/india/west-bengal/kolkata")

time.sleep(5)
a=browser.find_element_by_xpath('//div[@class="sectot-box-left"]')
aqi=a.find_element_by_xpath('//h2[@style="color:#d4cc0f"]').text
aqi = int(aqi)
print(aqi)

if aqi<100:
	print("AQI is "+str(aqi)+". It is moderate, no need to send email")
	#message = "AQI is moderate"
else:
	if aqi>=100 and aqi<200:
		message="The AQI value is {}. The AQI is poor ".format(aqi)
	elif aqi>=200 and aqi<300:
		message="The AQI value is {}. The AQI is unhealthy ".format(aqi)
	elif aqi>=300 and aqi<400:
		message="The AQI value is {}. The AQI is severe ".format(aqi)
	elif aqi>=400 and aqi<500:
		message="The AQI value is {}. The AQI is hazardous ".format(aqi)

	smtp_server = "smtp.gmail.com"
	port = 587  # For starttls
	sender_email = "mymail@gmail.com"
	receiver_email = ["frind1mail@gmail.com","friend2mail@gmail.com", "friend3mail@gmail.com"]
	password = input('Enter the password: ')

	context = ssl.create_default_context()

	server = smtplib.SMTP(smtp_server,port)
	server.starttls(context=context) # Secure the connection
	server.login(sender_email, password)
	time.sleep(5)
	server.sendmail(sender_email, receiver_email, message)
	print('Email alert has been sent')
	server.quit()

browser.quit()