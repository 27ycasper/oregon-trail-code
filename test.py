party_members = []
party_health = [10, 10, 10, 10 ]
miles_remaining = 200
days_until_winter = 60
mons = 0
oxen = 0
rations = 0
emergency_supplies = 0
oxen_price = 20
rations_price = 2
emergency_supplies_price = 5



print("Welcome to my Oregon Trail Game!")
answer = ""
while answer.lower() not in ["A", "B", "C"]:
    answer = input("Which career do you want to be? Banker (A), Carpenter (B), or Farmer (C): ")
if answer.lower() == "Banker from Boston":
    mons = 100
elif answer.lower() == "Carpenter from Ohio":
    mons = 80
else: 
    mons = 60

party_leader = input("What's your party leaders name?: ")
party_members.append(party_leader)

count = 0
while count == 0 > 3: 
    party = input("Enter a party member's name: ")
    party_members.append([party])

while mons >= 2:
    game_shop = input("What would you like to buy? A. Oxen B. Rations C. Emergency Supplies: ")



while answer.lower() not in ['a', 'b', 'c']:
    answer = input("What would you like to buy?: ")

if game_shop.lower() == 'a':
    amount = input("How many oxen would you like to buy?: ")
    if amount.isdigit():
        amount = int(amount)
        total = amount * oxen_price
        if mons >= total:
            oxen += amount
            mons -= total
        else:
            print("Not enough money.")
    else: 
        print("Invalid aount entered. Try again.")

