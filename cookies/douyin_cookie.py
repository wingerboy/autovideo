# -*- coding: utf-8 -*-
"""
本地打开浏览器
"""

import asyncio
import os
from playwright.async_api import Playwright, async_playwright


class DouyinCookie():
    def __init__(self, phone, timeout: int, path=''):
        """
        初始化
        :param phone: 手机号
        :param timeout: 你要等待多久，单位秒
        """
        self.timeout = timeout * 1000
        self.phone = phone
        self.path = os.path.join(os.path.dirname(os.path.realpath('__file__')), self.__class__.__name__)
        self.desc = f"user{phone}_{self.__class__.__name__}.json"

        if not os.path.exists(self.path):
            os.makedirs(self.path)

    async def __cookie(self, playwright: Playwright) -> None:
        browser = await playwright.chromium.launch(channel="chrome", headless=False)

        context = await browser.new_context()

        page = await context.new_page()

        await page.add_init_script("Object.defineProperties(navigator, {webdriver:{get:()=>false}});")

        await page.goto("https://creator.douyin.com/")

        await page.locator(".agreement-FCwv7r > img:nth-child(1)").click()

        await page.locator('#number').fill(self.phone)

        try:
            await page.wait_for_url("https://creator.douyin.com/creator-micro/home", timeout=self.timeout)
            cookies = await context.cookies()
            cookie_txt = ''
            for i in cookies:
                cookie_txt += i.get('name') + '=' + i.get('value') + '; '
            try:
                cookie_txt.index("sessionid")
                print(self.phone + " ——> 登录成功")
                # with open(os.path.join(self.path, "cookie", self.phone + ".txt"), mode="w") as f:
                #     f.write(cookie_txt)
                await context.storage_state(path=os.path.join(self.path, self.desc))
            except ValueError:
                print(self.phone + " ——> 登录失败，本次操作不保存cookie")
        except Exception as e:
            print(self.phone + " ——> 登录失败，本次操作不保存cookie", e)
        finally:
            await page.close()
            await context.close()
            await browser.close()

    async def main(self):
        async with async_playwright() as playwright:
            await self.__cookie(playwright)


def main():
    while True:
        phone = input('请输入手机号码\n输入"exit"将退出服务\n')
        if phone == "exit":
            break
        elif phone.isnumeric() and len(phone) == 11:
            app = DouyinCookie(phone, 60)
            asyncio.run(app.main())
        else:
            print('请输入正确的手机号码\n')


main()
