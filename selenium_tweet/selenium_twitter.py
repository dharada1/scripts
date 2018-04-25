# http://www.takunoko.com/blog/pythonselenium%E3%81%A7twitter%E3%81%AB%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B/
# ↑かんたんに改変したやつ。

# coding: utf-8
# Twitter Webにログインしてツイートしてみる
# seleniumの練習
from selenium import webdriver
 
def post_twitter( user_name, password):
   # chromedriver落としてきて同じディレクトリに配置。
   browser = webdriver.Chrome(executable_path="./chromedriver")
   browser.get("https://twitter.com/")
 
   # ログイン処理
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
      # この時点で、他の操作をするとなんだか失敗するみたい。
   except:
      print("ツイート失敗")
 
   browser.close()
 
if __name__ == "__main__":
   from getpass import getpass
   name = input("user name : ")
   pw = getpass("password  : ")
   post_twitter(name, pw)
