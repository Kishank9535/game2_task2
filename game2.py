from tkinter import *
root=Tk()
root.geometry("500x500")

frame=Frame(root)
frame.pack()
space=Label(frame,text="Tic-Tac-Toe",font=("Arial",30))
space.grid(row=0,column=0)
frame1=Frame(root)
frame1.pack()

b={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
ch="X"

def win(player):
   if b[1]==b[2] and b[2]==b[3] and b[3]==player:
      return True
   elif b[4]==b[5] and b[5]==b[6] and b[6]==player:
      return True
   elif b[7]==b[8] and b[8]==b[9] and b[9]==player:
      return True
   elif b[1]==b[4] and b[4]==b[7] and b[7]==player:
      return True
   elif b[2]==b[5] and b[5]==b[8] and b[8]==player:
      return True
   elif b[3]==b[6] and b[6]==b[9] and b[9]==player:
      return True
   elif b[1]==b[5] and b[5]==b[9] and b[9]==player:
      return True
   elif b[3]==b[5] and b[5]==b[7] and b[7]==player:
      return True
   return False

def draw():
   for i in b.keys():
      if b[i] =="":
         return False
   return True  

def restart():
   for i in buttons:
      i["text"]=" "
   for j in b.keys():
      b[j]=""
   space=Label(frame,text="Tic-Tac-Toe",font=("Arial",30),width=15)
   space.grid(row=0,column=0)                 


def play(event):
    global ch
    button=event.widget
    buttont=str(button)
    click=buttont[-1]
    if click=="n":
       click=1
    else:
       click=int(click)   
    if button["text"]==" ":
     if ch=="X":
       button["text"]="X"
       b[click]=ch
       if win(ch):
         winning=Label(frame,text=f"{ch} Wins the game",font=("Arial",25))
         winning.grid(row=0,column=0,columnspan=3)
       ch="O"
     else:
         button["text"]="O"
         b[click]=ch
         if win(ch):
          winning=Label(frame,text=f"{ch} Wins the game",font=("Arial",25))
          winning.grid(row=0,column=0,columnspan=3)
         ch="X" 
    if draw() :
          draw1=Label(frame,text=f"Game Draw",font=("Arial",25),width=13)
          draw1.grid(row=0,column=0,columnspan=3) 
     

btn1=Button(frame1,text=" ",width=4,height=2,font=("Arial",22),relief=RAISED,borderwidth=4)
btn1.grid(row=0,column=0)
btn1.bind("<Button-1>",play)

btn2=Button(frame1,text=" ",width=4,height=2,font=("Arial",22),relief=RAISED,borderwidth=4)
btn2.grid(row=0,column=1)
btn2.bind("<Button-1>",play)

btn3=Button(frame1,text=" ",width=4,height=2,font=("Arial",22),relief=RAISED,borderwidth=4)
btn3.grid(row=0,column=2)
btn3.bind("<Button-1>",play)


btn4=Button(frame1,text=" ",width=4,height=2,font=("Arial",22),relief=RAISED,borderwidth=4)
btn4.grid(row=1,column=0)
btn4.bind("<Button-1>",play)

btn5=Button(frame1,text=" ",width=4,height=2,font=("Arial",22),relief=RAISED,borderwidth=4)
btn5.grid(row=1,column=1)
btn5.bind("<Button-1>",play)

btn6=Button(frame1,text=" ",width=4,height=2,font=("Arial",22),relief=RAISED,borderwidth=4)
btn6.grid(row=1,column=2)
btn6.bind("<Button-1>",play)


btn7=Button(frame1,text=" ",width=4,height=2,font=("Arial",22),relief=RAISED,borderwidth=4)
btn7.grid(row=2,column=0)
btn7.bind("<Button-1>",play)

btn8=Button(frame1,text=" ",width=4,height=2,font=("Arial",22),relief=RAISED,borderwidth=4)
btn8.grid(row=2,column=1)
btn8.bind("<Button-1>",play)

btn9=Button(frame1,text=" ",width=4,height=2,font=("Arial",22),relief=RAISED,borderwidth=4)
btn9.grid(row=2,column=2)
btn9.bind("<Button-1>",play)

restartbtn=Button(frame1,text="Rest Game",width=10,height=1,font=("Arial",25),relief=RAISED,borderwidth=3,command=restart)
restartbtn.grid(row=4,column=0,columnspan=3)

buttons=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
root.mainloop()