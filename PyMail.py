from tkinter import *
from tkinter import ttk
import smtplib


def send():
    global n,p,s,m
    mymail=n.get()
    password=p.get()
    mailto=s.get()
    msg=m.get()
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(mymail,password)
    mailServer.sendmail(mymail,mailto,msg)
    print("Mail Sent")
    mailServer.quit()


    




root=Tk()
root.title("PYMAIL")
root.geometry('900x600+288+88')
root.config(bg='black')

n = Entry(root,bd=5)
n.configure(justify='center')
n.pack()
n.focus_set()
n.place(x=100,y=250,width=300,height=40)

p = Entry(root,show="*",bd=5)
p.configure(justify='center')
p.pack()
p.focus_set()
p.place(x=500,y=250,width=300,height=40)

s= Entry(root,bd=5)
s.configure(justify='center')
s.pack()
s.focus_set()
s.place(x=300,y=350,width=300,height=40)

m= Entry(root,bd=5)
m.configure(justify='center')
m.pack()
m.focus_set()
m.place(x=200,y=440,width=500,height=80)

canvas = Canvas(root, width = 900, height = 180,bg="black")      
canvas.pack()      
img = PhotoImage(file="by _ KRRITHEN.gif")      
canvas.create_image(0,0,anchor=NW, image=img) 

b1 = Button(root,text='  SUBMIT  ',command=send)
b1.place(x=420,y=540)


mainlabel = Label(root,text = "GMAIL ID",font =("new roman",11,"bold"),bg = "black",width = 13,fg ="white",relief = GROOVE,bd = 0)
mainlabel.place(x=190,y=230)

mainlabel = Label(root,text = "PASSWORD",font =("new roman",11,"bold"),bg = "black",width = 13,fg ="white",relief = GROOVE,bd = 0)
mainlabel.place(x=590,y=230)

mainlabel = Label(root,text = "RECEIVER ID",font =("new roman",11,"bold"),bg = "black",width = 13,fg ="white",relief = GROOVE,bd = 0)
mainlabel.place(x=390,y=330)

mainlabel = Label(root,text = "MESSAGE",font =("new roman",11,"bold"),bg = "black",width = 13,fg ="white",relief = GROOVE,bd = 0)
mainlabel.place(x=390,y=420)



root.mainloop()

