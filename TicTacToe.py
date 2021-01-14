#For details, see Project document.

from tkinter import *
import tkinter.messagebox
import random

	
tk = Tk()
tk.title("Tic Tac Toe")

buttons = StringVar()

button1 = Button(tk,text=" ", font=('Comic 26 bold'), height = 2, width = 4, command = lambda:checker(button1,playerLetter))
button1.grid(row = 0, column = 0, sticky = S+N+E+W)

button2 = Button(tk,text=" ", font=('Comic 26 bold'), height = 2, width = 4, command = lambda:checker(button2,playerLetter))
button2.grid(row = 0, column = 1, sticky = S+N+E+W)

button3 = Button(tk,text=" ", font=('Comic 26 bold'), height = 2, width = 4, command = lambda:checker(button3,playerLetter))
button3.grid(row = 0, column = 2, sticky = S+N+E+W)

button4 = Button(tk,text=" ", font=('Comic 26 bold'), height = 2, width = 4, command = lambda:checker(button4,playerLetter))
button4.grid(row = 1, column = 0, sticky = S+N+E+W)

button5 = Button(tk,text=" ", font=('Comic 26 bold'), height = 2, width = 4, command = lambda:checker(button5,playerLetter))
button5.grid(row = 1, column = 1, sticky = S+N+E+W)

button6 = Button(tk,text=" ", font=('Comic 26 bold'), height = 2, width = 4, command = lambda:checker(button6,playerLetter))
button6.grid(row = 1, column = 2, sticky = S+N+E+W)

button7 = Button(tk,text=" ", font=('Comic 26 bold'), height = 2, width = 4, command = lambda:checker(button7,playerLetter))
button7.grid(row = 2, column = 0, sticky = S+N+E+W)

button8 = Button(tk,text=" ", font=('Comic 26 bold'), height = 2, width = 4, command = lambda:checker(button8,playerLetter))
button8.grid(row = 2, column = 1, sticky = S+N+E+W)

button9 = Button(tk,text=" ", font=('Comic 26 bold'), height = 2, width = 4, command = lambda:checker(button9,playerLetter))
button9.grid(row = 2, column = 2, sticky = S+N+E+W)

def checker(buttons,playerLetter):
	if buttons["text"] == " ":
		buttons["text"] = playerLetter
		if(checkwin()!=1 and checkdraw()!=1):
			compplay(computerLetter)
			if(checkwin()!=1):
				checkdraw()

def checkdraw():
	if(button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and
		button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and
		button7["text"] != " " and button8["text"] != " " and button9["text"] != " "):
		tkinter.messagebox.showinfo("Notice!","Game draw!")
		return 1
		
def randomLet(computerLetter):
	turn = 0
	while turn != 1:
		rand = random.randint(1,10)
		if rand == 1 and button1["text"] == " ":
			button1["text"] = computerLetter
			turn = 1
		elif rand == 2 and button2["text"] == " ":
			button2["text"] = computerLetter
			turn = 1
		elif rand == 3 and button3["text"] == " ":
			button3["text"] = computerLetter
			turn = 1
		elif rand == 4 and button4["text"] == " ":
			button4["text"] = computerLetter
			turn = 1
		elif rand == 5 and button5["text"] == " ":
			button5["text"] = computerLetter
			turn = 1
		elif rand == 6 and button6["text"] == " ":
			button6["text"] = computerLetter
			turn = 1
		elif rand == 7 and button7["text"] == " ":
			button7["text"] = computerLetter
			turn = 1
		elif rand == 8 and button8["text"] == " ":
			button8["text"] = computerLetter
			turn = 1
		elif rand == 9 and button9["text"] == " ":
			button9["text"] = computerLetter
			turn = 1

def checkwin():	
	if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
		button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
		button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
		button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
		button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
		button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
		button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
		button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
		tkinter.messagebox.showinfo("Notice!","Winner is player X!")
		return 1
		
	elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
		button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
		button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
		button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
		button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
		button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
		button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
		button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
		tkinter.messagebox.showinfo("Notice!","Winner is player O!")
		return 1
		
		
def compplay(computerLetter):	
	if(button1["text"] == button2["text"] != " " and button3["text"] == " "):
		button3["text"] = computerLetter
	elif(button1["text"] == button3["text"] != " " and button2["text"] == " "):
		button2["text"] = computerLetter
	elif(button2["text"] == button3["text"] != " " and button1["text"] == " "):
		button1["text"] = computerLetter	
	elif(button4["text"] == button5["text"] != " " and button6["text"] == " "):
		button6["text"] = computerLetter
	elif(button4["text"] == button6["text"] != " " and button5["text"] == " "):
		button5["text"] = computerLetter
	elif(button5["text"] == button6["text"] != " " and button4["text"] == " "):
		button4["text"] = computerLetter		
	elif(button7["text"] == button8["text"] != " " and button9["text"] == " "):
		button9["text"] = computerLetter
	elif(button7["text"] == button9["text"] != " " and button8["text"] == " "):
		button8["text"] = computerLetter
	elif(button8["text"] == button9["text"] != " " and button7["text"] == " "):
		button7["text"] = computerLetter
	elif(button3["text"] == button5["text"] != " " and button7["text"] == " "):
		button7["text"] = computerLetter
	elif(button3["text"] == button7["text"] != " " and button5["text"] == " "):
		button5["text"] = computerLetter
	elif(button5["text"] == button7["text"] != " " and button3["text"] == " "):
		button3["text"] = computerLetter
	elif(button1["text"] == button5["text"] != " " and button9["text"] == " "):
		button9["text"] = computerLetter
	elif(button1["text"] == button9["text"] != " " and button5["text"] == " "):
		button5["text"] = computerLetter
	elif(button5["text"] == button9["text"] != " " and button1["text"] == " "):
		button1["text"] = computerLetter		
	elif(button4["text"] == button1["text"] != " " and button7["text"] == " "):
		button7["text"] = computerLetter
	elif(button4["text"] == button7["text"] != " " and button1["text"] == " "):
		button1["text"] = computerLetter
	elif(button1["text"] == button7["text"] != " " and button4["text"] == " "):
		button4["text"] = computerLetter	
	elif(button2["text"] == button5["text"] != " " and button8["text"] == " "):
		button8["text"] = computerLetter
	elif(button2["text"] == button8["text"] != " " and button5["text"] == " "):
		button5["text"] = computerLetter
	elif(button5["text"] == button8["text"] != " " and button2["text"] == " "):
		button2["text"] = computerLetter
	elif(button3["text"] == button9["text"] != " " and button6["text"] == " "):
		button6["text"] = computerLetter
	elif(button3["text"] == button6["text"] != " " and button9["text"] == " "):
		button9["text"] = computerLetter
	elif(button9["text"] == button6["text"] != " " and button3["text"] == " "):
		button3["text"] = computerLetter
	else:
		randomLet(computerLetter)

playerLetter = ""
computerLetter = ""
print("Do you want to be X or O? X goes first! (Press any other button to quit): ")
playerLetter = str(input())
if(playerLetter == "X"):
	computerLetter = "O"
elif(playerLetter == "O"):
	computerLetter = "X"
	compplay(computerLetter)
else:
	exit()		

tk.mainloop()
