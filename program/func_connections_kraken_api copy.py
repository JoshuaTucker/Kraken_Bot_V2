import time
import requests
import pprint
from func_authentication import get_kraken_signature
from constants import (
    API_KEY, SEC_KEY
)



# Read Kraken API key and secret stored in environment variables
api_url = "https://api.kraken.com"
api_key = API_KEY
api_sec = SEC_KEY

# Attaches auth headers and returns results of a POST request
def kraken_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['API-Key'] = api_key
    # get_kraken_signature() as defined in the 'Authentication' section
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)             
    req = requests.post((api_url + uri_path), headers=headers, data=data)
    return req

# Construct the request and print the result
bal = kraken_request('/0/private/Balance', {
    "nonce": str(int(1000*time.time()))
}, api_key, api_sec)

# Construct the request and print the result
trade_hist = kraken_request('/0/private/TradesHistory', {
    "nonce": str(int(1000*time.time()))
}, api_key, api_sec)

print(bal.json())       
print("\n", "////////////////////", "\n") 
print(trade_hist.json())
