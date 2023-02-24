import random

tup = (0,1)

choice = random.choice(tup)
print(choice)
if choice == 1:
    print("Present")
else :
    print("Absent")