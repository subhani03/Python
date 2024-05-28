from tkinter import *
from tkinter import ttk,font
   
from PIL import ImageTk,Image
import requests

def train2(a,win):
    win.destroy()
    win=Tk()
    win.geometry("400x400")
    base_url="https://rappid.in/apis/train.php?train_no={}".format(a)
    response=requests.get(base_url)
    train_status=response.json()

    Label(win,text="*****************************************************************").pack()
    Label(win,text="Train Name: "+train_status["train_name"]).pack()
    Label(win,text="*****************************************************************").pack()
    for x in train_status['data']:
        if x["is_current_station"]:
            Label(win,text="station \t\t: "+x["station_name"]).pack()
            Label(win,text="Distance from the starting \t: "+x["distance"]).pack()
            Label(win,text="Timing \t\t\t\t: "+x["Timing"]).pack()
            Label(win,text="Delay \t\t\t\t: "+x["Delay"]).pack()
            Label(win,text="Platform No \t\t\t\t: "+x["Platform No"]).pack()
            Label(win,text="Halt \t\t\t\t: "+x["Halt"]).pack()
        else:
            Label(win,text=x['station_name']).pack()
    Label(win,text="*****************************************************************").pack()
    Label(win,text="Msg: "+train_status["message"]).pack()
    Label(win,text="Msg upd: "+train_status["updated_time"]).pack()
    Label(win,text="*****************************************************************").pack()
    win.mainloop()


def home():
    win=Tk()
    win.geometry("500x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    f=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="TRAIN STATUS",font=label_font,bg="blue",fg="white")
    f.place(relx=0.15,rely=0)
    f.pack()
    f1=Frame(win,width=1000,height=50)
    f1.pack()
    f1.place(relx=0.28,rely=0.2)
    img=ImageTk.PhotoImage(Image.open("trainpic2.jpg"))
    l=Label(f1,image=img)
    l.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l=Label(win,text="Train No",bg="pink",font=label_font)
    l.place(relx=0.40,rely=0.80)
    e1=Entry(win)
    e1.place(relx=0.52,rely=0.80,width=154,height=35)
    l1=Button(win,text="OK",bg="green",font=label_font,command=lambda:train2(e1.get(),win))
    l1.place(relx=0.52,rely=0.90)
    win.mainloop()

home()










