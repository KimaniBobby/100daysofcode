import random

#String
string = "I love myself.","I am my best source of motivation."
array = []
for c in string:
  array += [c]
 
print(array[random.randint(0, len(array)-1)])

# Faster and more efficient
random.choice(string)