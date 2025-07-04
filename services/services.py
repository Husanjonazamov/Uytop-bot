# services.py fayli
import requests
from utils.env import BASE_URL



def listingisTop(listing_id):
    print(listing_id)
    url = f"http://127.0.0.1:8042/listing/top/{listing_id}/"
    response = requests.post(url)
    
    print(response.status_code)
    
    try:
        data = response.json()
        return data
    except Exception as e:
        return e