#-*-coding:CP949-*-
#from tkinter import *

#window = Tk()

"""
button = Button(window,text="Ŭ��!")
button.pack()
"""

"""
#���� ��ġ
w = Label(window,text="�ڽ� #1",bg="red",fg="white")
w.place(x=0,y=0)
w = Label(window,text="�ڽ� #1",bg="green",fg="black")
w.place(x=20,y=20)
w = Label(window,text="�ڽ� #1",bg="blue",fg="white")
w.place(x=40,y=40)
"""

"""
#���� ��ġ
l1 = Label(window,text="ȭ��")
l2 = Label(window,text="����")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)


e1= Entry(window)
e2= Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1 = Button(window,text="ȭ��->����")
b2 = Button(window,text="����->ȭ��")
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
"""

"""
def callback():
    button["text"] = "Ŭ����!"

button = Button(window,text="Ŭ��",command=callback)
button.pack(side=LEFT)
"""

#window.mainloop()

"""
class App:
    def __init__(self):
        window = Tk()
        helloB = Button(window,text="hello",command=self.hello,fg="red")
        helloB.pack(side=LEFT)
        quitB = Button(window,text="quit",command=self.quit)
        quitB.pack(side=LEFT)
        window.mainloop()
    def hello(self):
        print("Hellow Click!")
    def quit(self):
        print("Quit Click!")
App()
"""

"""
window=Tk()
button=Button(window,text="��ư�� Ŭ���ϼ���")
button.pack()
button["fg"] = "yellow"
button["bg"] = "green"
window.mainloop()
"""

"""
import tkinter as tk
import tkinter.font as font

class App:
    def __init__(self):
        root=tk.Tk()
        self.customFont = font.Font(family="Helvetica",size=12)

        buttonframe = tk.Frame()
        label  = tk.Label(root,text="Hello",font=self.customFont)
        buttonframe.pack()
        label.pack()

        bigger = tk.Button(root,text="��Ʈ�� ũ��",command=self.BigFont)
        smaller = tk.Button(root,text="��Ʈ�� �۰�",command=self.SmallFont)
        bigger.pack()
        smaller.pack()
        root.mainloop()

    def BigFont(self):
        size = self.customFont['size']
        self.customFont.configure(size =size+2)
    def SmallFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size-2)

app = App()
"""

from tkinter import *
window = Tk()
"""
photo = PhotoImage(file="apple.gi f")
w = Label(window,image=photo)
w.photo = photo
w.pack()
"""

Label(window,text="�̸�").grid(row=0)
Label(window,text="����").grid(row=1)


e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

def show():
    print("�̸�:%s\n����:%s"%(e1.get(),e2.get()))

parent = Tk()
Label(parent,text="�̸�").grid(row=0)
Label(parent,text="����").grid(row=1)
e1 = Entry(parent)
e2 = Entry(parent)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

Button(parent,text="���̱�",command=show).grid(row=3,column=1,sticky=W,pady=4)
Button(parent,text="����",command=parent.quit).grid(row=3,column=0,sticky=W,pady=4)

window.mainloop()
parent.mainloop()