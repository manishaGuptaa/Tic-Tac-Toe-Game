from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Tic Tac Toe")
clicked=True #if x is clicked
count =0
def click(b):
    global clicked, count
    if b["text"]==" " and clicked == True:
        b["text"] = "X"
        clicked=False
        count +=1
        checkifwon()
    elif b["text"]==" " and clicked == False:
         b["text"] = "O"
         clicked=True
         count +=1
         checkifwon()
    else:
         messagebox.showerror("Tic Tac Toe","This box is already selected\nPlease select another box.")
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    
def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"]=="X":
        winner = True
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,X won")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]=="X":
        winner = True
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,X won")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]=="X":
        winner = True
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,X won")
        disable_all_buttons()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]=="X":
        winner = True
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,X won")
        disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]=="X":
        winner = True
        b5.config(bg="green")
        b2.config(bg="green")
        b8.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,X won")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b3["text"]=="X":
        winner = True
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,X won")
        disable_all_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]=="X":
        winner = True
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,X won")
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]=="X":
        winner = True
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,X won")      
        disable_all_buttons()
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]=="O":
        winner = True
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,O won")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]=="O":
        winner = True
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,O won")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]=="O":
        winner = True
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,O won")
        disable_all_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]=="O":
        winner = True
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,O won")
        disable_all_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]=="O":
        winner = True
        b5.config(bg="green")
        b2.config(bg="green")
        b8.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,O won")
        disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b3["text"]=="O":
        winner = True
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,O won")
        disable_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]=="O":
        winner = True
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,O won")
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]=="O":
        winner = True
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        messagebox.showinfo("Tic Tac Toe", "Congratulations,O won")
        disable_all_buttons()
    if count==9 and winner==False:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie! \n No one wins ")
        disable_all_buttons()
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9;
    global clicked,count
    clicked=True
    count=0
    b1=Button(root,font="Lucida 25 bold",text=" ",height=3,width=6,bg="SystemButtonFace",command=lambda:click(b1))
    b2=Button(root,font="Lucida 25 bold",text=" ",height=3,width=6,bg="SystemButtonFace",command=lambda:click(b2))
    b3=Button(root,font="Lucida 25 bold",text=" ",height=3,width=6,bg="SystemButtonFace",command=lambda:click(b3))
    b4=Button(root,font="Lucida 25 bold",text=" ",height=3,width=6,bg="SystemButtonFace",command=lambda:click(b4))
    b5=Button(root,font="Lucida 25 bold",text=" ",height=3,width=6,bg="SystemButtonFace",command=lambda:click(b5))
    b6=Button(root,font="Lucida 25 bold",text=" ",height=3,width=6,bg="SystemButtonFace",command=lambda:click(b6))
    b7=Button(root,font="Lucida 25 bold",text=" ",height=3,width=6,bg="SystemButtonFace",command=lambda:click(b7))
    b8=Button(root,font="Lucida 25 bold",text=" ",height=3,width=6,bg="SystemButtonFace",command=lambda:click(b8))
    b9=Button(root,font="Lucida 25 bold",text=" ",height=3,width=6,bg="SystemButtonFace",command=lambda:click(b9))
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)
menu=Menu(root)
root.config(menu=menu)
options=Menu(menu, tearoff=False)
menu.add_cascade(label="Options",menu=options)
options.add_command(label="Reset Game", command=reset)
reset()
root.mainloop()


