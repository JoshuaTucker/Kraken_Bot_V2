import ccxt
from decouple import config
from datetime import date, datetime, timezone, tzinfo
from pprint import pprint
from constants import (
    API_KEY,
    SEC_KEY
)




kraken = ccxt.kraken({
    'enableRateLimit': True,
    'apiKey': API_KEY,
    'secret': SEC_KEY,
})
pprint(kraken.requiredCredentials)
def get_bid_ask():
    sol_order_book = kraken.fetch_order_book('SOL/USD')
    #print(sol_order_book)
    sol_bid = sol_order_book['bids'][0][0]
    sol_ask = sol_order_book['asks'][0][0]
    print(f'the best bid: {sol_bid} the best ask {sol_ask}')

    return sol_bid, sol_ask

#makepretty = get_bid_ask()
#pprint(makepretty)
#symbol = 'SOL/USD'
#amount = 0.5
#price = get_bid_ask()[0]
#price = price - 1
#params  = {}
#kraken.create_limit_buy_order(symbol, amount, price, params)
#print('we just used a bot cock sucker')




# play around with fetch_
#pretty = kraken.fetch_currencies()
#pprint(pretty)

# x = kraken.fetch_balance()
# 
#x = kraken.fetch_accounts()
#print(x)
credits = { "USD" : 'USD'}
#bal = kraken.fetch_balance()
#pprint(bal)
print("//////////////////////////////","\n")
print(kraken.fetchBalance())
pprint(get_bid_ask())
print("works")