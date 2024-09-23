# language: platforms/xiaohongshu/bot.py
from .actions import XiaohongshuActions
from .api import XiaohongshuAPI
from logs.logger import setup_logger

class XiaohongshuBot:
    def __init__(self, driver_path=None, username=None, password=None, api_base_url=None, api_access_token=None):
        self.actions = XiaohongshuActions(driver_path) if driver_path else None
        self.api = XiaohongshuAPI(api_base_url, api_access_token) if api_base_url and api_access_token else None
        self.username = username
        self.password = password
        self.logger = setup_logger('xiaohongshu_bot_logger', 'logs/xiaohongshu_bot.log')

    def run(self):
        self.logger.info("Running Xiaohongshu Bot")
        if self.actions:
            self.actions.login(self.username, self.password)
        self.logger.info("Xiaohongshu Bot is running")

    def post_content(self, content):
        if self.api:
            return self.api.post_content(content)
        elif self.actions:
            self.actions.post_content(content)

    def auto_reply(self, post_id_or_url, reply_content):
        if self.api:
            return self.api.auto_reply(post_id_or_url, reply_content)
        elif self.actions:
            self.actions.auto_reply(post_id_or_url, reply_content)

    def auto_private_message(self, user_id_or_url, message_content):
        if self.api:
            return self.api.auto_private_message(user_id_or_url, message_content)
        elif self.actions:
            self.actions.auto_private_message(user_id_or_url, message_content)

    def search_content(self, query):
        if self.api:
            return self.api.search_content(query)
        elif self.actions:
            self.actions.search_content(query)

    def follow_user(self, user_id_or_url):
        if self.api:
            return self.api.follow_user(user_id_or_url)
        elif self.actions:
            self.actions.follow_user(user_id_or_url)

    def like_post(self, post_id_or_url):
        if self.api:
            return self.api.like_post(post_id_or_url)
        elif self.actions:
            self.actions.like_post(post_id_or_url)

    def comment_post(self, post_id_or_url, comment_content):
        if self.api:
            return self.api.comment_post(post_id_or_url, comment_content)
        elif self.actions:
            self.actions.comment_post(post_id_or_url, comment_content)

    def close(self):
        if self.actions:
            self.actions.close()