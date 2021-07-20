import random

classes = ['Wizard', 'Warrior']

while True:
    try:
        option = int(input('Choose your figther:\n[1] - Wizard\n[2] - Warrior     - Select: '))
        if option == 1 or option == 2:
            break
        else:
            print("\nInvalid option, try again\n")
            pass
    except:
        print("\nInvalid option, try again\n")
        pass

if option == 1:
    stamana = 10

if option == 2:
    stamana = 15

hp = 10

print("\nCongratulations! You've chosen to be a great",classes[option - 1],"and shall defeat yourself in this marvelous adventure.\nYou're starting with:", str(stamana), "attack points and", str(hp),"health points\n")

actions = ["Attack", "Defeat", "Rest", "Heal"]

level = 1

while True:
    mhp = 20 + (level - 1)*10
    mat = 15 + (level -1)*3

    stamana = stamana + (level - 1)*5
    hp = hp + (level - 1)*5