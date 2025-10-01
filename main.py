game_name = "Escaping"  # TODO: name your game project
greeting = f"Welcome to {game_name}!"
print(greeting)
print(f'{"=" * len(greeting)}') # TODO: add/remove "=" to line up with "!"

name = input("Enter your character's name: ") #ask for the character's name

player = {
    'name': name,
    'health': 100,
    'coin': 0
}

import random
events = ["find a coin", "meet a monster", "do nothing"]
event = random.choice(events)
print(f"While exploring, you {event}!")

if event == "find a coin":
    player['coin'] += 1
    print(f"{player['name']} found a coin, {player['name']} now has {player['coin']} coins.")
elif event == "meet a monster":
    player['health'] -= 10
    print(f"{player['name']} got hurt during the combat with monster, health is now {player['health']}.")
else:
    pass
print(player)
