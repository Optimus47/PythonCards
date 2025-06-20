from dotenv import load_dotenv
import os

load_dotenv()

api_key: str = os.getenv("API_KEY")
print(api_key)
if os.getenv("DEBUG"):
    print("Debug mode is ON")

print(__annotations__)
