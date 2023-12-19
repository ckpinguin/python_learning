import os
from art import logo

bids = {}


print(logo)

bidding = True

while bidding:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  os.system('clear')
  bids[name] = bid
  should_continue = input("Are there more bidders (yes/no)?:\n")
  if should_continue == "no":
    bidding = False

max_bid = max(bids.values())
for key, value in bids.items():
  if value == max_bid:
    print(f"The highest bid of {value} came from {key}!")