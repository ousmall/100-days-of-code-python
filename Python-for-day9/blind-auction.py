import os
import auction_logo

print(auction_logo.logo)
print("Welcome to the teasure auction! Let's get started!")

auction_list = []

bidder_name = input("What is your name?\n").lower()
bidder_price = int(input("What is your bid?\n $"))

end_bidding = False

while not end_bidding:
    add_bidder = input("Are there any other bidder? Type 'Yes' to join the auction or 'No' to show the consequence.\n").lower()
    os.system("cls")
    if add_bidder == "yes":
        new_bid = {"bidder": bidder_name, "price": bidder_price} 
        auction_list.append(new_bid)
        
        bidder_name = input("What is your name?\n").lower()
        bidder_price = int(input("What is your bid?\n $"))
    
    elif add_bidder == "no":
        highest_bidder = ""
        highest_price = 0
        for bid in auction_list:
            if bid["price"] > highest_price:
                highest_price = bid["price"]
                highest_bidder = bid["bidder"]
        
        print(f"The final owner is {highest_bidder} with a bid of ${highest_price}") 
        end_bidding = True  
