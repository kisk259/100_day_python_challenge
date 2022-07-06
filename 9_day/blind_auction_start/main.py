from replit import clear
from art import logo


# HINT: You can call clear() to clear the output in the console.

def bid_func(bidders_list):
    win_name = ""
    win_bid = 0
    name = ""
    bid = 0
    for list_element in bidders_list:
        for key in list_element:
            if key == "name":
                name = list_element[key]
            else:
                bid = int(list_element[key])
            if bid > win_bid:
                win_name = name
                win_bid = bid

    print(f"The winner is {win_name} with a bid of {win_bid}")


print(logo)
print("Welcome to the secret auction program.")
bidders = []
new_bidder = {}
run = True
while run:
    # Can be made easier like this: {"James": 321} instead of {"name": James, "bid": 321}
    new_bidder["name"] = name_in = input("What is your name?: ")
    new_bidder["bid"] = bid_in = input("What's your bid?: ")
    bidders.append(new_bidder)

    other_bids = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bids == "no":
        clear()
        bid_func(bidders)
        run = False
    elif other_bids == "yes":
        clear()
