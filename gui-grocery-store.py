#GUI for a Grocery Store
#Assuming that each items will have its specific name

#import os
#import time
import tkinter as gui

items = {}
ordered_items = {}

def getInfo():
    fileData = []
    file = open('data.txt', 'r')
    line=file.readline()
    while (line!=''):
        line=line.strip('\n')
        fileData.append(line)
        line=file.readline()
    for i in range(len(fileData)):
        line=fileData[i]
        isLast=0
        newline=''
        number=''
        for i in range(len(line)):
            letter=line[i]
            if (letter==' '):
                isLast=1
                continue
            if isLast==0:
                newline=newline+letter
            else:
                number=int(letter)
        items[newline]=number

getInfo()

total_price = 0
display_string=''

def calculate():
    global total_price
    global display_string
    item_name = (item_entry.get()).lower()
    item_amount=amount_entry.get()
    if item_name in items:
        #print("test1")
        if item_name in ordered_items:
            new_item_amount=int(ordered_items[item_name])+int(item_amount)
            ordered_items[item_name]=str(new_item_amount)
        else:
            ordered_items[item_name]=item_amount
        items_key=''
        for key in items:
            if (key==item_name):
                items_key=key
        item_price=items[items_key]
        item_price=int(item_price)*int(item_amount)
        total_price=total_price+item_price
        total_price_label.config(text = ('The total price is: '+ str(total_price)))
        for key in ordered_items:
            display_string=display_string + (key+': '+ordered_items[key]+'\n')
        display_item_label.config(text=display_string)
        display_string=''
    else:
        #print("test2")
        error_window=gui.Tk()
        def destroyer():
            error_window.destroy()
        error_window.geometry("300x200")
        error_window.configure(bg='blue')
        error_label=gui.Label(error_window, text="Entered item is not in stock or is not a valid input")
        error_label.configure(bg='blue', fg='white')
        error_ok_button=gui.Button(error_window, text="OK", command=destroyer)
        error_label.pack(pady=5)
        error_ok_button.pack(pady=5)
        error_window.mainloop()

window=gui.Tk()
window.geometry('720x480')
window.title('Grocery Store')
window.configure(bg='blue')
frame= gui.Frame(window, relief= 'sunken', bg= "blue")
item_label=gui.Label(text='Enter the item here: ')
item_label.configure(bg='blue', fg='white')
item_entry = gui.Entry()
amount_label=gui.Label(text='Enter the amount here (negative to remove items): ')
amount_label.configure(bg='blue', fg='white')
amount_entry = gui.Entry()
total_price_label=gui.Label(text=('The total price is: '+ str(total_price)), font=15)
total_price_label.configure(bg='blue', fg='white')
button=gui.Button(text='Click to add item', command=calculate)
display_item_label=gui.Label(text='No items added yet.')
display_item_label.configure(bg='blue', fg='white')
frame.pack(pady=10)
item_label.pack(pady=5)
item_entry.pack(pady=5)
amount_label.pack(pady=5)
amount_entry.pack(pady=5)
total_price_label.pack(pady=5)
button.pack(pady=5)
display_item_label.pack(pady=5)
window.mainloop()