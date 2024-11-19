party_members = []
party_health = [10, 10, 10, 10 ]
miles_remaining = 200
days_until_winter = 60
mons = 0
oxen = 0
rations = 0
emergency_supplies = 0

a = print("Banker from Boston")
B = print("Carpenter from Ohio")

print("Welcome to my Oregon Trail Game!")
answer = input("Which career do you want to be..... ")
if answer.lower() == "a":
    mons = 100
elif answer.upper() == 'B':
    mons = 80
else: 
    mons = 60

party_leader = input("What's your party leaders name?")
party_members.append(party_leader)

count = 0
while count is 0 > 3: 
    party = input("Enter a party member's name: ")
    party_members.append([party])

