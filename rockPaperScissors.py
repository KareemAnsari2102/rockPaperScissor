from tkinter import *
import random  
import tkinter 

user = int
computer = int

win = 0
lose = 0

def rps(win, lose, user):
    computer = random.randrange(1, 4)

    if user == computer:
        var.set("It's a draw. \n No points")
    elif user == 1 and computer == 3:
        var.set("You choose Rock, I choose scissors. \nYou Win!")
        wins.set(wins.get() + 1)
    elif user == 1 and computer == 2:
        var.set("You choose Rock, I choose Paper. \nYou Lose!")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 2 and computer == 1:
        var.set("You choose Paper, I choose Rock. \nYou Win!")
        wins.set(wins.get() + 1)
    elif user == 2 and computer == 3:
        var.set("You choose Paper, I choose Scissors. \nYou Lose!")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 3 and computer == 1:
        var.set("You choose Scissors, I choose Rock. \nYou Lose!")
        lose += 1
        wins.set(wins.get() - 1)
    elif user == 3 and computer == 2:
        var.set("You choose Scissors, I choose Paper. \nYou Win!")
        wins.set(wins.get() + 1)
    else:
        var.set("Thanks for playing. \You Have " + str(win) + " wins and " + str(lose) + " losses.")


top = tkinter.Tk()

top.wm_title("Rock Paper Scissor")

top.minsize(width=400, height=200)
top.maxsize(width=400, height=200)

B1 = tkinter.Button(top, text = "Rock", command= lambda: rps(win, lose, 1))
B1.grid(row=0, column=1)
B2 = tkinter.Button(top, text = "Paper", command= lambda: rps(win, lose, 2))
B2.grid(row=0, column=2)
B3 = tkinter.Button(top, text = "Scissors", command= lambda: rps(win, lose, 3))
B3.grid(row=0, column=3)

space = tkinter.Label(top, text="")
space.grid(row=1)

var = StringVar()
var.set("Welcome")

l = Label(top, textvariable= var)
l.grid(row=2, column=2)

wins = IntVar()
wins.set(win)

w = Label(top, textvariable= wins)
w.grid(row=3, column=3)

labeled = Label(top, text= "Score: ")
labeled.grid(row=3, column=1)

copy = Label(top, text= "Rock Paper Scissor Game")
copy.grid(row=5, column=2)

top.mainloop()