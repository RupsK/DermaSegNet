# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 18:07:43 2023

@author: rupal
"""

from tkinter import messagebox
from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Smart AIDermatology")
root.geometry('800x700')

root.config(bg ='Green')


image1 = Image.open("C:/Users/rupal/OneDrive/Desktop/6.jpg")
image1 = image1.resize((124,124))
bg = ImageTk.PhotoImage(image1)

image2 = Image.open("C:/Users/rupal/OneDrive/Desktop/7.png")
image2 = image2.resize((124,124))
bg2 = ImageTk.PhotoImage(image2)


label = tk.Label(root, image=bg).place(x = 10, y= 10)
label = tk.Label(root, image=bg2).place(x = 660, y= 10)

Label(root, text="Welcome to AI-Derma solutions", font = ("Britannic Bold",25)).place(x = 170, y =50)

Button(root, text="Upload image", font = ("Arial",14), foreground= 'black').place(x = 320, y =150)


image3 = Image.open("C:/Users/rupal/OneDrive/Desktop/try/276_GrabCut.png")
image3 = image3.resize((224,224))
photo = ImageTk.PhotoImage(image3)
label = tk.Label(root, image=photo).place(x = 390, y= 200)

image4 = Image.open("C:/Users/rupal/OneDrive/Desktop/try/276.jpg")
image4 = image4.resize((224,224))
photo1 = ImageTk.PhotoImage(image4)
label2 = tk.Label(root, image=photo1).place(x = 140, y= 200)



result= tk.Button(root, text ="Diagnosis", font = ("Arial",14), justify= 'center').place(x = 345, y =450)

#entry = tk.Entry(font=("Arial",14 ), justify= 'center').place(x = 280, y =500)
lable = tk.Label(text = "Melanoma skin cancer", font = ("Arial", 14)).place(x = 300, y =500)

label = tk.Label(text="* Consult medical expert for further treatment", font = ("Arial",14), foreground= 'red').place(x = 220, y =600)

root.mainloop()