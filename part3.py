import random

game_name = "Escaping"  # TODO: name your game project

name = "Tester" #ask for the character's name

player = {
    "name": name,
    "health": 100,
    "coin": 0,
    "x": 0,
    "y": 0
}

events = ["find a coin", "meet a monster", "do nothing"]

map_size = 9

def check_event():
    global player, events
    if events == "find a coin":
        player["coin"] += 1
    elif events == "meet a monster":
        player["health"] -= 10

def draw_ui(x, y):
    print("=========================")
    for i in range(map_size):
        for j in range(map_size):
            if i == x and j == y:
                print("C", end=" ")
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end=" ")
            else:
                print(".", end=" ")
        print()
    print("=========================")
    print(f"Health: {player['health']}")
    print("-------------------------")
    print(f"Coin: {player['coin']}")
    print("=========================")

def move(direction):
    global player, map_size
    if direction == "w" and player["x"] > 0:
        player["x"] -= 1
    elif direction == "s" and player["x"] < map_size - 1:
        player["x"] += 1
    elif direction == "a" and player["y"] > 0:
        player["y"] -= 1
    elif direction == "d" and player["y"] < map_size - 1:
        player["y"] += 1
    else:
        print("You cannot move that way!")

def main():
    print(f"Welcome to {game_name}!")
    print("=========================")
    print(f"Great {player['name']}! Let's begin the adventure!")

    draw_ui(player["x"], player["y"])
    direction = input("Your next move (w/a/s/d/q): ")

    while direction != "q":
        move(direction)

        if player["x"] == map_size - 1 and player["y"] == map_size - 1:
            print("Congratulations! You reach the gate for next level.")
            break

        check_event()
        draw_ui(player["x"], player["y"])
        direction = input("Your next move (w/a/s/d/q): ")

if __name__ == "__main__":
    main()
    