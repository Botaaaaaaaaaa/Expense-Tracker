import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter.messagebox import showerror

win=tk.Tk()
win.title("EXPENSE TRACKER")
win.geometry("900x500")
img=tk.PhotoImage(file="C:/Users/user/Downloads/taskpy/wallet.png")
win.iconphoto(False,img)

fr1 = tk.Frame(win, bg="red")
fr1.grid(row=0, column=0)

def add_expense():
    entries=[payee_en,des_entry,amount_en,mode_combo]
    flag = False

    for entry in entries:
        if len(entry.get())==0:
            flag = True 
            break
    if flag==True:
         showerror(title="ERROR",message="Все поля должны быть заполнены")
    else:
        date = date_entry.get()
        payee = payee_en.get()
        description = des_entry.get()
        amount = amount_en.get()
        payment_mode = mode_combo.get()

        tree.insert("", "end", values=(date, payee, description, amount, payment_mode))

        date_entry.delete(0, tk.END)
        payee_en.delete(0, tk.END)
        des_entry.delete(0, tk.END)
        amount_en.delete(0, tk.END)
        mode_combo.delete(0, tk.END)

def delete_expense():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

def delete_all():
    tree.delete(*tree.get_children())

def edit_expense():
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, "values")

    date_entry.delete(0, tk.END)
    date_entry.insert(0, values[0])

    payee_en.delete(0, tk.END)
    payee_en.insert(0, values[1])

    des_entry.delete(0, tk.END)
    des_entry.insert(0, values[2])

    amount_en.delete(0, tk.END)
    amount_en.insert(0, values[3])

    mode_combo.delete(0, tk.END)
    mode_combo.insert(0, values[4])
    tree.delete(selected_item)

def sum_amount():
    tree.get_children()
    sun_sum = 0
    for i in tree.get_children():
        tree.item(i)['values'][3]
        n=int(tree.item(i)['values'][3])
        sun_sum += n

    lbl_amount.config(text= sun_sum)

date_entry=DateEntry(fr1,year=datetime.today().year,date_pattern="d.m.Y")
date_entry.grid(row=1,column=0,sticky="w")

tk.Label(fr1,text="Date: ",bg="red").grid(row=0,column=0,sticky="w")

des_label=tk.Label(fr1,text="Description:",bg="red").grid(row=3,column=0,sticky="w")
des_entry=tk.Entry(fr1)
des_entry.grid(row=4,column=0,sticky="w",columnspan=4)
amount_lb=tk.Label(fr1,text="Amount:",bg="red").grid(row=5,column=0,sticky="w")
amount_en=tk.Entry(fr1)
amount_en.grid(row=6,column=0,sticky="w")
payee_lb=tk.Label(fr1,text="Payee:",bg="red").grid(row=7,column=0,sticky="w")
payee_en=tk.Entry(fr1)
payee_en.grid(row=8,column=0,columnspan=5,sticky="w")
mode_lb=tk.Label(fr1,text="Mode of Payment:",bg="red").grid(row=9,column=0,sticky="w")
combo = ["Cash", "Credit Card", "VISA", "Gift Card","Mobile Payment"]
mode_combo = ttk.Combobox(fr1,values=combo)
mode_combo.grid(row=10,column=0,sticky="w")
lb_amount=tk.Label(fr1,text="Sum amounts: ",bg="red").grid(row=17,column=0,sticky="w")

lbl_amount=tk.Label(fr1,text="",bg="orange")
lbl_amount.grid(row=18,column=0,sticky="w",ipadx=35)

btn=tk.Button(fr1,text="show",bg="orange",command=sum_amount).grid(row=17,column=1)
add_button = tk.Button(fr1, text="Add expense",bg="pink", command=add_expense).grid(row=13,column=0,ipadx=5,ipady=5,pady=8)
con_button = tk.Button(fr1,text="Delete expense",bg="pink",command=delete_expense).grid(row=16,column=0,ipadx=5,ipady=5,pady=8)
edit_button = tk.Button(fr1,text="Edit expense",bg="pink",command=edit_expense).grid(row=14,column=0,ipadx=5,ipady=5,pady=8)
del_button=tk.Button(fr1,text="Delete All",command=delete_all,bg="pink").grid(row=15,column=0,ipadx=5,ipady=5,pady=8)

tree = ttk.Treeview(win, columns=("Date", "Payee", "Description", "Amount", "Mode of Payment"), show="headings")

tree.heading("Date", text="Date")
tree.heading("Payee", text="Payee")
tree.heading("Description", text="Description")
tree.heading("Amount", text="Amount")
tree.heading("Mode of Payment", text="Mode of Payment")

tree.column("Date", width=100)
tree.column("Payee", width=100)
tree.column("Description", width=150)
tree.column("Amount", width=80)
tree.column("Mode of Payment", width=150)

fr3=tk.Frame(bg="blue").grid(row=2,column=2)
tree.grid(fr3,row=0, column=1, padx=10, pady=10, columnspan=3)

win.mainloop()