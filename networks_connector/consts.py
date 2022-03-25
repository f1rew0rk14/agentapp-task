from dotenv import load_dotenv

import os

load_dotenv()

CHANNELS = ["vk", "facebook"]
VK_TOKEN = os.environ.get("VK_TOKEN")
if not VK_TOKEN:
    raise ValueError("You must specify VK_TOKEN in your environment")

FACEBOOK_TOKEN = os.environ.get("FACEBOOK_TOKEN")
if not FACEBOOK_TOKEN:
    raise ValueError("You must specify FACEBOOK_TOKEN in your environment")
