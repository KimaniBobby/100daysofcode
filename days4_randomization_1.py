import random

random_integer = random.randint(1,10)

random_float = round(random.random(),2) * 5 #generate random floating point number (number between 0.0 to 1.0) not including 1

print(random_integer)

print(random_float)


love_score = random.randint(1,100)

print(f"Your love score is {love_score}")