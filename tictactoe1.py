from tkinter import *
from tkinter import messagebox
import random
from turtle import position

root = Tk()
root.title('chriswolf - Tic-Tac-Toe') 

# X goes first
clicked = True
count = 0


# disable all buttons
def disableAllButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# check for winner
def winner():
    global win 
    win = False

    # X rows
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n X wins")
        disableAllButtons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n X wins")
        disableAllButtons()
    
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n X wins")
        disableAllButtons()


    # X Columns
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n X wins")
        disableAllButtons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n X wins")
        disableAllButtons()
    
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n X wins")
        disableAllButtons()
    
    # X diagonals
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations"" \n X wins")
        disableAllButtons()
    
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n X wins")
        disableAllButtons()

    # 0 rows
    elif b1["text"] == "0" and b2["text"] == "0" and b3["text"] == "0":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n 0 wins")
        disableAllButtons()

    elif b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n 0 wins")
        disableAllButtons()
    
    elif b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n 0 wins")
        disableAllButtons()


    # 0 Columns
    elif b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n 0 wins")
        disableAllButtons()

    elif b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0":
        b2.config(bg="green")
        b5.config(bg="green") 
        b8.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n 0 wins")
        disableAllButtons()
    
    elif b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n 0 wins")
        disableAllButtons()
    
    # 0 diagonals
    elif b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n 0 wins")
        disableAllButtons()
    
    elif b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        win = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations \n 0 wins")
        disableAllButtons()

    # check if tie
    if count == 9 and win == False:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie ")

        

# Button clicked function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "0"
        clicked = True
        count += 1
        winner()
    else:
        messagebox.showerror("Tic-Tac-Toe", "That box is already occupied. \n Pick another box" )


# reset menu
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    
    messagebox.showinfo("Tic-Tac-Toe", "The game has been restated.")

    # Build buttons
    b1 = Button(root, text=" ", font=("Helveto", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helveto", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helveto", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helveto", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helveto", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helveto", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helveto", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helveto", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helveto", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # Grid buttons to screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    

# menu
myMenu = Menu(root)
root.config(menu=myMenu)

# options menu
optionMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Rest Game", command=reset)


reset()

root.mainloop() 