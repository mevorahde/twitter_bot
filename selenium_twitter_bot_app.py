from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
from pathlib import Path

# Activate '.env' file
load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Twitter_Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        time.sleep(3)
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q=%23" + hashtag + "&src=typeahead_click")
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            tweets = bot.find_elements(By.XPATH, '//*[@data-testid="tweet"]//a[@dir="auto"]')
            links = [elem.get_attribute('href') for elem in tweets]
            for link in links:
                bot.get(link)
            try:
                # 'liking' a tweet, doesn't work. Need to find the latest element/XPATH for the heart.
                bot.find_elements(By.XPATH, '//*[@data-testid="like"]//a[@dir="ltr"]')
                time.sleep(10)
            except Exception as ex:
                time.sleep(60)


david = Twitter_Bot(os.getenv("t_username"), os.getenv("t_password"))
david.login()
david.like_tweet("100DaysOfCode")


