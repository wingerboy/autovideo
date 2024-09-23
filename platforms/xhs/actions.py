# language: platforms/xiaohongshu/actions.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from logs.logger import setup_logger

class XiaohongshuActions:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.logger = setup_logger('xiaohongshu_actions_logger', 'logs/xiaohongshu_actions.log')

    def login(self, username, password):
        self.logger.info("Logging in to Xiaohongshu")
        self.driver.get("https://www.xiaohongshu.com/login")
        time.sleep(2)
        
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(5)
        self.logger.info("Logged in to Xiaohongshu")

    def post_content(self, content):
        self.logger.info("Posting content to Xiaohongshu")
        self.driver.get("https://www.xiaohongshu.com/post")
        time.sleep(2)
        
        self.driver.find_element(By.NAME, "content").send_keys(content)
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(5)
        self.logger.info("Content posted to Xiaohongshu")

    def auto_reply(self, post_url, reply_content):
        self.logger.info(f"Auto replying to post: {post_url}")
        self.driver.get(post_url)
        time.sleep(2)
        
        self.driver.find_element(By.NAME, "reply").send_keys(reply_content)
        self.driver.find_element(By.NAME, "reply").send_keys(Keys.RETURN)
        time.sleep(2)
        self.logger.info("Auto reply sent")

    def auto_private_message(self, user_url, message_content):
        self.logger.info(f"Sending private message to user: {user_url}")
        self.driver.get(user_url)
        time.sleep(2)
        
        self.driver.find_element(By.NAME, "message").send_keys(message_content)
        self.driver.find_element(By.NAME, "message").send_keys(Keys.RETURN)
        time.sleep(2)
        self.logger.info("Private message sent")

    def search_content(self, query):
        self.logger.info(f"Searching content with query: {query}")
        self.driver.get("https://www.xiaohongshu.com/search")
        time.sleep(2)
        
        self.driver.find_element(By.NAME, "search").send_keys(query)
        self.driver.find_element(By.NAME, "search").send_keys(Keys.RETURN)
        time.sleep(2)
        self.logger.info("Search completed")

    def follow_user(self, user_url):
        self.logger.info(f"Following user: {user_url}")
        self.driver.get(user_url)
        time.sleep(2)
        
        self.driver.find_element(By.NAME, "follow").click()
        time.sleep(2)
        self.logger.info("User followed")

    def like_post(self, post_url):
        self.logger.info(f"Liking post: {post_url}")
        self.driver.get(post_url)
        time.sleep(2)
        
        self.driver.find_element(By.NAME, "like").click()
        time.sleep(2)
        self.logger.info("Post liked")

    def comment_post(self, post_url, comment_content):
        self.logger.info(f"Commenting on post: {post_url}")
        self.driver.get(post_url)
        time.sleep(2)
        
        self.driver.find_element(By.NAME, "comment").send_keys(comment_content)
        self.driver.find_element(By.NAME, "comment").send_keys(Keys.RETURN)
        time.sleep(2)
        self.logger.info("Comment posted")

    def close(self):
        self.logger.info("Closing browser")
        self.driver.quit()