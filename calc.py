from tkinter import *   
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

data_write = open("data.txt", "w")

tk = Tk()  
tk.geometry('463x123')  
tk.title('Калькулятор')

text = Entry(tk, width=77)
text.grid(row=0, column=0, columnspan=11)

def pred():    
    import prediction

def one():
    text.insert(END, '1')
def two():
    text.insert(END, '2')
def three():
    text.insert(END, '3')
def four():
    text.insert(END, '4')
def five():
    text.insert(END, '5')
def six():
    text.insert(END, '6')
def seven():
    text.insert(END, '7')
def eight():
    text.insert(END, '8')
def nine():
    text.insert(END, '9')
def zero():
    text.insert(END, '0')
def fsp():
    text.insert(END, '.')
def sps():
    text.insert(END, ' ')
def ent():
    txt = text.get()
    txt_arr = txt.split(' ')
    for i in txt_arr:
        data_write.write(i + '\n')
    data_write.close()
    pred()
b1= Button(tk, text = '1', bg='gray', fg='white', width = 15, command=one)
b1.grid(row=1, column=0)
b2= Button(tk, text = '2', bg='gray', fg='white', width = 15, command=two).grid(row=1, column=1)
b3= Button(tk, text = '3', bg='gray', fg='white', width = 15, command=three).grid(row=1, column=2)
b_ent= Button(tk, text = 'Ввод', bg='gray', fg='white', width = 15, command=ent).grid(row=1, column=3)
b4= Button(tk, text = '4', bg='gray', fg='white', width = 15, command=four).grid(row=2, column=0)
b5= Button(tk, text = '5', bg='gray', fg='white', width = 15, command=five).grid(row=2, column=1)
b6= Button(tk, text = '6', bg='gray', fg='white', width = 15, command=six).grid(row=2, column=2)
b_ft = Button(tk, text = '.', bg='gray', fg='white', width = 15, command=fsp).grid(row=2, column=3)
b7= Button(tk, text = '7', bg='gray', fg='white', width = 15, command=seven).grid(row=3, column=0)
b8= Button(tk, text = '8', bg='gray', fg='white', width = 15, command=eight).grid(row=3, column=1)
b9= Button(tk, text = '9', bg='gray', fg='white', width = 15, command=nine).grid(row=3, column=2)
b0= Button(tk, text = '0', bg='gray', fg='white', width = 15, command=zero).grid(row=3, column=3)
but_sps = Button(tk, text = 'space', bg='gray', fg='white', width=65, command=sps)
but_sps.grid(row=4, column=0, columnspan=4)

tk.mainloop()