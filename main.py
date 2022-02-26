
from tkinter import *
root = Tk()
root.title("ASCII")
root.geometry("400x400")

root.configure(background = "#e6b877")

enter_word = Entry(root)
enter_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_output = Label(root, text="Name in ASCII: ", bg = "#bae677", fg = "black")
encryption_output = Label(root, text="Encyrpted Name: ", bg = "#bae677", fg = "black")

def ASCII_converter():
    input_text = enter_word.get()
    
    for i in input_text:
        label_output["text"] += str(ord(i)) + " "
        ascii = int(ord(i))
        encrypted = ascii - 1
        encryption_output["text"] += str(chr(encrypted)) + " "
        
btn = Button(root, text = "Display in ASCII", command = ASCII_converter, bg = "gold", fg = "black")

btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label_output.place(relx = 0.5, rely = 0.6, anchor = CENTER)        
encryption_output.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()