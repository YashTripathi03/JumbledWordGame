import tkinter #import tkinter module
from tkinter import *
import random #import random module
from tkinter import messagebox

answers = ["python", "java", "swift", "canada", "india", "america",
           "london", "australia", "turbo", "singapore", "linux", "freedom", "dependence", "meaning", "beneath", "minister", "ceremony", "properties", "material", "rectangle", "backbone", "skeleton", "doorway", "girlfriend"]
words = ["nptoyh", "avja", "wfsit", "cdanaa", "aidin", "aiearcm",
         "odnlon", "straaalui", "burot", "gpareonsi", "ixuln", "reofmed", "eecdndepen", "eanmgni", "entbhea", "inemtsri", "erncomye", "rpepirsote", "atamirle", "eclrgaetn", "acnbobek", "keostenl", "ooadyrw", "ilngerdrif"]
num = random.randrange(0, len(words), 1)


def default():  #define the jumbled words to be shown randomly
    global words, answers, num
    lbl.config(text=words[num])


def res():  #pick any random word from the words list created above
    global words, answers, num
    num = random.randrange(0, len(words), 1)
    lbl.config(text=words[num])
    e1.delete(0, END)


def checkans():  #to check answers
    global words, answers, num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("SUCCESS", "This is a Correct answer")
        res()
    else:
        messagebox.showerror("ERROR", "This is not the Correct answer")
        e1.delete(0, END)


root = tkinter.Tk()  #to create the gui
root.geometry("350x400+400+300")
root.title("JUMBBLED WORD GAME")
root.configure(background="black")
lbl = Label(root, text="Your here", font=("arial", 18), bg="black", fg="white")
lbl.pack(pady=30, ipady=10, ipadx=10)
ans1 = StringVar()
e1 = Entry(root, font=("arial", 16), textvariable=ans1)
e1.pack(ipady=5, ipadx=5)
btncheck = Button(root, text="CHECK", font=("arial", 16), width=16,
                  bg="light grey", fg="green", relief=GROOVE, command=checkans)
btncheck.pack(pady=40)
btnreset = Button(root, text="RESET", font=("arial", 16), width=16,
                  bg="light grey", fg="red", relief=GROOVE, command=res)
btnreset.pack()
default()
root.mainloop()
