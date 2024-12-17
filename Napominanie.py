from cProfile import label
from tkinter import *
from tkinter import simpledialog as sd
from  tkinter import messagebox as md
import datetime
import pygame
import time

t = None

def set():
    global t
    rem = sd.askstring("Время напоминания","Установить время (формат 24")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            t = dt.timestamp()
            print(t)
            label.config(test=f"Напоминание установлено на: {hour:02}:{minute:02}")
        except ValueError:
            md.showerror("Ощибка","Не верный формат времени")




