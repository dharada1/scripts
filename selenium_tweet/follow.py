# coding: utf-8
from selenium import webdriver
 
def post_twitter(user_name, password, user_id):
   browser = webdriver.Chrome(executable_path="./chromedriver")
   browser.get("https://twitter.com/")
 
   # Login
   mail = browser.find_element_by_name('session[username_or_email]')
   pass_wd = browser.find_element_by_name('session[password]')
   mail.send_keys(user_name)
   pass_wd.send_keys(password)
   pass_wd.submit()
 
   browser.get("https://twitter.com/" + user_id + "/following")

   for button in browser.find_elements_by_class_name("user-actions-follow-button"):
      button.click()
      # TODO
      # selenium.common.exceptions.WebDriverException: Message: unknown error: Element <span class="user-actions-follow-button js-follow-btn follow-button">...</span> is not clickable at point (645, 13). Other element would receive the click: <div class="container">...</div>
   browser.close()
 
if __name__ == "__main__":
   user_id = "hikakin"

   secrets = open(".secrets", "r")
   line = secrets.read().split(" ")
   secrets.close()

   user_name = line[0]
   password  = line[1]

   post_twitter(user_name, password, user_id)
