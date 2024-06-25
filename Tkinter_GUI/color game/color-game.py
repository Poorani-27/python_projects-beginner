import tkinter as tk
import random

root = tk.Tk()

colours = ["Red", "Yellow", "Orange", "Blue", "Brown", "Purple", "Black"]
timeleft = 30
score = 0

def startgame(event=None):
    if timeleft == 30:
        countdown()
    nextcolor()

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text="Timeleft: " + str(timeleft))
        timelabel.after(1000, countdown)
    else:
        label.config(text="Time's Up")
        e.config(state='disabled')


def nextcolor(event=None):
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tk.END)
        random.shuffle(colours)
        label.config(fg=colours[1], text=colours[0])
        scorelabel.config(text="Score: " + str(score))

def show_entry():
    start_button.pack_forget()
    e.pack(pady=20, padx=15)
    e.focus_set()
    root.bind('<Return>', nextcolor)  # Bind the Return key to the nextcolor function
    startgame()

instructions = tk.Label(root, text="Type in color\nof the words and not the word text!", font=("Helvetica", 12), bg='lightblue')
instructions.pack(pady=20)

scorelabel = tk.Label(root, text="Score: 0", font=("Helvetica", 12), bg='lightblue')
scorelabel.pack(pady=20)

timelabel = tk.Label(root, text="Timeleft: " + str(timeleft), font=("Helvetica", 12), bg='lightblue')
timelabel.pack(pady=20)

label = tk.Label(root, font=("Helvetica", 16), bg='lightblue')
label.pack(pady=20)

e = tk.Entry(root)

start_button = tk.Button(root, text="Start", font=("Helvetica", 16, "bold"), bg='green', fg='white', width=20, height=2, command=show_entry)
start_button.pack(pady=20, padx=15)

root.title("Colour Game")
root.geometry("400x400")
root.configure(bg='lightblue')

root.mainloop()
