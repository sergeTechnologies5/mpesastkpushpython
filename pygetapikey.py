import requests
from requests.auth import HTTPBasicAuth

consumer_key = "jJMVK098pTNas1GdmiEUGwVARaI5zOs3"
consumer_secret = "LMmzbd6qzELQfR5f"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print (r.text)
