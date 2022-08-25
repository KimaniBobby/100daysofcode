import blessings
import time
import random


t = blessings.Terminal()

name = input(t.yellow("What is your name? "))

aff_prefix = "I, " + name + ", "

fb_prefix = "You "

question = t.red("What is your quest? ") + "\n" + t.bright_black("(I, <name>, <state your quest>.)") + "\n" + t.cyan("> ")

affirm_times = random.randrange(12, 17)

for i in range(affirm_times):
    # print(t.yellow(str(i + 1)))
    affirmation = input(question)

    feedback = affirmation.replace(aff_prefix, fb_prefix)

    if (i < affirm_times - 1 ):
        loops =  i + random.randrange(10)
        for j in range(loops):
            colornum = random.randrange(1,15)
            print(t.color(colornum)(feedback))
            time.sleep(random.random())
        print("\n")

    if ( i == affirm_times - 1 ):
        feedback = feedback.upper()
        for j in range(i + affirm_times):
            print(t.color(j+1)(feedback))
            time.sleep(random.random())
        print(t.bold("You have proved yourself worthy."))
        quit()