from .base import TextGeneratorBase

class ChatGPTTextGenerator(TextGeneratorBase):
    def generate(self, prompt):
        # 实现ChatGPT的文本生成逻辑
        return "Generated text by ChatGPT"