from tkinter import *
import pandas_datareader as dr
from datetime import datetime

def enter(event):
    add_command()

def delete(event):
    delete_stock()

def caps(event):
    stock_text.set(stock_text.get().upper())

def today():
    e3.insert(0,datetime.now().strftime('%Y-%m-%d'))

def add_command():
    list1.insert(END,stock_text.get())
    e1.delete(0,END)

def get_selected_row(event):
    global index
    index=list1.curselection()

def delete_stock():
    list1.delete(index)

def data_export():
    for item in list1.get(0,END):
        dr.DataReader(item,'yahoo',startdate_text.get(),enddate_text.get()).to_csv(item+'.csv')

window=Tk()
window.wm_title("Stock .csv exporter")

l1=Label(window,text="Stock name")
l1.grid(row=0,column=0)

l2=Label(window,text="Start Date")
l2.grid(row=1,column=0)

l3=Label(window,text="End Date")
l3.grid(row=1,column=2)

stock_text=StringVar()
e1=Entry(window,textvariable=stock_text)
e1.grid(row=0,column=1)

e1.bind('<Return>',enter)
e1.bind("<KeyRelease>", caps)

startdate_text=StringVar()
e2=Entry(window,textvariable=startdate_text)
e2.grid(row=1,column=1)

enddate_text=StringVar()
e3=Entry(window,textvariable=enddate_text)
e3.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)
list1.bind('<Delete>',delete)

b1=Button(window,text="Today's Date", width=20,command=today)
b1.grid(row=3,column=3)

b2=Button(window,text="Add stock ('Enter')", width=20,command=add_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Remove stock ('Delete')", width=20,command=delete_stock)
b3.grid(row=5,column=3)

b4=Button(window,text="Generate .csv", width=20, bg='green',command=data_export)
b4.grid(row=6,column=3)

window.mainloop()
