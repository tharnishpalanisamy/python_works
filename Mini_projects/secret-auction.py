from art import logo
print(logo)
def bid():
    to_continue = False
    bidders = {}
    while not to_continue:
        name = input("Enter your name :")
        bid = int(input("Enter you bid : $"))
        bidders[name] = bid
        direction = input("Are there any other bidders? Type 'yes or 'no'.").lower()
        if direction == "y":
            print("\n"*20)
            to_continue = False
        else :
            to_continue = True
    print(bidders)
    highest = 0
    for bid in bidders:
        value = bidders[bid]
        if highest < value:
            name = bid
            highest = value

    print(f"the highest bid was {highest} by {name}")

bid()

