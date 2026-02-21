# 1- import the random module

import random
# 2- Creates subjects
subjects=[
    "Dev",
    "Deepika",
    "Koyel",
    "A Mumbai cat",
    "A Groups of Monkeys",
    "Prime Minster Modi",
    "Auto Richwas from Kolkata"
]

actions=[
    "launches",
    "cancles",
    "dance with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
]

places_or_things=[
    "at Red Fort",
    "in Kolkata Local Train",
    "a plote of samosa",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_things = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject} {action} (places_or_things)"
    print("\n" + headline)
    
    user_input = input("\n Do you want another headline ?(yes/no)").strip()
    if user_input == "no":
        break
    
    #print goodbye message
    print("\n Thanks for using the Fake News Headline Generator.Have a fun day")
    
    