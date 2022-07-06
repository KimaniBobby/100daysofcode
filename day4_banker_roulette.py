import random 

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


length = len(names)

test1 = random.randint(0,length -1 )

person_who_will_pay =names[test1]

print(f"{names[test1]} is going to buy the meal today!")

#print (test1)

# print(len(names))

