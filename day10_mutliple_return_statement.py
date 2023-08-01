def format_name(f_name, l_name):

    if f_name =="" or l_name == "":
        return "You didnt provide valid inputs"

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name\n"),(input("What is your last name\n"))))

# output = len("Bobby")
    