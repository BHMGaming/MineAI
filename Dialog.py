import sys, json, zipfile, audioop, hashlib, wave, io

gui = True
import tkinter
from tkinter import filedialog, messagebox

def pickProject():
    try:
        root = tkinter.Tk()
        root.withdraw()
        pypath = filedialog.askopenfilename(title="Open MineAI Project", filetypes=[("Python Files", "*.py")])
    except:
        pypath = sys.argv[-1]
    return (pypath)

def error(message, gui):
    root = tkinter.Tk()
    root.withdraw()
    if gui:
        message = message + '\n\nSorry about that.'
        messagebox.showerror('Error', message, icon='warning')
    else:
        lines = message.split('\n')
        lines = ["       " + line for line in lines]
        lines[0] = "Error: " + lines[0][7:]
        print('\n'.join(lines))
        input('Press enter to exit... ')
    exit()

def success(warnings):
    if warnings == 0:
        messagebox.showinfo("Success", "Completed with no warnings")
    elif warnings == 1:
        messagebox.showinfo("Success", "Completed with {} warning".format(warnings))
    else:
        messagebox.showinfo("Success", "Completed with {} warnings".format(warnings))

def confirm(pypath):
    confirm = messagebox.askquestion('Confirm Upload',"Are you sure you want to run '{}' in MineAI?".format(pypath), icon='warning')
    while confirm == 'no':
        pypath = pickProject()
        confirm = messagebox.askquestion('Confirm Upload',"Are you sure you want to run '{}' in MineAI?".format(pypath), icon='warning')
    
pypath = pickProject()
confirm(pypath)



















##while True:
##    if __name__ == '__main__':
##        input()
##        if '-h' in sys.argv:
##            print(
##                '''
##        Arguments: sb3tosb2.py [unordered options] sb3path sb2path
##        List of Options:
##        -h: Show this list
##        -c: Enable Scratch 3.0 compatibility mode; Add workarounds for blocks that are exclusive to or work differently in 3.0
##          The indented options will automatically enable compatibility mode:
##          -j: Use an unlimited join workaround
##          -l: Use custom blocks to automatically limit list length to 200,000
##        -p: Tries to insert blocks to fill the screen when the pen size is set to a value greater than 255''')
##
### Tkinter Open File
##root = Tk()
##root.withdraw()
##root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Mine AI files","*.ma"),("all files","*.*")))
##print(root.filename)
##sb3path = root.filename
##
### Tkinter Save File
##root = Tk()
##root.withdraw()
##root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Save file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
##print(root.filename)
##
### Tkinter Open Directory
##root = Tk()
##root.withdraw()
##root.directory = filedialog.askdirectory()
##print(root.directory)
##
##retry = messagebox.askquestion('Enable Compatibility Mode',"The converted project may not work properly unless compatibility mode is enabled.\n\nWould you like to re-convert the sb3 file with compatibility mode enabled?".format(sb3path), icon='warning')
##retry = (retry == 'yes')
