from tkinter import *
from tkcalendar import Calendar
background="#000000"
framebg="#EDEDED"
framefg="#06283D"


root=Tk()
root.title('ForexOracle')
root.geometry("1000x650")
root.config(bg=background)


f1=Frame(root,width=400,height=200,bg="#151515")
f1.place(x=30,y=100)
f2=Frame(root,width=400,height=200,bg="#151515")
f2.place(x=330,y=100)


#top frames
Label(root,text="FOREXORACLE", width=10,height=2,bg="#F07900",fg='#f5f5f5',font='arial 20 bold').pack(side=TOP,fill=X)
Label(root,text="Email: something@gmail.com", width=10,height=3,bg="#F8A145", anchor='e').pack(side=BOTTOM,fill=X)
Label(f2,text="USD-INR", width=10,height=2,bg='#151515',fg='#f5f5f5',font='arial 16 bold').place(x=50,y=90)
Label(f2,text="Conversion Rate", width=20,height=2,bg='#151515',fg='#f5f5f5',font='arial 20 bold').place(x=20,y=15)
Label(root,text="Conversion", width=20,height=2,bg='#000000',fg='#f5f5f5',font='arial 20 bold').place(x=300,y=395)
Label(root,text="Calculator", width=20,height=1,bg='#000000',fg='#f5f5f5',font='arial 20 bold').place(x=300,y=445)
f3=Frame(root,width=400,height=200,bg="#151515")
f3.place(x=570,y=350)
Label(f3,text="INR", width=10,height=2,bg='#151515',fg='#f5f5f5',font='arial 16 bold').place(x=50,y=8)
Label(f3,text="USD", width=10,height=2,bg='#151515',fg='#f5f5f5',font='arial 16 bold').place(x=50,y=63)
#input box
inp=StringVar()
Entry(f3,textvariable=inp,width=10,bd=2,font="arial 20").place(x=170,y=15)
oup1=StringVar()
Entry(f3,textvariable=oup1,width=10,bd=2,font="arial 20").place(x=170,y=70)
oup2=StringVar()
Entry(f2,textvariable=oup2,width=10,bd=2,font="arial 20").place(x=170,y=100)
cal=Calendar(f1,selectmode='day', year = 2023, month = 3, day = 5)
cal.pack(pady = 20)

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
Button(f1, text = "Get Conversion", command = grad_date).pack(pady=20)
date=Label(f1, text="")
date.pack(pady=20)
def calc():
    oup1.set(int(oup2)*int(inp))
Button(f3, text = "Convert", command = calc).place(x=190,y=150)






root.mainloop()
