import os

class Config(object):

    API_ID = os.environ.get("API_ID", "20826111")
    if not API_ID:
        raise ValueError("❌ API_ID is missing in environment variables.")
    API_ID = int(API_ID)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7785298933:AAH8puU-CEjCtr9eO5F6KBO2kiEhKyFg_UU")
    API_HASH = os.environ.get("API_HASH", "7b6813d0d82891dd367b420b46133691")
    MAX_FILE_SIZE = 2194304000
    
    
