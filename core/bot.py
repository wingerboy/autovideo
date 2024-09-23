# language: core/bot.py
from content_generation.text.chatgpt import ChatGPTTextGenerator
from content_generation.image.dalle import DalleImageGenerator
from notification.feishu import FeishuNotification
from notification.email import EmailNotification
from logs.logger import setup_logger

class SocialMediaBot:
    def __init__(self):
        self.platform_bots = []
        self.text_generator = ChatGPTTextGenerator()
        self.image_generator = DalleImageGenerator()
        self.notifications = []
        self.logger = setup_logger('bot_logger', 'logs/bot.log')

    def add_platform_bot(self, platform_bot):
        self.platform_bots.append(platform_bot)
        self.logger.info(f"Added platform bot: {platform_bot.__class__.__name__}")

    def add_notification(self, notification):
        self.notifications.append(notification)
        self.logger.info(f"Added notification: {notification.__class__.__name__}")

    def run(self):
        self.logger.info("Starting SocialMediaBot")
        for bot in self.platform_bots:
            bot.run()
        self.logger.info("SocialMediaBot is running")

    def generate_content(self, prompt):
        self.logger.info(f"Generating content for prompt: {prompt}")
        text = self.text_generator.generate(prompt)
        image = self.image_generator.generate(prompt)
        self.logger.info("Content generated")
        return text, image

    def notify(self, message):
        self.logger.info(f"Sending notification: {message}")
        for notification in self.notifications:
            notification.send(message)
        self.logger.info("Notifications sent")