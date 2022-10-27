tomorrow = {
    "Bug":"an error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop":"The action of doing something over and over again"

}

print(tomorrow["Loop"])

tomorrow["Today"]= "Focus on today and hope for the best tomorrow"

print(tomorrow["Today"])

print(tomorrow)

#create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
#tomorrow = {}

#print(tomorrow)

#Editing contents in a dictionary 

#tomorrow["Bug"] = "Me and Mine"

#print(tomorrow["Bug"])

#Loop through a dictionary

for key in tomorrow:
    print(key)
    print (tomorrow [key])

    