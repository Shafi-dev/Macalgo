from kiteconnect import KiteConnect, exceptions
from dotenv import load_dotenv
import os


def get_kite():
    load_dotenv()
    kite = KiteConnect(api_key=os.getenv("KITE_API_KEY"))
    
    token_file = os.path.join(os.path.dirname(__file__), ".access_token")
    
    if not os.path.exists(token_file):
        print("No token found! Run login.py file first")
        exit(1)
        
    with open(token_file, "r") as f:
        access_token = f.read().strip()
        
    kite.set_access_token(access_token)
    
    try:
        kite.profile()
    except exceptions.TokenException:
        print("Token expired! Run login.py file first")
        exit(1)
        
    return kite
