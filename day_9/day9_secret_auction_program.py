from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount >highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bidding_finished:

    bid_name = input("Please enter your name\n")
    bid_price = int(input("Please enter your bid price\n$"))

    bids[bid_name] = bid_price
    choice = input("Are there other users who want to bid?Yes or No\n").lower()

    if choice == "no":
        bidding_finished =True
        highest_bidder(bids)
    elif choice == "yes":
        clearConsole = lambda: print('\n' * 150)
        clearConsole()


    
