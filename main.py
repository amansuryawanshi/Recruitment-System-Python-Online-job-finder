import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def click_login():
    call(["python", "login.py"])
def click_regis():
    call(["python", "regis.py"])
def click_find():
    call(["python","projectpython.py"])
    
class Online_Employee_Recruitment_System:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'  
        _compcolor = '#ffffff' 
        _ana1color = '#ffffff' 
        _ana2color = '#ffffff'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("963x749+540+110")
        root.title("Employee Recruitment System")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")





        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message6.configure(background="#d9d9d9")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''WELCOME''')
        self.Message6.configure(width=791)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.18, rely=0.17, height=103, width=566)
        self.Button2.configure(activebackground="#ff6600")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''1.Login''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_login)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.18, rely=0.33, height=93, width=566)
        self.Button3.configure(activebackground="#ff6600")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(text='''2.Register Yourself''')
        self.Button3.configure(command=click_regis)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.18, rely=0.48, height=90, width=566)
        self.Button4.configure(activebackground="#ff6600")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(text='''3.Apply for Job''')
        self.Button4.configure(command=click_find)
if __name__ == '__main__':
    GUUEST=Online_Employee_Recruitment_System()        
