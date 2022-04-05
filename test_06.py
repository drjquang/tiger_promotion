# Date: 05/04/2022
# This will create an array of buttons
# -----------------------------------------------------
# Modify test_04, create a dictionary of buttons

import tkinter as tk
from tkinter import *
from tkinter.ttk import *

# Variable declaration
DIGITS_FONT_STYLE = ("Arial", 25, "bold")

LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F5F5F5"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("560x420")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.window.configure(bg=LIGHT_GRAY)

        self.photo = PhotoImage(file=r"assets\image_01.png")
        # Create the properties for an array of buttons
        self.button_dict = {}
        self.digits = {
            1: (1, 1), 2: (1, 2), 3: (1, 3), 4: (1, 4),
            5: (2, 1), 6: (2, 2), 7: (2, 3), 8: (2, 4),
            9: (3, 1), 10: (3, 2), 11: (3, 3), 12: (3, 4),
            13: (4, 1), 14: (4, 2), 15: (4, 3), 16: (4, 4)
        }
        # Create button frame
        self.buttons_frame = self.create_buttons_frame()
        # Create buttons
        self.create_digit_buttons()

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        print(value)
        # Need to determine which button was clicked
        self.button_dict[value].focus_set()
        self.button_dict[value]["text"] = "  "
        # self.button_dict[value]["state"] = "disabled"
        self.button_dict[value]["image"] = self.photo

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            self.button_dict[digit] = tk.Button(self.buttons_frame, text=str(digit).zfill(2),
                                                bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                                                borderwidth=0,
                                                command=lambda x=digit: self.add_to_expression(x))
            self.button_dict[digit].grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
