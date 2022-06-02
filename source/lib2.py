#-*-coding:CP949-*-
#from tkinter import *

#window = Tk()

"""
choice = IntVar()

Label(window,text="가장 선호하는 프로그래밍 언어를 선택하시오",justify=LEFT,padx=20).pack()
Radiobutton(window,text="Python",padx=20,variable=choice,value=1).pack(anchor=W)
Radiobutton(window,text="C",padx=20,variable=choice,value=2).pack(anchor=W)
Radiobutton(window,text="Swift",padx=20,variable=choice,value=3).pack(anchor=W)
Radiobutton(window,text="Java",padx=20,variable=choice,value=4).pack(anchor=W)

window.mainloop()
"""

"""
Label(window,text="가장 선호하는 프로그래밍 언어를 선택하시오",justify=LEFT,padx=20).pack()

value1= IntVar()
Checkbutton(window,text="Python",variable=value1).grid(row=1,sticky=W)
value2= IntVar()
Checkbutton(window,text="C",variable=value2).grid(row=2,sticky=W)
value3= IntVar()
Checkbutton(window,text="Java",variable=value3).grid(row=3,sticky=W)
value4= IntVar()
Checkbutton(window,text="Swift",variable=value4).grid(row=4,sticky=W)

window.mainloop()
"""

#from PIL import Image, ImageFilter, ImageTk
#import tkinter as tk

"""
window = tk.Tk()
canvas = tk.Canvas(window,width=500,height=500)
canvas.pack()

img = Image.open("source\lenna.png")
tk_img = ImageTk.PhotoImage(img)

out = img.rotate(45)
tk_img2 = ImageTk.PhotoImage(out)
ImageFilter
blur = img.filter(ImageFilter.BLUR)
tk_img3 = ImageTk.PhotoImage(blur)


#canvas.create_image(250,250,image=tk_img)
#canvas.create_image(250,250,image=tk_img2)
canvas.create_image(250,250,image=tk_img3)

window.mainloop()
"""

"""
def open():
    pass

def quit():
    window.quit()

window = tk.Tk()
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)

filemenu.add_command(label="열기",command=open)
filemenu.add_command(label="종료",command=quit)

menubar.add_cascade(label="파일",menu=filemenu)

window.config(menu=menubar)
window.mainloop()
"""

from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import Canvas, filedialog as fd

im = None
tk_img = None

def open():
    global im,tk_img
    fname = fd.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250,250,image=tk_img)
    window.update()

def quit():
    window.quit()\

def image_rotate():
    global im,tk_img
    out=im.rotate(45)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250,250,image=tk_img)
    window.update()

def image_blur():
    global im, tk_img
    out = im.filter(ImageFilter.BLUR)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250,250,image=tk_img)
    window.update()

window = tk.Tk()
canvas = tk.Canvas(window,width=500,height=500)
canvas.pack()

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)
filemenu.add_command(label="열기",command=open)
filemenu.add_command(label="닫기",command=quit)
ipmenu.add_command(label="영상 회전",command=image_rotate)
ipmenu.add_command(label="영상흐리게",command=image_blur)
menubar.add_cascade(label="파일",menu=filemenu)
menubar.add_cascade(label="영상처리",menu=ipmenu)

window.config(menu=menubar)
window.mainloop()

