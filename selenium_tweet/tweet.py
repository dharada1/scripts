# coding: utf-8
from selenium import webdriver
 
def post_twitter( user_name, password):
   # chromedriver落としてきて同じディレクトリに配置。
   browser = webdriver.Chrome(executable_path="./chromedriver")
   browser.get("https://twitter.com/")
 
   # Login
   mail = browser.find_element_by_name('session[username_or_email]')
   pass_wd = browser.find_element_by_name('session[password]')
   mail.send_keys(user_name)
   pass_wd.send_keys(password)
   pass_wd.submit()
 
   # ツイートの処理
   from datetime import datetime
   post_body = browser.find_element_by_id("tweet-box-home-timeline")
   post_body.send_keys("Python test: "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
   try:
      post_button = browser.find_element_by_css_selector("button.tweet-action")
      post_button.click()
      print("ツイート成功")
   except:
      print("ツイート失敗")
 
   browser.close()
 
if __name__ == "__main__":
   from getpass import getpass
   name = input("user name : ")
   pw = getpass("password  : ")
   post_twitter(name, pw)
