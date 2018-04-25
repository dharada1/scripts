# coding: utf-8
from selenium import webdriver
 
def post_twitter( user_name, password, user_id):
   # chromedriver落としてきて同じディレクトリに配置。
   browser = webdriver.Chrome(executable_path="./chromedriver")
   browser.get("https://twitter.com/")
 
   # Login
   mail = browser.find_element_by_name('session[username_or_email]')
   pass_wd = browser.find_element_by_name('session[password]')
   mail.send_keys(user_name)
   pass_wd.send_keys(password)
   pass_wd.submit()
 
   browser.get("https://twitter.com/" + user_id)
   browser.close()
 
if __name__ == "__main__":
   from getpass import getpass
   user_id = input("who to open :")


   test_data = open(".secrets", "r")
   contents = test_data.read().split(" ")
   test_data.close()

   post_twitter(contents[0], contents[1], user_id)
