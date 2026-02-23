import numpy as np

msg = "Roll the Dice!"

"""Return a random integer between 1 and 6 inclusive"""
def roll():
    return int(np.random.randint(1, 7))

if __name__ == "__main__":
    print(msg)
    print(roll())