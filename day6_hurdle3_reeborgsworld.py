def turn_right():
    turn_left()
    turn_left()
    turn_left()

def wall_ahead():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front:
        wall_ahead()