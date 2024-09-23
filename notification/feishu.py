# language: notification/feishu.py
from .base import NotificationBase
import requests
from logs.logger import setup_logger

class FeishuNotification(NotificationBase):
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.logger = setup_logger('feishu_notification_logger', 'logs/feishu_notification.log')

    def send(self, message):
        self.logger.info(f"Sending Feishu notification: {message}")
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "msg_type": "text",
            "content": {
                "text": message
            }
        }
        response = requests.post(self.webhook_url, headers=headers, json=data)
        self.logger.info("Feishu notification sent")
        return response.json()