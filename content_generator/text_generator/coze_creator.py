import asyncio
import logging
import time
import os
import json
from tqdm import tqdm
from playwright.async_api import Playwright, async_playwright
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random
import requests
from pprint import pprint
import shutil

class Coze():
    def __init__(self):
        self.ua = {
            "web": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 "
                   "Safari/537.36",
            "app": "com.ss.android.ugc.aweme/110101 (Linux; U; Android 5.1.1; zh_CN; MI 9; Build/NMF26X; "
                   "Cronet/TTNetVersion:b4d74d15 2020-04-23 QuicVersion:0144d358 2020-03-24)"
        }
        self.resultTextArr = []
        self.resultText = ''

class CozeChat(Coze):
    def __init__(self, 
                timeout: int, 
                cookie_file: str,
                space_id: str,
                coze_app_id: str):
        super(CozeChat, self).__init__()
        """
        初始化
        :param timeout: 你要等待多久，单位秒
        :param cookie_file: cookie文件路径
        """
        self.timeout = timeout * 1000
        self.cookie_file = cookie_file
        self.path = os.path.abspath('')
        self.space_id = space_id
        self.coze_app_id = coze_app_id
    
    def change_coze_app(self, space_id, coze_app_id):
        self.space_id = space_id
        self.coze_app_id = coze_app_id

    async def playwright_init(self, p: Playwright, headless=None):
        """
        初始化playwright
        """
        if headless is None:
            headless = False

        browser = await p.chromium.launch(headless=headless,
                                          chromium_sandbox=False,
                                          ignore_default_args=["--enable-automation"],
                                          channel="chrome", args=["--start-maximized"]
                                          )
        return browser
        
    async def run(self, p: Playwright) -> None:
        browser = await self.playwright_init(p)
        context = await browser.new_context(storage_state=self.cookie_file, user_agent=self.ua["web"],no_viewport=True)
        page = await context.new_page()
        await page.goto(f"https://www.coze.cn/space/{self.space_id}/bot/{self.coze_app_id}")
        time.sleep(5)
        print("正在判断账号是否登录")
        if "/space" not in page.url:
            print("账号未登录")
            logging.info("账号未登录")
            return
        print("账号已登录")
        try:
            await page.locator('.coz-bg-max.coz-stroke-primary > div > textarea').fill('给我讲一下各星座今日星运，开场白讲一下日期，然后直接讲星座,对话中不要出现"今日"')
            await page.locator('.coz-icon-button.coz-icon-button-default > [data-testid="bot-home-chart-send-button"]').click()
            # 等待页面加载完成
            tmp = True
            while tmp:
                try:
                    # 等待元素存在
                    await page.wait_for_selector('span:has-text("停止响应")', state='visible', timeout=1000)
                    time.sleep(1)
                except Exception as e:
                    # 元素不存在，退出循环
                    break
            # 获取HTML内容
            tmp_value = await page.locator('.chat-uikit-text-content > .flow-markdown-body').last.inner_text()
            self.resultText  = '\n'.join(list(filter(None, (tmp_value.split('\n')))))
            print('文字已生成')
            # self.resultTextArr  = list(filter(None, (tmp_value.split('\n'))))
            # input(123)
        except Exception as e:
            print("登录失败，cookie已失效，请登录后再试\n", e)
            logging.info("登录失败，cookie已失效，请登录后再试")
        finally:
            await page.close()
            await context.close()
            await browser.close()

    async def main(self):
        async with async_playwright() as playwright:
            await self.run(playwright)


app = CozeChat(60, '/Users/wingerliu/Downloads/github/autovideo/cookies/CozeCookie/user_CozeCookie.json', '7416035471685861416', '7416036210902827034')
asyncio.run(app.main())
print(app.resultText)