# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total = 0

for h in student_heights:
    total +=  h
print(total)

number_of_items = 0

for s2 in student_heights:
    number_of_items +=1
print(number_of_items)

average = total/number_of_items

print(round (average))
