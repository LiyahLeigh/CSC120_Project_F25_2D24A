import random

class Player:
    def __init__(self, name = "Tester"):
        self.name = name
        self.health = 100
        self.coin = 0
        self.x = 0
        self.y = 0

    def move(self, direction, map_size):
        """
        Move the player on the map if possible.
        
        This is the old move() logic from part 3, but using self.x / self.y
        instead of player["x"], player["y"].
        """
        direction = direction.lower().strip()

        if direction == "w" and self.x > 0:
            self.x -= 1
        elif direction == "s" and self.x < map_size - 1:
            self.x += 1
        elif direction == "a" and self.y > 0:
            self.y -= 1
        elif direction == "d" and self.y < map_size - 1:
            self.y += 1
        else:
            print("You cannot move that way!")

class GameMap:
    def __init__(self, size = 9):
        self.size = size

    def draw(self, player):
        """
        Draw the map and HUD. Equivalent to draw_ui(x, y) from part 3, 
        but now we read x and y from the player object.
        """
        print("=========================")
        for i in range(self.size):
            for j in range(self.size):
                if i == player.x and j == player.y:
                    print("C", end=" ")
                elif i == self.size - 1 and j == self.size - 1:
                    print("M", end=" ")
                else:
                    print(".", end=" ")
            print()
        print("=========================")
        print(f"Health: {player.health}")
        print("=========================")
        print(f"Coin: {player.coin}")
        print("=========================")

        print("Your move (w/a/s/d/q): ", end=" ")

class Game:
    def __init__(self, name = "Tester", map_size = 9):
        self.game_name = "Escaping"
        self.name ="Tester"
        self.events = ["find a coin", "meet a moster", "do nothing"]

        self.map_size = map_size

        self.player = Player(name)
        self.map = GameMap(map_size)

    def check_event(self):
        """
        Same logic as check_event() from part 3, but using self.player.
        """
        event =random.choice(self.events)

        if event == "find a coin":
            self.player.coin += 1
        elif event == "meet a monster":
            self.player.health -= 10

    def play(self):
        """
        This is your old main() function, converted into a method.
        Uses self.player and self.map instead of globals.
        Includes simple exception handling on input.
        """
        print(f"Welcome to {self.game_name}!")
        print("=========================")
        print(f"Great {self.player.name}! Let's begin the adventure!")

        while True:
            self.map.draw(self.player)
            try:
                direction = input()
            except EOFError:
                print("\nInput error. Exiting game.")
                break

            if direction == "q":
                print("Thanks for playing!")
                break

            self.player.move(direction, self.map.size)

            if (
                self.player.x == self.map.size -1
                and self.player.y == self.map.size - 1
            ):
                print("Congratulations! You reach the gate for next level.")
                break

            self.check_event()

if __name__ == "__main__":
    Game().play()
