import telegram 
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv ("API_TOKEN")
print(API_TOKEN)