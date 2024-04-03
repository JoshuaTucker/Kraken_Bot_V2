import ccxt
import dontshare_config

# import #your own functions from a file
from datetime import date, datetime, timezone, tzinfo
from pprint import pprint

kraken = ccxt.kraken({
    'enableRateLimit': True,
    'apiKey': dontshare_config.xP_KEY,
    'secret': dontshare_config.xP_SEC,
})

#def get_bid_ask():
#    sol_order_book = kraken.fetch_order_book('SOL/USD')
#    #print(sol_order_book)
#    sol_bid = sol_order_book['bids'][0][0]
#    sol_ask = sol_order_book['asks'][0][0]
#    print(f'the best bid: {sol_bid} the best ask {sol_ask}')
#
#    return sol_bid, sol_ask

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

pprint(kraken.fetch_balance())