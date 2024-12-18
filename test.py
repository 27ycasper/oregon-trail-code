import random
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
party_dead = False
dead = 'rip'
rand_num = 0



print("Welcome to my Oregon Trail Game!")
answer = ""
while answer.lower() not in ['a', 'b', 'c']:
    answer = input("Which career do you want to be? Banker (A), Carpenter (B), or Farmer (C): ")
if answer.lower() == 'a':
    mons = 100
elif answer.lower() == 'b':
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
    game_shop = input("What would you like to buy? Oxen (A), Rations (B), Emergency Supplies (C), Done(D): ")


    while game_shop.lower() not in ['a', 'b', 'c', 'd']:
        game_shop = input("What would you like to buy?: ")

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
            print("Invalid amount entered. Try again.")
    if game_shop.lower() == 'd':
        break

    if game_shop.lower() == 'b':
        amount = input("How many Rations would you like to buy?: ")
        if amount.isdigit():
            amount = int(amount)
            total = amount * rations_price
            if mons >= total:
                rations += amount
                mons -= total
            else:
                print("Not enough money.")
        else: 
            print("Invalid amount entered. Try again.")
    if game_shop.lower() == 'd':
        break

    if game_shop.lower() == 'c':
        amount = input("How many Emergency supplies would you like to buy?: ")
        if amount.isdigit():
            amount = int(amount)
            total = amount * emergency_supplies_price
            if mons >= total:
                emergency_supplies += amount
                mons -= total
            else:
                print("Not enough money.")
        else: 
            print("Invalid amount entered. Try again.")
    if game_shop.lower() == 'd':
        break

while miles_remaining > 0 and not party_dead:
    print("Here are your options: A, B, C, D, E")
    health = ""
    
    while health.lower() not in ['a','b','c','d','e']:
        health = input("Response:")
    
if health.upper() == 'A':
    if rations > 0:
        rations -= 1
    if days_until_winter <= 0:
        if party_health[0] != dead:
            party_health[0] += 1.5
        if party_health[1] != dead:
            party_health[1] += 1.5
        if party_health[0] != dead:
            party_health[2] += 1.5
        if party_health[0] != dead:
            party_health[3] += 1.5
    else:
        party_health[0] += 3
        party_health[1] += 3
        party_health[2] += 3
        party_health[3] += 3
else:
    print("You are not able to, sorry!")
if answer.upper() == 'B':
    if oxen > 0:
        days = random.randint(15,30)
        party_health[0] -= 3
        party_health[1] -= 3
        party_health[2] -= 3
        party_health[3] -= 3
        random_percent = random.randint(0,100)
if random_percent <= 5:
    oxen -= 1
else:
        days = random.randint(30, 80)
party_health[0] -= 6
party_health[1] -= 6
party_health[2] -= 6
party_health[3] -= 6

miles = random.randint(10,40)
miles_remaining -= miles
days_until_winter -= days

if answer.upper == 'C':
    if oxen > 0:
        days = random.randint(5,15)
    party_health[0] -= 8
    party_health[1] -= 8
    party_health[2] -= 8
    party_health[3] -= 8

    miles = random.randint(30,60)
    miles_remaining -= miles
    days_until_winter -= days

if answer.upper() == 'D':
    print("Health of party: ")
    print(party_health)

print("Rations remaining: " + str(rations))

answer = input("Are you sure you want to quit?: ")
if "y" in answer.lower():
    print("You have chosen to quit.")

rand_num == random.randint(1,20)
if rand_num == 1:

    if emergency_supplies > 0: 
        emergency_supplies -= 1
    else: 
        party_health[0] -= 5
        party_health[1] -= 5
        party_health[2] -= 5  
        party_health[3] -= 5

elif rand_num == 20:
    party_health[0] += 5
    party_health[1] += 5
    party_health[2] += 5 
    party_health[3] += 5
else:
    if party_health[0] != dead and party_health[0] <= 0:
        party_health[0] = dead
    if party_health[1] != dead and party_health[1] <= 0:
        party_health[1] = dead

if party_health.count(dead) == 4:
    party_dead = True
else: 
    if not party_dead:
        print("Surviving members: ")
if party_health[0] != dead:
    print("/t" + party_members[0])
if party_health[1] != dead:
    print("/t" + party_members[1])