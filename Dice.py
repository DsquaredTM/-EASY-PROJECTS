import random
import tkinter as tk
from tkinter import  messagebox
def display_dice():
    roll = random.randint(1,6)
    messagebox.showinfo("Dice Roll", f" '{roll}' is your number.")
    return roll

if __name__ == "__main__":
    random.randint(1,6)
    root = tk.Tk()
    root.title("Random Dice")
    root.geometry("300x300")

    main_dice = tk.Frame(root)
    main_dice.grid(pady=120, padx=120)

    btn_roll_dice = tk.Button(main_dice, text="Roll Dice", command=display_dice)
    btn_roll_dice.grid(pady=10)

    root.mainloop()
