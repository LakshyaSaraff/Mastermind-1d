import tkinter
import random
import os
from Constants import Colors, width, height, thickness
from Game import Game
from GUI import Interface


root = tkinter.Tk()
frame = tkinter.Frame(root)
canvas = tkinter.Canvas(frame, width=width,height=height, highlightthickness=thickness,highlightbackground='black', 
            relief=tkinter.FLAT,bg=Colors['White'],bd=0)


