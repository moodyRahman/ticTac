#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
HOW TO PLAY
this is a terminal tic tac toe game made by Moududur "Moody" Rahman
when requested for the input, type in the coordinate of your input
in a 0 to 2 scale
EXAMPLE
player one coor: 0 0   <enter>
     |   |    |2
  -----------
     |   |    |1
  -----------
   x |   |    |0
  -----------  y
   0 | 1 | 2  x

 and that happens
"""

from random import shuffle
import os
import time as t
# make globals
# the solution to every problem is to make more globals
global tic, isOver, turn, whoWon, message, isMulti
tic = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
isOver = False
turn = 0
whoWon = None
message = ""
isMulti = ""


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

"""""""""
┌─┐  ┬ ┬  ┌─┐  ┌─┐  ┬┌─  ┌─┐  ┬─┐  ┌─┐
│    ├─┤  ├┤   │    ├┴┐  ├┤   ├┬┘  └─┐
└─┘  ┴ ┴  └─┘  └─┘  ┴ ┴  └─┘  ┴└─  └─┘
"""""""""


# streamlines returning values from the tic tac grid
# okay not really, i just dont like typing square brackets
def chx(x, y):
    return tic[x][y]


# only plebs hardcode
def vertCheck():
    global whoWon
    for x in [0, 1, 2]:  # runs a vert check with values x = 0, 1, 2
        if chx(x, 0) == chx(x, 1) == chx(x, 2) == "x":
            whoWon = "x"
            return True
        if chx(x, 0) == chx(x, 1) == chx(x, 2) == "o":
            whoWon = "o"
            return True

    return False


def horizCheck():
    global whoWon
    for y in [0, 1, 2]:  # runs a horiz check with values y = 0, 1, 2
        if chx(0, y) == chx(1, y) == chx(2, y) == "x":
            whoWon = "x"
            return True
        if chx(0, y) == chx(1, y) == chx(2, y) == "o":
            whoWon = "o"
            return True

    return False


def diagCheck():
    global whoWon  # 2 diagonal cases, hard coded them, guess im a pleb now
    if chx(0, 0) == chx(1, 1) == chx(2, 2) == "x":
        whoWon = "x"
        return True
    if chx(0, 0) == chx(1, 1) == chx(2, 2) == "o":
        whoWon = "o"
        return True

    if chx(0, 2) == chx(1, 1) == chx(2, 0) == "x":
        whoWon = "x"
        return True
    if chx(0, 2) == chx(1, 1) == chx(2, 0) == "o":
        whoWon = "o"
        return True

    return False


def isTie():
    global whoWon, tic
    a = tic[0].count("x") + tic[0].count("o")
    b = tic[1].count("x") + tic[1].count("o")
    c = tic[2].count("x") + tic[2].count("o")
    if a + b + c == 9:
        whoWon = "tie"
        return True

    return False


# check to see if any gameover condition is met
# easier to manage as one big function checking the grid of global tic
def bigCheck():
    global isOver
    if vertCheck():
        isOver = True
    elif horizCheck():  # no particular reason why the elifs, should work the
        isOver = True   # same with three ifs
    elif diagCheck():
        isOver = True
    elif isTie():
        isOver = True


"""""""""
┌┬┐  ┬─┐  ┌─┐  ┬ ┬    ┌┐   ┌─┐  ┌─┐  ┬─┐  ┌┬┐
 ││  ├┬┘  ├─┤  │││    ├┴┐  │ │  ├─┤  ├┬┘   ││
─┴┘  ┴└─  ┴ ┴  └┴┘    └─┘  └─┘  ┴ ┴  ┴└─  ─┴┘
"""""""""


# handles drawing the board
def draw():
    global message
    clr()  # clears the screen
    print(' ' + str(tic[0][2]) + ' | ' + str(tic[1][2]) + ' | ' + str(tic[2][2]) + "  |2")
    print('-----------')
    print(' ' + str(tic[0][1]) + ' | ' + str(tic[1][1]) + ' | ' + str(tic[2][1]) + "  |1")
    print('-----------')
    print(' ' + str(tic[0][0]) + ' | ' + str(tic[1][0]) + ' | ' + str(tic[2][0]) + "  |0")
    print('-----------  y')
    print(" 0 | 1 | 2  x")
    print (message)


"""
┬  ┌┐┌  ┌┬┐  ┌─┐  ┬─┐  ┌─┐  ┌─┐  ┌┬┐  ┬  ┌─┐  ┌┐┌  ┌─┐
│  │││   │   ├┤   ├┬┘  ├─┤  │     │   │  │ │  │││  └─┐
┴  ┘└┘   ┴   └─┘  ┴└─  ┴ ┴  └─┘   ┴   ┴  └─┘  ┘└┘  └─┘
"""


# super mega useful code
# given the raw_input of two numbers,
# return a list with two numbers in the strings
def numIso(input):
    return [int(s) for s in input.split() if s.isdigit()]


def turnZero():
    global turn, message
    try:
        message = ""
        if turn == 0:
            input1 = numIso(raw_input("(x)player one coor: "))
            if tic[input1[0]][input1[1]] == " ":
                tic[input1[0]][input1[1]] = "x"
            else:
                message = "cant place where there is already a piece"
                play()
            turn = 1
            play()    # once the player has inputted, run play again
    except IndexError:
        message = "type coordinates between 0 and 2"
        play()


def compAI():
    global tic
    x = [0, 1, 2]
    y = [0, 1, 2]
    shuffle(x)
    shuffle(y)
    for a in x:
        for b in y:
            if tic[a][b] != "x":
                if tic[a][b] != "o":
                    return [a, b]


def turnOne():
    global turn, message, tic, isMulti

    try:
        message = ""
        if turn == 1:
            if isMulti:
                input1 = numIso(raw_input("(o)player two coor: "))
            else:
                input1 = compAI()

            if tic[input1[0]][input1[1]] == " ":
                tic[input1[0]][input1[1]] = "o"
            else:
                message = "cant place where there is already a piece"
                play()
        turn = 0
        play()    # same as above comment
    except IndexError:
        message = "type coordinates between 0 and 2"
        play()


def play():
    global message, whoWon
    draw()  # draw the board
    global turn, tic

    bigCheck()
    if isOver is False:
        turnZero()
        turnOne()
    else:
        if whoWon == "x":
            print "player 1 won (x)"
            quit()
        elif whoWon == "tie":
            print "issa tie"
            quit()
        else:
            print "player 2 won (o)"
            quit()


def multChoose():
    global isMulti
    clr()
    print "one player against computer or two players?"
    print "type two player or computer"
    print "type help for help"
    isMulti = raw_input(": ")
    if isMulti == "two player":
        isMulti = True
    elif isMulti == "computer":
        isMulti = False
    elif isMulti == "help":
        help()
        multChoose()
    else:
        print "two player or computer"
        raw_input()
        multChoose()


def help():
    clr()
    print "type in the x-y coordinate of where you want"
    t.sleep(1)
    print "your piece to go, seperated by a space"
    t.sleep(1)
    print "<ENTER>"
    t.sleep(2)
    raw_input()
    clr()
    print "first to get three in a row wins"
    t.sleep(1)
    print "coded moududur 'moody' rahman, 2018"
    print "draw() function made by c. kaung and modded by moody"
    t.sleep(2)
    print "<ENTER>"
    raw_input()


def bigOleWrapper():
    multChoose()
    play()


# boilerplate code
if __name__ == '__main__':
    bigOleWrapper()
