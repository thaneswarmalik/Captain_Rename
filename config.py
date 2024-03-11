# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24106665")

API_HASH = os.environ.get("API_HASH", "efd96d849629b8426369b718913263b9")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6254275801:AAFiuCrZp4rq9D5dqhFa8iuo8Xw_-bPA9Mg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Cineverse_Movies_7") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://thaneswar9:thaneswar9@cluster0.1w4lqre.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6961701346').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
