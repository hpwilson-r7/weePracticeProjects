#!/usr/bin/env python3
# This is a shebang line this lets you run it like ./collatzSequence.py instead of python3 collatzSequence.py
# It also doesn't work atm

# +++ Buggies +++
# Have to select medium twice, but only counts the first selection

import random
import time
import sys
import json
from pick import pick


# Prints Title
def title():
    title = "Movie Chooser"
    sparkle = "=+"
    print(sparkle * int((len(title) / 2) + 1) + "=")
    print((" " * int(len(title) / 8)) + title)
    print(sparkle * int((len(title) / 2) + 1) + "=")


# Sets feeling tag
def feelingChooser():
    options = ["Happy", "Nostalgic", "Sad", "Cramptastic", "Serious", "Christmassy"]
    title = "How are you feeling?: "
    option, index = pick(options, title)
    optionString = option
    feeling = optionString
    return (feeling)


# Sets medium tag
def mediumChooser():
    options = ["Live Action", "Animated"]
    title = "Would you like a live action or animated movie?: "
    option, index = pick(options, title)
    optionString = option
    medium = optionString
    return (medium)


# Sets ghibli tag
def ghibliChooser():
    options = ["Yes", "No"]
    title = "Do you want a Ghibli movie?: "
    option, index = pick(options, title)
    optionString = option
    ghibli = False
    if optionString == "Yes":
        ghibli = True
    return (ghibli)


# Chooses random movie that contains all tags
def choosingFilm(feeling, medium, ghibli):
    with open("movies.json") as f:
        data = json.load(f)
        # Filter the data by class
        filteredData = [movie for movie in data if
                        feeling in movie["feeling"] and medium in movie["medium"] and movie["ghibli"] is ghibli]
        if filteredData == None or filteredData == []:
            return "Sorry, there aren't any movies that fit"
        # Select random spell
        randomMovie = filteredData[random.randint(0, len(filteredData) - 1)]
        return randomMovie['name']


# Main Function
def movieChooser():
    title()
    while True:
        input("\nPlease hit enter to begin!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        feeling = feelingChooser()
        print("You're feeling " + feeling, end="")
        input()
        medium = mediumChooser()
        print("You're wanting a " + medium + " movie", end="")
        input()
        ghibli = False
        if medium == "Animated":
            ghibli = ghibliChooser()
            if ghibli is True:
                print("You're wanting a Ghibli Movie")
            else:
                print("You don't want a Ghibli Movie")
            input()
        workingMagic()
        print()
        print("\nPerhaps you should watch..." + choosingFilm(feeling, medium, ghibli))
        answer = input("Would you like to choose another film? (y/n)\n")
        if answer == "n":
            print("\nI'm glad to have been of help!")
            break


# Animation, shamelessly taken from GeeksForGeeks
def workingMagic():
    # String to be displayed when the application is loading
    load_str = "working my movie magic..."
    ls_len = len(load_str)
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
    # used to keep the track of
    # the duration of animation
    counttime = 0
    # pointer for travelling the loading string
    i = 0
    while (counttime != 100):
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.050)
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str)
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
        # y->for storing altered ASCII code
        y = 0
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)
        # for storing the resultant string
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]
        # displaying the resultant string
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()
        # Assigning loading string
        # to the resultant string
        load_str = res
        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1


if __name__ == '__main__':
    print()
    movieChooser()
