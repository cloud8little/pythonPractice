import json

class Config:
    def __init__(self,config_file="config.json"):
        with open(config_file, "r", encoding='utf-8') as user_file:
            self.config = json.load(user_file)

configIns = Config()
print(configIns.config.get("ControllerAddress"))            