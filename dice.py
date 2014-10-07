import random
from random import randint

total_heads = 0
total_tails = 0

#create a function that half the time returns "heads" and half the time returns "tails"
def flip_coin():
    x = randint(0,1)
    if x==0:
        return "heads"
    return "tails"

#flip 1000 times
for n in range(0,1000):
    flip = flip_coin()
    if flip == "heads":
        total_heads = total_heads + 1
    else:
        total_tails = total_tails + 1

print "Heads flipped: ", total_heads
print "Tails flipped: ", total_tails
