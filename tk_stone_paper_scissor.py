from tkinter import *
import tkinter
import random

m=tkinter.Tk()
m.geometry("350x300")
m.title("Stone Paper Scissor")

compValues={"0":"Stone","1":"Paper","2":"Scissor"}

def reset_game():
    b1["state"]="active"
    b2["state"]="active"
    b3["state"]="active"
    l2.config(text="Player")
    l4.config(text="Computer")
    l3.config(text="")

def disable():
    b1["state"]="disable"
    b2["state"]="disable"
    b3["state"]="disable"


def rock():
    comp=compValues[str(random.randrange(0,2))]
    if comp=="Stone":
        res="Draw!"
    elif comp=="Paper":
        res="Computer wins!"
    else:
        res="You win!"

    l2.config(text="Stone")
    l4.config(text=comp)
    l5.config(text=res, fg="black")
    disable()

def paper():
    comp=compValues[str(random.randrange(0,2))]
    if comp=="Paper":
        res="Draw!"
    elif comp=="Scissor":
        res="Computer wins!"
    else:
        res="You win!"

    l2.config(text="Paper")
    l4.config(text=comp)
    l5.config(text=res, fg="black")
    disable()

def scissor():
    comp=compValues[str(random.randrange(0,2))]
    if comp=="Scissor":
        res="Draw!"
    elif comp=="Stone":
        res="Computer wins!"
    else:
        res="You win!"

    l2.config(text="Scissor")
    l4.config(text=comp)
    l5.config(text=res, fg="black")
    disable()



l1=Label(m, text="Stone Paper Scissor", fg="black", font="Gungsuhche 20 bold")
l1.pack(pady=20)

#FRAME1 for displaying some labels and results
frame1=Frame(m)
frame1.pack()
l2=Label(frame1,text="Player" ,font=10)
l2.pack(side=LEFT)
l3=Label(frame1,text="vs")
l3.pack(side=LEFT)
l4=Label(frame1,text="Computer", font=10)
l4.pack()
l5=Label(m, text="", width=20,font=10, bg="white",relief="solid")
l5.pack(pady=20)

#FRAME2 for buttons of rock paper scissor
frame2= Frame(m)
frame2.pack()
b1= Button(frame2, text="Stone",font=10, width=7,activebackground="grey", command=rock)
b1.pack(side=LEFT)
b2= Button(frame2,text="Paper",font=10,width=7,activebackground="grey",command=paper)
b2.pack(side=LEFT)
b3= Button(frame2, text="Scissor",width=7,font=10,activebackground="grey",command=scissor)
b3.pack()

Button(m,text='RESET GAME', background="black", font=10,fg="yellow",command=reset_game).pack(pady=20)

m.mainloop()