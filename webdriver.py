from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://clients.mindbodyonline.com/ASP/su1.asp?studioid=491797&tg=&vt=&lvl=&stype=&view=&trn=0&page=&catid=&prodid=&date=7%2f24%2f2023&classid=0&prodGroupId=&sSU=&optForwardingLink=&qParam=&justloggedin=&nLgIn=&pMode=0&loc=1")

username = 'INSERT YOUR USERNAME/EMAIL'
password = 'INSERT YOUR PASSWORD'
# SIGN IN
username_signin = driver.find_element('id','su1UserName')
password_signin = driver.find_element('id','su1Password')
signIn_btn = driver.find_element('id','btnSu1Login')

username_signin.send_keys(username)
password_signin.send_keys(password)
signIn_btn.click()

# GO TO CLASSES
classes = driver.find_element('id', 'tabA7')
classes.click()

# LOOK FOR DESIRED CLASS
# TRICKSTER NAME="cid17"


input('Press Enter to close the browser...')
print(driver.title)
# driver.close()
driver.quit()