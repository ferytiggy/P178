# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:08:00 2024

@author: Aidan
"""

from tkinter import *
import random

root = Tk()
root.title("P178")
root.geometry("800x1200")
root.config(bg="cyan")

color_random = Label(root, bg="white")
color_random.place(relx=0.5, rely=0.5, anchor=CENTER)

class game:
    def __init__(self):
        self.__score = 0
        
    def updateGame():
        self.text = ["ROSA", "VERDE", "ROJO", "AZUL", "AMARILLO", "NARANJA"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black", "green", "red", "blue", "yellow", "orange"]
        self.random_number_for_color = random.randint(0,5)
        color_random["text"] = self.color[self.random_number_for_text]
        color_random["fg"] = self.color[self.random_number_for_color]
        
btn = Button(root, text="Iniciar", command=updateGame(), bg="white", fg="white",
relief=FLAT, padx=10, pady=1, font=("Arial",15))

root.mainloop()