social_media_bot/
├── README.md
├── requirements.txt
├── config/
│   ├── config.yaml
├── core/
│   ├── __init__.py
│   ├── bot.py
│   ├── scheduler.py
├── content_generation/
│   ├── __init__.py
│   ├── text/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── chatgpt.py
│   │   ├── tongyi.py
│   │   ├── coze.py
│   │   ├── kim.py
│   ├── image/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dalle.py
│   │   ├── sd.py
│   ├── video/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── deepfake.py
│   ├── audio/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── google_tts.py
│   │   ├── amazon_polly.py
├── platforms/
│   ├── __init__.py
│   ├── xiaohongshu/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── bot.py
│   ├── feishu/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── bot.py
│   ├── common/
│       ├── __init__.py
│       ├── utils.py
├── notification/
│   ├── __init__.py
│   ├── base.py
│   ├── feishu.py
│   ├── email.py
│   ├── wechat.py
├── tests/
│   ├── __init__.py
│   ├── test_bot.py
│   ├── test_scheduler.py
│   ├── test_xiaohongshu.py
│   ├── test_feishu.py
│   ├── test_text_generation.py
│   ├── test_image_generation.py
│   ├── test_video_generation.py
│   ├── test_audio_generation.py
│   ├── test_notification.py
└── main.py
