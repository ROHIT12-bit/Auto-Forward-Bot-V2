from os import environ 

class Config:
    API_ID = environ.get("API_ID", "26047636")
    API_HASH = environ.get("API_HASH", "d8b1ed69ae1f937c5dd4d3cc8c8de440")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8582865115:AAGkGIAg9VVQLcuo02WGo9mK1NQ2u2Ol8f4") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8367080346').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
