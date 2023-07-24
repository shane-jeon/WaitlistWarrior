from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://clients.mindbodyonline.com/ASP/su1.asp?studioid=491797&tg=&vt=&lvl=&stype=&view=&trn=0&page=&catid=&prodid=&date=7%2f24%2f2023&classid=0&prodGroupId=&sSU=&optForwardingLink=&qParam=&justloggedin=&nLgIn=&pMode=0&loc=1")

username = 'INSERT YOUR USERNAME/EMAIL'
password = 'INSERT YOUR PASSWORD'

# GO TO CLASSES
classes = driver.find_element('id', 'tabA7')
classes.click()
wait = WebDriverWait(driver, 10)
# LOOK FOR DESIRED CLASS

# TRICKSTER NAME="cid17"
# odd_rows = driver.find_elements(By.CLASS_NAME, '.oddRow')

# print(odd_rows)

test_button_click = driver.find_element(By.NAME, 'but8634')

test_button_click.click()

# # MODAL SIGN IN
wait = WebDriverWait(driver, 10)

username_signin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="su1UserName"]')))
password_signin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="su1Password"]')))
signIn_btn = driver.find_element('id','btnSu1Login')

username_signin.send_keys(username)
password_signin.send_keys(password)
signIn_btn.click()

wait = WebDriverWait(driver, 10)
# h1_element = driver.find_element(By.XPATH, "//div[@id='pageWrapper']//div[@id='wrapper-frame']//div[@id='wrapper-minheight']//div[@id='wrapper-bottompad']//div[@class='wrapper]//div[@id='main-content']//h1")
h1_element = driver.find_element(By.XPATH, '//div[@id="pageWrapper"]//div[@id="wrapper-minheight"]//div[@id="wrapper-bottompad"]//div[@class="wrapper"]//div[@id="main-content"]//*[contains(text(), "Class/Event Full")]')
# h1_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Class/Event Full')]")
h1_text = h1_element.text
print('H1_TEXT')
print(h1_text)
expected_text = "Class/Event Full"

assert expected_text in h1_text, f"Expected text '{expected_text}' not found in the h1 element"

input('Press Enter to close the browser...')
# print(driver.title)
# driver.close()
driver.quit()