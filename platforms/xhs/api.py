# language: platforms/xiaohongshu/api.py
import requests
from logs.logger import setup_logger

class XiaohongshuAPI:
    def __init__(self, base_url, access_token):
        self.base_url = base_url
        self.access_token = access_token
        self.logger = setup_logger('xiaohongshu_api_logger', 'logs/xiaohongshu_api.log')

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def post_content(self, content):
        self.logger.info("Posting content to Xiaohongshu via API")
        url = f"{self.base_url}/posts"
        data = {
            "content": content
        }
        response = requests.post(url, headers=self._get_headers(), json=data)
        self.logger.info(f"Response: {response.status_code} - {response.text}")
        return response.json()

    def auto_reply(self, post_id, reply_content):
        self.logger.info(f"Auto replying to post {post_id} via API")
        url = f"{self.base_url}/posts/{post_id}/replies"
        data = {
            "content": reply_content
        }
        response = requests.post(url, headers=self._get_headers(), json=data)
        self.logger.info(f"Response: {response.status_code} - {response.text}")
        return response.json()

    def auto_private_message(self, user_id, message_content):
        self.logger.info(f"Sending private message to user {user_id} via API")
        url = f"{self.base_url}/users/{user_id}/messages"
        data = {
            "content": message_content
        }
        response = requests.post(url, headers=self._get_headers(), json=data)
        self.logger.info(f"Response: {response.status_code} - {response.text}")
        return response.json()

    def search_content(self, query):
        self.logger.info(f"Searching content with query: {query} via API")
        url = f"{self.base_url}/search"
        params = {
            "q": query
        }
        response = requests.get(url, headers=self._get_headers(), params=params)
        self.logger.info(f"Response: {response.status_code} - {response.text}")
        return response.json()

    def follow_user(self, user_id):
        self.logger.info(f"Following user {user_id} via API")
        url = f"{self.base_url}/users/{user_id}/follow"
        response = requests.post(url, headers=self._get_headers())
        self.logger.info(f"Response: {response.status_code} - {response.text}")
        return response.json()

    def like_post(self, post_id):
        self.logger.info(f"Liking post {post_id} via API")
        url = f"{self.base_url}/posts/{post_id}/like"
        response = requests.post(url, headers=self._get_headers())
        self.logger.info(f"Response: {response.status_code} - {response.text}")
        return response.json()

    def comment_post(self, post_id, comment_content):
        self.logger.info(f"Commenting on post {post_id} via API")
        url = f"{self.base_url}/posts/{post_id}/comments"
        data = {
            "content": comment_content
        }
        response = requests.post(url, headers=self._get_headers(), json=data)
        self.logger.info(f"Response: {response.status_code} - {response.text}")
        return response.json()