from tkinter import*
import random
from datetime import date, datetime

win=Tk()
win.title("TCK_Auto_aim")
win.geometry("700x150")
win.option_add("*Font","궁서 20")
win.configure(background="Aquamarine")

#label
lab=Label(win)
lab.config(text="Amount of Targets",background="Green Yellow")
lab.grid(column=0,row=0,padx=20,pady=20)

#entry
ent=Entry(win)
ent.grid(column=1,row=0,padx=20,pady=20)

#indicate the random buttons
def ran_btn():
    global btn
    btn=Button(win)
    btn.config(background="Blue violet")
    btn.config(comman=click)
    btn.config(text=k)
    x=random.random()
    y=random.random()
    if x >= 0.9:
        btn.place(relx=x-0.1,rely=y)
    elif x <= 0.1:
        btn.place(relx=x+0.1,rely=y)
    elif y >= 0.9:
        btn.place(relx=x,rely=y-0.1)
    elif y <= 0.1:
        btn.place(relx=x+0.1,rely=y+0.1)
    else:
        btn.place(relx=x,rely=y)
    

k=1

def click():
    global k
    if k<num_t:
        k+=1
        btn.destroy()
        ran_btn()
    else:
        end=datetime.now()
        dif=(end-start).total_seconds()
        btn.destroy()
        lab=Label(win)
        lab.config(text="CLEAR " + str(dif) + "seconds",background="Aquamarine")
        lab.pack(pady=230)

def btn_f():
    global num_t
    num_t=int(ent.get()) #strin to int
    for i in win.grid_slaves():#grid 창 전부 list로 저장 [label,entry,button]
         i.destroy() 
    win.geometry("500x500")
    ran_btn()
    global start
    start=datetime.now() #check time
    
#button
btn=Button(win)
btn.config(text="START",background="Cyan")
btn.config(command=btn_f)
btn.grid(column=0,row=1,columnspan=2)

win.mainloop()