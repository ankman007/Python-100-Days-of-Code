from Modules import PyArt

print(PyArt.auction_logo)
bid_account = {}
choice = ''

while choice != 'no':
    name = input('\nWhat is your name? ')
    bid_price = float(input('What is your bid? $'))
    choice = input('Are there any other bidders? [yes or no]\n')
    bid_account[name] = bid_price

highest_bid = 0
highest_bidder = ''

for name, bid_price in bid_account.items():
    if bid_price > highest_bid:
        highest_bid = bid_price
        highest_bidder = name

print(f'\n\nThe winner of this blind auction is {highest_bidder.capitalize()} with a bid of ${highest_bid}.')
