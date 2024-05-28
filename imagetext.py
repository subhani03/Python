from tkinter import *
from tkinter import font,ttk,messagebox
from PIL import ImageTk,Image
class A:
    def __init__(self,root1):
        self.root=root1
        self.root.title("Transparent label image") 
        self.root.geometry("1500x1500")
        
        self.bg=ImageTk.PhotoImage(Image.open("homeimage.jpg"))

        canvas=Canvas(self.root)
        canvas.create_image(600,500,image=self.bg)
        label_font=font.Font(weight="bold",family="Times New Roman",size=20)
        canvas.create_text(700,80,text="welcome to Livewire",fill="white",font=label_font)
        label_font=font.Font(weight="bold",family="Times New Roman",size=15)
        t="""Live Carriers on-demand courses in emerging technologies
        give you the knowledge you need to stay ahead of the 
        curve and succeed in today's fast-paced world."""
        canvas.create_text(800,600,text=t,fill="white",font=label_font)
        canvas.pack(fill="both",expand=True)
root=Tk()
obj=A(root)
root.mainloop()