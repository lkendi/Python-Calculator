"""
Calculator Module
"""
import tkinter as tk

# colors used in the calculator
DARK_GREY = '#333333'
LIGHT_GREY = '#595959'
WHITE = '#FCFCFC'
YELLOW = '#F2C94C'

# font
DIGITS_FONT = ("Roboto", 24)
RESULT_FONT = ("Roboto", 36, "bold")


class Calculator():
    """Calculator class"""

    def __init__(self):
        """Initializes a new calculator object"""
        # Calculator window
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("250x560")
        self.window.resizable(False, False)
        self.window.configure(background=DARK_GREY)

        # Frames
        self.display_frame = tk.Frame(
            self.window,
            bg=LIGHT_GREY
        )
        self.display_frame.pack(fill="both", expand=True)
        self.buttons_frame = tk.Frame(
            self.window,
            bg=DARK_GREY
        )
        self.buttons_frame.pack(fill="x")

        # buttons
        self.calc_buttons = {
            'C': (0, 0), '%': (0, 1), '.': (0, 2), '\u00F7': (0, 3),
            7: (1, 0),   8: (1, 1),   9: (1, 2),   '\u00D7': (1, 3),
            4: (2, 0),   5: (2, 1),   6: (2, 2),   '-': (2, 3),
            1: (3, 0),   2: (3, 1),   3: (3, 2),   '+': (3, 3),
            '(': (4, 0),  0: (4, 1), ')': (4, 2),   '=': (4, 3)
        }
        for symbol, grid_position in self.calc_buttons.items():
            button = tk.Button(
                self.buttons_frame,
                text=symbol,
                bg=DARK_GREY,
                fg=WHITE,
                padx=10,
                pady=10,
                font=DIGITS_FONT,
                borderwidth=0,
                command=lambda x=symbol: self.button_pressed(x))
            button.grid(row=grid_position[0],
                        column=grid_position[1])

        # text and labels
        self.expression_text = ""
        self.result_text = ""
        self.expression_label = tk.Label(self.display_frame,
                                         text=self.expression_text,
                                         fg=YELLOW,
                                         bg=LIGHT_GREY,
                                         font=DIGITS_FONT,
                                         anchor=tk.NE)
        self.expression_label.pack(expand=True, fill="both")
        self.result_label = tk.Label(self.display_frame,
                                     text=self.result_text,
                                     fg=YELLOW,
                                     bg=LIGHT_GREY,
                                     font=RESULT_FONT,
                                     anchor=tk.E)
        self.result_label.pack(expand=True, fill="both")

    def button_pressed(self, symbol):
        """Function that handles pressing of the different buttons"""
        if symbol in ['=']:
            self.expression_label.config(text=self.expression_text)
            self.result_label.config(text="")
            self.evaluate_expression()
        elif symbol in ['C']:
            self.expression_text = ""
            self.expression_label.config(text="")
            self.result_text = ""
            self.result_label.config(text="")
        else:
            self.expression_text += str(symbol)
            self.result_label.config(text=self.expression_text)
        print(self.expression_text)

    def evaluate_expression(self):
        """Evaluates the expression and updates the result"""
        try:
            expression = self.expression_text.replace(
                        '\u00F7', '/').replace('\u00D7', '*')
            result = eval(expression)
            if isinstance(result, float):
                result = round(result, 3)
            self.result_text = result
            self.result_label.config(text=self.result_text)
        except ZeroDivisionError:
            self.expression_label.config(text="Arithmetic Error")
            self.expression_text = ""
            self.result_text = ""
        except SyntaxError:
            self.expression_label.config(text="Syntax Error")
            self.expression_text = ""
            self.result_text = ""

    def start_calc(self):
        """Starts the calculator"""
        self.window.mainloop()


if __name__ == "__main__":
    """Entry point"""
    my_calc = Calculator()
    my_calc.start_calc()
