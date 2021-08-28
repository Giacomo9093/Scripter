# | From G9 | Scripter9093 | >>> by Giacomo9093 <<< | v1.0 | Python3 | For Linux/Ubuntu | © |
#IMPORT
import tkinter as tk 
import time 
import getpass 
import os
from tkinter import font
import zenity
import zenipy

#IMPORT FROM...
from tkinter.ttk import *
from typing import Optional, Sized, Text, TextIO
from io import DEFAULT_BUFFER_SIZE, TextIOWrapper
from tkinter.font import BOLD, ITALIC
from tkinter.constants import BOTTOM, LAST, TOP, TRUE, W
from tkinter.messagebox import *
from tkinter import StringVar, Toplevel, messagebox
from zenity import cli, file_selection, show
from zenipy import *
from zenipy.zenipy import message
from ast import Str

#PRE...
username = getpass.getuser()

opzions = [
    "False - Run whitout the terminal",
    "True - Run with the terminal"
]

#VARIABLES

#DEF 
def selected(event):
    print("DA DEFINIRE") #Terminal only / Dev Only

def change_txt(self):
    print("")

def exec_path():
    exec_path_to = zenipy.file_selection()
    # | global sp1                               |
    # | sp1.config(text=exec_path_to, fg="gray") |
    tb1.delete(0, "end")
    tb1.insert(0, exec_path_to)
    showinfo(title="Desktop Scripter", message="You have selected "+exec_path_to)

def icon_path():
    icon_path_to = icon_path_to = zenipy.file_selection()
    # | global sp2                               |
    # | sp2.config(text=icon_path_to, fg="gray") |
    tb2.delete(0, "end")
    tb2.insert(0, icon_path_to)
    showinfo(title="Desktop Scripter", message="You have selected "+icon_path_to)

def create_ds():
    showinfo(title="Desktop Scripter", message="The Desktop icon will be created in your Home folder")
    g1.quit()
    g1.destroy()

#TKINTER > SETUP > GUI
g1 = tk.Tk()
g1.geometry("")
g1.geometry("600x780")
g1.resizable(False, False)
g1.title("Desktop Scripter")

exec_path_to = StringVar()
icon_path_to = StringVar()
name_exec = StringVar()
comment_exec = StringVar()
version_exec = StringVar()
deskname = StringVar()

#TKINTER > SETUP > BUTTON / ENTRY / TEXT
tk.Label(g1, text="· · · · · Enter the location of the executable · · · · ·", fg="red2", font=BOLD).pack() 
tk.Label(g1, text="Generally it is: /home/username/path-to-the-executable/executable-name", fg="black").pack()
tb1 = tk.Entry(g1, width=50, fg="black", font=ITALIC, textvariable=exec_path_to) # | ENTRY |
tb1.pack() # | PACK ENTRY |
but1 = tk.Button(g1, width=48, fg="black", text="Browse to files", font=BOLD, command=exec_path).pack()
sp1 = tk.Label(g1, text="  ")
sp1.pack()

tk.Label(g1, text="· · · · · · · Enter the location of the Icon · · · · · · ·", fg="red2", font=BOLD).pack()
tk.Label(g1, text="Generally it is: /home/username/path-to-the-icon/icon-name", fg="black").pack()
tb2 = tk.Entry(g1, width=50, fg="black", font=ITALIC, textvariable=icon_path_to) # | ENTRY |
tb2.pack() # | PACK ENTRY |
tk.Button(g1, width=48, fg="black", text="Browse to files", font=BOLD, command=icon_path).pack()
sp2 =tk.Label(g1, text="  ")
sp2.pack()

tk.Label(g1, text="· · · · · · · · · · · · · · · Terminal · · · · · · · · · · · · · · ·", fg="red2", font=BOLD).pack()
tk.Label(g1, text="True - if you want the executable to run from the terminal", fg="black").pack()
tk.Label(g1, text="False - if you want the executable to run without using the terminal", fg="black").pack()
clicked = tk.StringVar()
clicked.set(opzions[0])
drop_menu_f_t = tk.OptionMenu(g1, clicked, *opzions).pack()
sp3 = tk.Label(g1, text="  ")
sp3.pack()

tk.Label(g1, text="· · · · · · · · · · · · · · · · Name · · · · · · · · · · · · · · · ·", fg="red2", font=BOLD).pack()
tk.Label(g1, text="The Program / Executable Name: will appear under the icon ...", fg="black").pack()
tb3 = tk.Entry(g1, width=50, fg="black", font=ITALIC, textvariable=name_exec) # | ENTRY |
tb3.pack() # | PACK ENTRY | 
sp4 = tk.Label(g1, text="  ")
sp4.pack()

tk.Label(g1, text="· · · · · · · · · · · · · · · Comment · · · · · · · · · · · · · · ·", fg="red2", font=BOLD).pack()
tk.Label(g1, text="Comment freely on the Program / Executable - [NOT VISIBLE FROM DESKTOP]", fg="black").pack()
tb4 = tk.Entry(g1, width=50, font=ITALIC,textvariable=comment_exec) # | ENTRY |
tb4.pack() # | PACK ENTRY | 
sp5 =tk.Label(g1, text="  ")
sp5.pack()

tk.Label(g1, text="· · · · · · · · · · · · · · · Version · · · · · · · · · · · · · · ·", fg="red2", font=BOLD).pack()
tk.Label(g1, text="Enter the version of the executable / program - [NOT VISIBLE FROM THE DESKTOP]", fg="black").pack()
tb5 = tk.Entry(g1, width=50, font=ITALIC,textvariable=version_exec) # | ENTRY |
tb5.pack() # | PACK ENTRY |
sp6 =tk.Label(g1, text="  ")
sp6.pack()

tk.Label(g1, text="· · · · · · · · · · · File.desktop Name · · · · · · · · · · ·", fg="red2", font=BOLD).pack()
tk.Label(g1, text="Enter the name of your file.desktop", fg="black").pack()
tb6 = tk.Entry(g1, width=50, font=ITALIC, textvariable=deskname)
tb6.pack()
sp7 =tk.Label(g1, text="  ")
sp7.pack()

tk.Button(g1, width=48, fg="green", text="Make your Desktop-Shortcut", font=BOLD, command=create_ds).pack()

#MAINLOOP
if __name__ == "__main__":
    g1.mainloop()

#VARIABLE TRANSLATION
exec_pather = exec_path_to.get()
icon_pather = icon_path_to.get()
version_exe = version_exec.get()
comment_exe = comment_exec.get()
name_exe = name_exec.get()
desk_name = deskname.get()

#EDIT DESKTOP FILE 
script_desktop = open("/home/"+username+"/"+desk_name+".desktop", "w")
script_desktop.write("#by Giacomo9093 > Scripter > Desktop Scripter...\n")
script_desktop.write("[Desktop Entry]\n")
script_desktop.write("Version="+version_exe+"\n")
script_desktop.write("Name="+name_exe+"\n")
script_desktop.write("Comment="+comment_exe+"\n")
script_desktop.write("Exec="+exec_pather+"\n")
script_desktop.write("Icon="+icon_pather+"\n")
script_desktop.write("Type=Application"+"\n")
selected_output = clicked.get()
if selected_output == opzions[0]:
    script_desktop.write("Terminal=false")
if selected_output == opzions[1]:
    script_desktop.write("Terminal=true")
script_desktop.close()
exit()