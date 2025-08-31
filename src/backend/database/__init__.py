import json

from ..config import *

def get_channel():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f).get("channel")
    
def set_channel(channel):
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
    config["channel"] = channel
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)