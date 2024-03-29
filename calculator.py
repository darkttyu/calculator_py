from tkinter import *

root = Tk()
root.title("First Calculator Project")

calc_entry = Entry(root, width=35, borderwidth=5)
calc_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def insert_number(number):
    
    current = calc_entry.get()
    calc_entry.delete(0, END)
    calc_entry.insert(0, str(current) + str(number))

def clear_entry():
    calc_entry.delete(0, END)

def compute_add():
    first_num = calc_entry.get() 
    global f_num 
    global math 
    math = 'addition'
    f_num = int(first_num)
    
    calc_entry.delete(0, END)
    
def compute_subtract():
    first_num = calc_entry.get() 
    global f_num 
    global math 
    math = 'subtraction'
    f_num = int(first_num)
    
    calc_entry.delete(0, END)

def compute_multiply():
    first_num = calc_entry.get() 
    global f_num 
    global math 
    math = 'multiplication'
    f_num = int(first_num)
    
    calc_entry.delete(0, END)

def compute_divide():
    first_num = calc_entry.get() 
    global f_num 
    global math 
    math = 'division'
    f_num = int(first_num)
    
    calc_entry.delete(0, END)

def compute_operation():
    s_num = calc_entry.get()
    calc_entry.delete(0, END)
    
    if math == 'addition':
        calc_entry.insert(0, f_num + int(s_num))
    elif math == 'subtraction':
        calc_entry.insert(0, f_num - int(s_num))
    elif math == 'multiplication':
        calc_entry.insert(0, f_num * int(s_num))
    elif math == 'division':
        calc_entry.insert(0, f_num / int(s_num))
    
    
# Buttons Defined 

num_0 = Button(root, text="0", padx=40, pady=20, command=lambda: insert_number(0))
num_1 = Button(root, text="1", padx=40, pady=20, command=lambda: insert_number(1))
num_2 = Button(root, text="2", padx=40, pady=20, command=lambda: insert_number(2))
num_3 = Button(root, text="3", padx=40, pady=20, command=lambda: insert_number(3))
num_4 = Button(root, text="4", padx=40, pady=20, command=lambda: insert_number(4))
num_5 = Button(root, text="5", padx=40, pady=20, command=lambda: insert_number(5))
num_6 = Button(root, text="6", padx=40, pady=20, command=lambda: insert_number(6))
num_7 = Button(root, text="7", padx=40, pady=20, command=lambda: insert_number(7))
num_8 = Button(root, text="8", padx=40, pady=20, command=lambda: insert_number(8))
num_9 = Button(root, text="9", padx=40, pady=20, command=lambda: insert_number(9))

plus_button = Button(root, text="+", padx=39, pady=20, command=compute_add)
clear_button= Button(root, text="Clear", padx=79, pady=20, command=clear_entry)
equal_button = Button(root, text= '=', padx=91, pady=20, command=compute_operation)

minus_button = Button(root, text="-", padx=41, pady=20, command=compute_subtract)
times_button = Button(root, text="*", padx=40, pady=20, command=compute_multiply)
divide_button = Button(root, text="/", padx=41, pady=20, command=compute_divide)

# Button Position

num_0.grid(row=4, column=0)

num_1.grid(row=3, column=0)
num_2.grid(row=3, column=1)
num_3.grid(row=3, column=2)

num_4.grid(row=2, column=0)
num_5.grid(row=2, column=1)
num_6.grid(row=2, column=2)

num_7.grid(row=1, column=0)
num_8.grid(row=1, column=1)
num_9.grid(row=1, column=2)

plus_button.grid(row=5, column=0)

minus_button.grid(row=6, column=0)
times_button.grid(row=6, column=1)
divide_button.grid(row=6, column=2)

equal_button.grid(row=5, column=1, columnspan=2)
clear_button.grid(row=4, column=1, columnspan=2)
root.mainloop()
