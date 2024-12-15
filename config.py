from os import environ

API_ID = int(environ.get("API_ID", "18421790"))
API_HASH = environ.get("API_HASH", "e66653d6147227f2127e5a4724151712")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "1002253867562"))
ADMINS = int(environ.get("ADMINS", "6474680825"))
DB_URI = environ.get("DB_URI", "mongodb+srv://yunokhann:Po0umBUdyETzpABD@cluster0.y3mzf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "PlyAeRequestbot")
