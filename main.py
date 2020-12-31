from replit import clear
from art import logo
print(logo)


def add_bid(new_name,new_bid):
  biddings[new_name] = new_bid


biddings = {}
is_other_bidder ="yes"
while is_other_bidder == "yes":
  clear()
  print("Welcome!!!")
  name = input("What is your name?")
  bid = int(input("What is your bidding price?"))
  add_bid(new_name = name, new_bid = bid)
  is_other_bidder = input("If there is other bidder then enter 'yes', if not then enter 'no'. ")

  if is_other_bidder == "no":
    heighst_bid = 0
    for bidder in biddings:
      if biddings[bidder]>heighst_bid:
        heighst_bid = biddings[bidder]
        winner = bidder
    clear()
    print(f"Bidding list :{biddings} ")
    print(f"Heighst bid is:{heighst_bid}")
    print(f"Highst bidder is {winner}")







