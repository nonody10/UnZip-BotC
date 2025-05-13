import os

class Config(object):

    API_ID = os.environ.get("API_ID")
    if not API_ID:
        raise ValueError("❌ API_ID is missing in environment variables.")
    API_ID = int(API_ID)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_HASH = os.environ.get("API_HASH", "")
    MAX_FILE_SIZE = 2194304000
    
    
