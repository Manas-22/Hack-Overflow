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