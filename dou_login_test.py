from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchWindowException

login = 'scorecardacc@gmail.com'
password = 'QazxswedC'

browser = webdriver.Firefox()

el_wait = WebDriverWait(browser, 10) #waits until an element will be presented on the page

link = "http://dou.ua"
browser.get(link)

main_window_handle = browser.current_window_handle

def window_switching(base_window_handle): #switching to another tab
	for handle in browser.window_handles:
		if handle != base_window_handle:
			second_window_handle = handle
	browser.switch_to.window(second_window_handle)

	
def logout(): #logouts from account 

	el_wait.until(EC.presence_of_element_located((By.XPATH, "//header[@class='b-head']/div[@class='right-part']/a[@class='min-profile']/img[@class='g-avatar']")))
	
	el = browser.find_element_by_xpath("//header[@class='b-head']/div[@class='right-part']/a[@class='min-profile']/img[@class='g-avatar']")
	el.click()

	el_wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://dou.ua/logout/']")))

	el = browser.find_element_by_xpath("//a[@href='http://dou.ua/logout/']")
	el.click()
	print('Click logout')


def login_by_facebook(login, password, basehandle): 
	
	print('DOU test: Login by Facebook')

	el_wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='login-link']")))
	el = browser.find_element_by_xpath("//a[@id='login-link']")
	el.click()
	el = browser.find_element_by_xpath("//div[@class='login-button btnFb']")
	el.click()
	
	window_switching(basehandle) 

	el_wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))

	el = browser.find_element_by_xpath("//input[@id='email']")
	el.send_keys(login)
	el = browser.find_element_by_xpath("//input[@id='pass']")
	el.send_keys(password)
	el = browser.find_element_by_xpath("//div[@id='login_button_inline']/label[@id='loginbutton']")
	el.click()

	browser.switch_to.window(basehandle) #back to base tab
	print ('Logined')
	logout()
	print ('Test completed successfuly ')
	
def login_by_google(login, password, basehandle):

	print('DOU test: Login by Google')

	el_wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='login-link']")))

	el = browser.find_element_by_xpath("//a[@id='login-link']")
	el.click()
	el = browser.find_element_by_xpath("//div[@class='login-button btnGoogle']")
	el.click()

	window_switching(basehandle)

	el_wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='Email']")))

	el = browser.find_element_by_xpath("//input[@id='Email']")
	el.send_keys(login)
	el = browser.find_element_by_xpath("//input[@id='Passwd']")
	el.send_keys(password)
	el = browser.find_element_by_xpath("//input[@name='signIn']")
	el.click()
	
	browser.switch_to.window(basehandle) #back to base tab
	print ('Logined')
	logout()
	print ('Test completed successfuly ')
	
def login_by_linkedin(login, password, basehandle):

	print('DOU test: Login by LinkedIn')

	el_wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='login-link']")))

	el = browser.find_element_by_xpath("//a[@id='login-link']")
	el.click()
	el = browser.find_element_by_xpath("//div[@class='login-button btnLin']")
	el.click()

	window_switching(basehandle)

	el_wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='session_key-oauthAuthorizeForm']")))

	el = browser.find_element_by_xpath("//input[@id='session_key-oauthAuthorizeForm']")
	el.send_keys(login)
	el = browser.find_element_by_xpath("//input[@id='session_password-oauthAuthorizeForm']")
	el.send_keys(password)
	el = browser.find_element_by_xpath("//input[@name='authorize']")
	el.click()

	try: #if error appears
		browser.find_element_by_xpath("//div[@id='global-error']/div[@id='yui-gen1']")
		
		el = browser.find_element_by_xpath("//input[@id='session_password-oauthAuthorizeForm']")
		el.send_keys(password)
		el = browser.find_element_by_xpath("//input[@name='authorize']")
		el.click()
	except NoSuchWindowException: 
		a = 0

	browser.switch_to.window(basehandle) #back to base tab
	print ('Logined')
	logout()	
	print ('Test completed successfuly ')

def login_by_vk(login, password, basehandle):

	print('DOU test: Login by VK')

	el_wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='login-link']")))

	el = browser.find_element_by_xpath("//a[@id='login-link']")
	el.click()
	el = browser.find_element_by_xpath("//div[@class='login-button btnLoginVk']")
	el.click()

	window_switching(main_window_handle)
	
	sleep(3)
	
	el_wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='box']/div[@class='info']/input[@name='email']")))

	el = browser.find_element_by_xpath("//div[@id='box']/div[@class='info']/input[@name='email']")
	el.send_keys(login)
	el = browser.find_element_by_xpath("//div[@class='info']/input[@name='pass']")
	el.send_keys(password)
	el = browser.find_element_by_xpath("//button[@id='install_allow']")
	el.click()

	browser.switch_to.window(main_window_handle) #back to base tab
	print ('Logined')
	logout()
	print ('Test completed successfuly ')

def login_by_email(login, password):
	
	print('DOU test: Login by e-mail')
	
	el_wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='login-link']")))
	
	el = browser.find_element_by_xpath("//a[@id='login-link']")
	el.click()
	el = browser.find_element_by_xpath("//a[@id='_loginByMail']")
	el.click()


	el_wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
	
	el = browser.find_element_by_xpath("//input[@name='username']")
	el.send_keys(login)
	el = browser.find_element_by_xpath("//input[@name='password']")
	el.send_keys(password)
	el = browser.find_element_by_xpath("//button[@class='big-button btnSubmit']")
	el.click()
	print ('Logined')
	logout()
	print ('Test completed successfuly ')

	
login_by_facebook(login, password, main_window_handle)

login_by_google(login, password, main_window_handle)

login_by_linkedin(login, password, main_window_handle)
	
login_by_vk(login, password, main_window_handle)

""""because registration by email now is closed 
you need to enter your personal e-mail and password, 
that is registrated on DOU"""

login = raw_input("Please, enter your e-mail: ")
password = raw_input("Please, enter your password: ")
	
login_by_email(login, password)

browser.close()

print("All login tests completed successfully")