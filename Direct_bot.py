# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time, random

# # Username and password of your instagram account:
# my_username = 'xmen_naruto'
# my_password = 'hentai'

# # Instagram username list for DM:
# usernames = ['user1', 'user2', 'user3']

# # Messages:
# messages = ['Hey! Pls follow my page', 'Hey, how you doing?', 'Hey']

# # Delay time between messages in sec:
# between_messages = 2000

# browser = webdriver.Chrome('chromedriver')

# # Authorization:
# def auth(username, password):
# 	try:
# 		browser.get('https://instagram.com')
# 		time.sleep(random.randrange(2,4))

# 		input_username = browser.find_element_by_name('username')
# 		input_password = browser.find_element_by_name('password')

# 		input_username.send_keys(username)
# 		time.sleep(random.randrange(1,2))
# 		input_password.send_keys(password)
# 		time.sleep(random.randrange(1,2))
# 		input_password.send_keys(Keys.ENTER)

# 	except Exception as err:
# 		print(err)
# 		browser.quit()

# auth(my_username,my_password)

# #save your login info?
# time.sleep(10)
# notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
# #turn on notif
# time.sleep(10)
# notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time, random

# # Username and password of your instagram account:
# my_username = 'xmen_naruto'
# my_password = 'hentai'

# # Instagram username list for DM:
# usernames = ['user1', 'user2', 'user3']

# # Messages:
# messages = ['Hey! Pls follow my page', 'Hey, how you doing?', 'Hey']

# # Delay time between messages in sec:
# between_messages = 2000

# browser = webdriver.Chrome('chromedriver')

# # Authorization:
# def auth(username, password):
# 	try:
# 		browser.get('https://instagram.com')
# 		time.sleep(random.randrange(2,4))

# 		input_username = browser.find_element_by_name('username')
# 		input_password = browser.find_element_by_name('password')

# 		input_username.send_keys(username)
# 		time.sleep(random.randrange(1,2))
# 		input_password.send_keys(password)
# 		time.sleep(random.randrange(1,2))
# 		input_password.send_keys(Keys.ENTER)

# 	except Exception as err:
# 		print(err)
# 		browser.quit()

# auth(my_username,my_password)

# #save your login info?
# time.sleep(10)
# notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
# #turn on notif
# time.sleep(10)
# notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time, random

# # Username and password of your instagram account:
# my_username = 'xmen_naruto'
# my_password = 'hentai'

# # Instagram username list for DM:
# usernames = ['sujeetkumarrath', 'mac_max22', 'prince.sai']

# # Messages:
# messages = ['Hey! Pls follow my page', 'Hey, how you doing?', 'Hey']

# # Delay time between messages in sec:
# between_messages = 2000

# browser = webdriver.Chrome('chromedriver')

# # Authorization:
# def auth(username, password):
# 	try:
# 		browser.get('https://instagram.com')
# 		time.sleep(random.randrange(2,4))

# 		input_username = browser.find_element_by_name('username')
# 		input_password = browser.find_element_by_name('password')

# 		input_username.send_keys(username)
# 		time.sleep(random.randrange(1,2))
# 		input_password.send_keys(password)
# 		time.sleep(random.randrange(1,2))
# 		input_password.send_keys(Keys.ENTER)

# 		browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
# 		time.sleep(random.randrange(1,2))

# 		browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
# 		time.sleep(random.randrange(1,2))

# 	except Exception as err:
# 		print(err)
# 		browser.quit()

# # Sending messages:
# def send_message(users, messages):
# 	try:
# 		#browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
# 		#time.sleep(random.randrange(3,5))
# 		browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
# 		time.sleep(random.randrange(1,2))
		
# 		# browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
# 		# for user in users:
# 		# 	time.sleep(random.randrange(1,2))
# 		# 	browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
# 		# 	time.sleep(random.randrange(2,3))
# 		# 	browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]').find_element_by_tag_name('button').click()
# 		# 	time.sleep(random.randrange(3,4))
# 		# 	browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
# 		# 	time.sleep(random.randrange(3,4))
# 		# 	text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
# 		# 	text_area.send_keys(random.choice(messages))
# 		# 	time.sleep(random.randrange(2,4))
# 		# 	text_area.send_keys(Keys.ENTER)
# 		# 	print(f'Message successfully sent to {user}')
# 		# 	time.sleep(between_messages)
# 		# 	browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click() 
			

# 	except Exception as err:
# 		print(err)
# 		browser.quit()


# auth(my_username, my_password)
# time.sleep(random.randrange(2,4))
# send_message(usernames, messages)



# from selenium import webdriver
# import time

# browser = webdriver.Chrome(r'C:\Users\Sujeet\Desktop\Direct_bot\chromedriver.exe')
# browser.get('https://instagram.com/')
# time.sleep(3)

# #Automate Login
# def login():
# 	Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
# 	Username.send_keys("xmen_naruto")
# 	time.sleep(2)
# 	password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
# 	password.send_keys("hentai")
# 	password.submit()
# 	time.sleep(2)
# login()

# browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
# time.sleep(random.randrange(1,2))
# browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
# time.sleep(random.randrange(1,2))

from selenium import webdriver
import time , random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
timeout = 7
msg = 'As we respect your online market security so we are also aware of your interest. We present the best of products in the market for you at the convenience price so that you can get the product at the easiest.'


browser = webdriver.Chrome(r'C:\Users\Sujeet\Desktop\Direct_bot\chromedriver.exe')
browser.get('https://instagram.com/')
time.sleep(random.randrange(2,4))
Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
Username.send_keys("dmb79672022")
time.sleep(random.randrange(2,4))
password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("dev@123")
password.submit()
time.sleep(random.randrange(7,10))

#not save info
#WebDriverWait(driver, timeout).until(element_present)

try :
    Notnow=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
    
    time.sleep(random.randrange(7,10))

    Noti=WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]'))).click()
    #time.sleep(random.randrange(7,10))
except NoSuchElementException as err:
    print(err)    



#Hashtag_Search
#link = "https://www.instagram.com/p/CbkSgp1rDOL/?utm_medium=copy_link"
finally:
    time.sleep(random.randrange(2,3))
    searchbox = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    searchbox.clear()
    searchbox.send_keys("cloth")
    time.sleep(random.randrange(3,4))
    searchbox.send_keys(Keys.ENTER)
    time.sleep(random.randrange(3,4))
    searchbox.send_keys(Keys.ENTER)

    time.sleep(random.randrange(7,10))
    poat_select = browser.find_element_by_class_name("_9AhH0").click()
    #poat_select = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[4]/article/div[1]/div/div[1]/div[1]/a/div/div[2]").click()
    time.sleep(random.randrange(7,10))

    find_likers = browser.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[3]/div/div/section[2]/div/div/div/a[2]/div").click()
    #find_likers = browser.find_element_by_class_name("_7UhW9   xLCgt        qyrsm KV-D4              fDxYl    T0kll ").click()
    time.sleep(random.randrange(7,10))

    ##1st liker
    liker_1st = browser.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/div/div/div[1]/div[2]/div/div/span/a/span").click()
    #liker_1st = browser.find_element_by_class_name("_7UhW9   xLCgt        qyrsm KV-D4           se6yk       T0kll ").click()
    time.sleep(random.randrange(7,10))

    liker_1st_inbox = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/div/div[1]/button").click()
    time.sleep(random.randrange(7,10))

    liker_1st_msg = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    liker_1st_msg.send_keys(msg)
    time.sleep(random.randrange(3,4))
    liker_1st_msg.send_keys(Keys.ENTER)
    print(f"message sent sucessfully")
    
    #comment_onpost = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[3]/div/div/section[1]/span[2]/button").click()
    #time.sleep(random.randrange(3,4))
    # commentbox = browser.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[3]/div/div/section[3]/div/form/textarea")
    # commentbox.clear()
    # commentbox.send_keys(msg)
    # time.sleep(random.randrange(3,4))
    # commentbox.send_keys(Keys.ENTER)



