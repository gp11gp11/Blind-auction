from replit import clear#used to call clear() to clear the output in the console
from art import logo

print(logo)

aution_list = {}
end = False
while not end:
  name = input("what's your name?")
  bid  = input("What's your bid")
  aution_list[name] = bid
  #winner = ""
  other_bidder = input("Are there other bidders?Type 'yes' or 'no'")
  if other_bidder == "no":
    end = True
  elif other_bidder == "yes":
    clear()


winner = ""
winner_bid = 0
for name in aution_list:
  bid = int(aution_list[name])
  if bid > winner_bid:
    winner_bid = bid
    winner = name
print(f"{winner} is the wins the bid,the bid amount is {winner_bid}")
'''
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 
'''
  
  