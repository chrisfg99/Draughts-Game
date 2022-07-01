#University of Sussex
#Candidate Number: 184521
from tkinter import *
from draughts.menu import Menu

#the main function that will run the program by calling the main menu
def main():
    root=Tk()
    root.title("Draughts Main Menu")
    root.iconbitmap(r'circle_favicon.ico')
    #set configure window and its columns
    root.columnconfigure(1,minsize=100)
    root.columnconfigure(4,minsize=100)
    root.rowconfigure(10,minsize=100)
    root.configure(bg="white")
    root.resizable(False,False)
    #call the main menu
    Menu(root)
    root.mainloop()

main()
