from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
# default separator style
s=Separator(win)
s.place(relx=0.2,rely=0.5)
# info colored separator style - handle color
s1=Separator(win,bootstyle="success")
s1.place(relx=0.2,rely=0.9)
.
#sizegrip
# default sizegrip style
Sizegrip()
# info colored sizegrip style - handle color
s2=Sizegrip(win,bootstyle="info")
s2.place(relx=0.2,rely=0.7)
win.mainloop()
