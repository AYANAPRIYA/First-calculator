from tkinter import *

root = Tk()
display = Entry(root)
display.grid(sticky=N,columnspan=50)

def getvarriables(number):
	current = display.get()
	display.delete(0, END)
	display.insert(0, (current) + (number))
def cleardata():
	display.delete(0, END)

def add():
	first_num = display.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_num)
	display.delete(0, END)
def sub():
	first_num = display.get()
	global f_num
	global math
	math = "substraction"
	f_num = int(first_num)
	display.delete(0, END)
def mult():
	first_num = display.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_num)
	display.delete(0, END)
def div():
	first_num = display.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_num)
	display.delete(0, END)


def equals():
	second_num = display.get()
	display.delete(0, END)


	if math == "addition":
		display.insert(0, f_num + int(second_num))
	elif math == "substraction":
		display.insert(0, f_num - int(second_num))
	elif math == "multiplication":
		display.insert(0, f_num * int(second_num))
	elif math == "division":
		display.insert(0, f_num / int(second_num))   		


label_1 = Button(root, text="1", command=lambda: getvarriables("1"), padx=40,pady=30)
label_2 = Button(root, text="2", command=lambda: getvarriables("2"), padx=40,pady=30)
label_3 = Button(root, text="3", command=lambda: getvarriables("3"), padx=40,pady=30)
label_4 = Button(root, text="4", command=lambda: getvarriables("4"), padx=40,pady=30)
label_5 = Button(root, text="5", command=lambda: getvarriables("5"), padx=40,pady=30)
label_6 = Button(root, text="6", command=lambda: getvarriables("6"), padx=40,pady=30)
label_7 = Button(root, text="7", command=lambda: getvarriables("7"), padx=40,pady=30)
label_8 = Button(root, text="8", command=lambda: getvarriables("8"), padx=40,pady=30)
label_9 = Button(root, text="9", command=lambda: getvarriables("9"), padx=40,pady=30)
label_0 = Button(root, text="0", command=lambda: getvarriables("0"), padx=40,pady=30)

label_add = Button(root, text="+", command=add, padx=40,pady=30)
label_sub = Button(root, text="-", command=sub, padx=40,pady=30)
label_mul = Button(root, text="*", command=mult, padx=40,pady=30)
label_div = Button(root, text="/", command=div, padx=40,pady=30)
label_clr = Button(root, text="clr", command=cleardata, padx=40,pady=30)
label_eqls = Button(root, text="=", command=equals, padx=40,pady=30)
label_1.grid(row=1, column=0, columnspan=1)
label_2.grid(row=1, column=1, columnspan=1)
label_3.grid(row=1, column=2, columnspan=1)
label_4.grid(row=2, column=0, columnspan=1)
label_5.grid(row=2, column=1, columnspan=1)
label_6.grid(row=2, column=2, columnspan=1)
label_7.grid(row=3, column=0, columnspan=1)
label_8.grid(row=3, column=1, columnspan=1)
label_9.grid(row=3, column=2, columnspan=1)
label_0.grid(row=4, column=1, columnspan=1)
label_add.grid(row=1, column=3, columnspan=1)
label_sub.grid(row=2, column=3, columnspan=1)
label_mul.grid(row=3, column=3, columnspan=1)
label_div.grid(row=4, column=3, columnspan=1)
label_clr.grid(row=4, column=0, columnspan=1)
label_eqls.grid(row=4, column=2, columnspan=1)
root.mainloop()
