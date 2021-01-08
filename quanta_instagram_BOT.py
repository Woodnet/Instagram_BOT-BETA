#
#	Author: Pulsar
#	YouTube: https://www.youtube.com/channel/UCVo0vjlE50dn2LFynrGe9yA
# 	GitHub: https://www.github.com/Woodnet
# 	Twitter: https://twitter.com/7Pulsar
#	Python-Version: Python 3.8.2
#	--> Please write a comment on GitHub-issues.
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time,sys

try:
    os.system("cls") #Windows -default
except Exception:
    os.system("clear") #Linux OS

class Instabot:

    def __init__(self,username,password,firefox_geckodriver):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=firefox_geckodriver)

    def close_bot(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        print("[*] Opening Login-Site..")
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(3)
        print("[+] Login Site has been opened")
        username_elem = driver.find_element_by_xpath("//input[@name='username']")
        username_elem.clear()
        username_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        print("[*] Logging in..")
        time.sleep(3)

    def follow(self, __abo_username):
        driver = self.driver
        try:
            print("[+] Logged in")
            print("[*] Try to get User-Page..")
            driver.get("https://instagram.com/" + __abo_username + "/")
            print("[+] Opened")
            print("\n[*] Following User..")
            try:
                time.sleep(3)
                follow = driver.find_element_by_class_name("_5f5mN       jIbKX  _6VtSN     yZn4P   ")
                print("[+] Following")
            except Exception as e:
                print("[!] Error while searching for element => %s"%(e))
                time.sleep(5)
                exit()
            try:
                follow.click()
            except Exception as e:
                print("[!] Unabled to follow user!")
                time.sleep(5)
            print("[+] Following %s!"%(__abo_username))
        except Exception as e:
            print("ok here is a problem!")
            time.sleep(5)
            exit()

#
password = "[password]" #YOUR PASSWORD
username = "[username]" #YOUR USERNAME
firefox_geckodriver = "" #Path to the Firefox-Geckodriver
#

if __name__ == '__main__':
    print("\n[*] InstaBot has been started!\n")
    __abo_username = input("Username to follow: ")
    print("\n\n")
    bot = Instabot(username, password,firefox_geckodriver)
    bot.login()
    bot.follow(__abo_username)
    enter = input("Press ENTER to close BOT>> ")
    print("[*] Closing Bot..")
    try:
        bot.close_bot()
        print("[+] Closed")
    except Exception as e:
        print("[!] Failure! %s"%(e))
