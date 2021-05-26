from tkinter import *
import tkinter.messagebox as tmsg
import tkinter.filedialog as tfile
import os
root = Tk()
root.title("Untitled - Notepad")
root.geometry("850x1400")
menu_bar = Menu(root)

#Functions
def New():
	global file
	root.title("Untitled - Notepad")
	file = None
	text_area.delete(1.0, END)

def Open():
	global file
	file = tfile.askopenfilename(defaultextension=".txt" , filetypes=[("All files" , "*.*"), ("Text documents" , "*.txt")])
	if file == "":
		file = None
	else:
		root.title(os.path.basename(file) + " - Notepad")
		text_area.delete(1.0, END)
		f = open(file, "r")
		text_area.insert(1.0 , f.read())

def Save():
	global file
	if file==None:
		file = tfile.asksaveasfilename(defaultextension=".txt" , filetypes=[("All files" , "*.*"), ("Text documents" , "*.txt")])
		if file=="":
			file=None
		else:
			f = open(file, "w")
			f.write(text_area.get(1.0, END))
			f.close()
			root.title(os.path.basename(file) + " - Notepad")
		
	else:
		f= open(file, "w")
		f.write(text_area.get(1.0, ENd))
		f.close()

def cut():
	text_area.event_generate("<<Cut>>")

def copy():
	text_area.event_generate("<<Copy>>")

def paste():
	text_area.event_generate("<<Paste>>")

def about():
	tmsg.showinfo("Notepad" , "Notepad created by Ayush")


#File Menu
file_menu = Menu(menu_bar , tearoff=0)
file_menu.add_command(label="New" , command=New)
file_menu.add_command(label="Open" , command=Open)
file_menu.add_command(label="Save" , command=Save)
file_menu.add_separator()
file_menu.add_command(label="Exit" , command=quit)
menu_bar.add_cascade(label="File" , menu=file_menu)

#Edit Menu
edit_menu = Menu(menu_bar , tearoff=0)
edit_menu.add_command(label="Cut" , command=cut)
edit_menu.add_command(label="Copy" , command=copy)
edit_menu.add_command(label="Paste" , command=paste)
menu_bar.add_cascade(label="Edit" , menu=edit_menu)

#Help Menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About Notepad", command=about)
menu_bar.add_cascade(label="Help" , menu=help_menu)

root.config(menu=menu_bar)



#TextArea
text_area= Text(root , font="lucida 12")
file = None
text_area.pack(expand=True,fill=BOTH)

#ScrollBar
scrollbar = Scrollbar(text_area)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)



root.mainloop()