from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext


screen = Tk()
screen.title("|(:--Orange by Arvind--:)|")
textpad = scrolledtext.ScrolledText(screen, width=100, height=80)


# Creating a menu & define function for each menu item

def open_command():
    file = filedialog.askopenfile(parent=screen,title='Select a File')
    if file != None:
        contents = file.read()
        #1.0 indexing h an contents uske characters
        textpad.insert(1.0, contents)
        file.close()

def save_command():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        #both are index
        data = textpad.get(1.0,END)
        file.write(data)
        file.close()


def new_command():
    screen.title("New untitled file")
    textpad.delete(1.0,END)


def exit_command():
    if messagebox.askokcancel('Quit','Do you really want to quit'):
        screen.destroy()


def about_command():
    label = messagebox.showinfo('About','''This Text Editor (Orange) is created by Arvind Pathak
on 23-11-2020(18:30) this is a simple text editor created in python using tkinter ''')

def about_money():
    label = messagebox.askyesno('Purchase pro version(Orange pro+)','''This Text Editor (orange) by Arvind
can be bought for 99$/month only. Do you want to procced further:''')
    if label==False:
        messagebox.showwarning("sale for you","You can get an extra 50% discount, just rethink again")

def code():
    error=messagebox.showerror("Unauthorised Access",'''only people related to
orange corporation are allowed ''')

def bg():
    bginput=input("write a color")
    textpad.configure(bg=bginput)

def font():
    fontinput=input("write a font")
    textpad.configure(font=fontinput)

def textcolour():
    fginput=input("write a color")
    textpad.configure(fg=fginput)


menu = Menu(screen)
screen.config(menu=menu)
filemenu = Menu(menu)
editmenu=Menu(menu)
helpmenu = Menu(menu)


#menu is for windows and filemenu is inside menu 
menu.add_cascade(label='Files',menu=filemenu)
menu.add_cascade(label='Edit',menu=editmenu)
menu.add_cascade(label='Design')
menu.add_cascade(label='Mailings')
menu.add_cascade(label='Review')
menu.add_cascade(label='View')
#menu is inside for help this time
menu.add_cascade(label='Help',menu=helpmenu)
menu.add_cascade(label='code',command=code)


filemenu.add_command(label='New',command=new_command)
filemenu.add_command(label='Open..',command=open_command)
filemenu.add_command(label='Save',command=save_command)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=exit_command)


editmenu.add_command(label='Textcolour',command=textcolour)
editmenu.add_command(label='Font',command=font)
editmenu.add_command(label='Background',command=bg)


helpmenu.add_command(label='Premium features',command=about_money)
helpmenu.add_command(label='About..', command=about_command)

chk=Checkbutton(screen,text='Click it if you want to change the coding of this program',command=code)
chk.pack(side=BOTTOM , anchor=SW)

textpad.pack()

screen.mainloop()

