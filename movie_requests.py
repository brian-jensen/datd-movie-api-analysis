import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")

print(api_key)
