import time
import random
#from PIL import Image

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.tiredness = 50

    def feed(self):
        self.hunger -= 10
        self.happiness += 5

    def play(self):
        self.happiness += 10
        self.tiredness += 5

    def sleep(self):
        self.tiredness -= 10
        self.hunger += 5

    def check_status(self):
        if self.hunger <= 0 or self.happiness <= 0 or self.tiredness <= 0:
            print(f"{self.name} has passed away...")
            return False
        return True

    def save_to_file(self):
        with open(f"{self.name}_status.txt", "w") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Hunger: {self.hunger}\n")
            file.write(f"Happiness: {self.happiness}\n")
            file.write(f"Tiredness: {self.tiredness}\n")

def main():
    name = input("Enter your Tamagotchi's name: ")
    tamagotchi = Tamagotchi(name)

    while tamagotchi.check_status():
        action = input("\nChoose an action: [feed / play / sleep / save / exit] ")
        if action == "feed":
            tamagotchi.feed()
            print(f"{tamagotchi.name} has been fed!")
        elif action == "play":
            tamagotchi.play()
            print(f"{tamagotchi.name} is playing!")
        elif action == "sleep":
            tamagotchi.sleep()
            print(f"{tamagotchi.name} is sleeping!")
        elif action == "save":
            tamagotchi.save_to_file()
            print("Tamagotchi's status has been saved to file.")
        elif action == "exit":
            tamagotchi.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
