# language: main.py
from core.bot import SocialMediaBot
from platforms.xiaohongshu.bot import XiaohongshuBot
from platforms.feishu.bot import FeishuBot
from notification.feishu import FeishuNotification
from notification.email import EmailNotification
from logs.logger import setup_logger

def main():
    main_logger = setup_logger('main_logger', 'logs/main.log')
    main_logger.info("Starting main function")

    # 初始化各平台的机器人
    xiaohongshu_bot = XiaohongshuBot()
    feishu_bot = FeishuBot()
    
    # 初始化通知模块
    feishu_notification = FeishuNotification(webhook_url="your_feishu_webhook_url")
    email_notification = EmailNotification(smtp_server="smtp.example.com", smtp_port=465, username="your_email@example.com", password="your_password")
    
    # 初始化主机器人
    bot = SocialMediaBot()
    bot.add_platform_bot(xiaohongshu_bot)
    bot.add_platform_bot(feishu_bot)
    bot.add_notification(feishu_notification)
    bot.add_notification(email_notification)
    
    # 启动机器人
    bot.run()
    
    # 发送通知
    bot.notify("机器人已启动")

    main_logger.info("Main function finished")

if __name__ == "__main__":
    main()