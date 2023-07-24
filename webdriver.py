from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://clients.mindbodyonline.com/ASP/su1.asp?studioid=491797&tg=&vt=&lvl=&stype=&view=&trn=0&page=&catid=&prodid=&date=7%2f24%2f2023&classid=0&prodGroupId=&sSU=&optForwardingLink=&qParam=&justloggedin=&nLgIn=&pMode=0&loc=1")

input('Press Enter to close the browser...')
print(driver.title)
# driver.close()
driver.quit()