print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Please pay $5")
  elif age <= 18:
    bill = 7
    print("Please pay $7")
  elif age>=18:
    bill = 12
    print("Please pay $12")
    

    
  wants_photos = input("Do you want photos Y or N ")

  if wants_photos == "Y":
    bill +=3
  
  print(f"Your final bill is ${bill}")
else:
  print("You can't ride the rollercoaster")

