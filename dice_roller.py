import random as random

def randRoll(roll):
    return random.randrange(1, roll + 1, 1)

def main():
    while(1):
        inVal = input('Enter command:')
        if (inVal == "stop"):
            break
        elif(inVal == "1"):
            print("1")
        else:
            print(randRoll(int(inVal)))
    return

if(__name__ == "__main__"):
    main()