from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")

# default scrollbar style
Scrollbar()

# success colored default scrollbar style
s=Scrollbar(win,text="subi",bootstyle="success")
s.place(relx=0.2,rely=0.5)
#round
# default round scrollbar style
s1=Scrollbar(win,text="hello",bootstyle="round")
s1.place(relx=0.2,rely=0.6)
# danger colored round scrollbar style
s2=Scrollbar(win,text="success",bootstyle="danger-round")
s2.place(relx=0.2,rely=0.7)
win.mainloop()