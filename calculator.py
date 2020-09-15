from __future__ import division
import tkinter as Tk


class Calculator:
    ''' main class that constructs the calc and preforms the calculations '''

    def __init__(self, master):
        # Global variables needed throughout a single calculation
        self.top_string = ''    # string for label at top of calculator
        self.number1 = 0       # storage of first number selected
        self.number2 = 0       # storage of second number selected
        self.add = False       # + boolean
        self.subtract = False  # - boolean
        self.multiply = False  # x boolean
        self.divide = False  # / boolean

        # Top Label Layout
        self.label = Tk.Label(master, text='0', bg='black', fg='white', height=2, width=4)
        self.label.grid(row=0, column=0, columnspan=4, sticky=Tk.N+Tk.E+Tk.S+Tk.W)
        self.label.config(font='Verdana 16 bold')

        # Button Layout
        Tk.Button(master, text='1', height=2, width=6, command=lambda: self.number_pressed(1)).grid(row=1, column=0)
        Tk.Button(master, text='2', height=2, width=6, command=lambda: self.number_pressed(2)).grid(row=1, column=1)
        Tk.Button(master, text='3', height=2, width=6, command=lambda: self.number_pressed(3)).grid(row=1, column=2)
        Tk.Button(master, text='4', height=2, width=6, command=lambda: self.number_pressed(4)).grid(row=2, column=0)
        Tk.Button(master, text='5', height=2, width=6, command=lambda: self.number_pressed(5)).grid(row=2, column=1)
        Tk.Button(master, text='6', height=2, width=6, command=lambda: self.number_pressed(6)).grid(row=2, column=2)
        Tk.Button(master, text='7', height=2, width=6, command=lambda: self.number_pressed(7)).grid(row=3, column=0)
        Tk.Button(master, text='8', height=2, width=6, command=lambda: self.number_pressed(8)).grid(row=3, column=1)
        Tk.Button(master, text='9', height=2, width=6, command=lambda: self.number_pressed(9)).grid(row=3, column=2)
        Tk.Button(master, text='0', command=lambda: self.number_pressed(0)).grid(row=4, columnspan=2, sticky=Tk.N+Tk.E+Tk.S+Tk.W)
        Tk.Button(master, text='+', height=2, width=6, command=lambda: self.sign_pressed("+")).grid(row=1, column=3)
        Tk.Button(master, text='-', height=2, width=6, command=lambda: self.sign_pressed("-")).grid(row=2, column=3)
        Tk.Button(master, text='x', height=2, width=6, command=lambda: self.sign_pressed("*")).grid(row=3, column=3)
        Tk.Button(master, text='/', height=2, width=6, command=lambda: self.sign_pressed("/")).grid(row=4, column=3)
        Tk.Button(master, text='C', height=2, width=6, command=self.clear_all).grid(row=4, column=2)
        Tk.Button(master, text='=', height=2, command=self.equals).grid(row=5, columnspan=4, sticky=Tk.N+Tk.E+Tk.S+Tk.W)

    def number_pressed(self, button_number):
        ''' This function is triggered when buttons 0 - 9 are pushed '''
        if self.number1 is 0 and not any([self.add, self.subtract, self.multiply, self.divide]):
            self.number1 = button_number
            self.top_string = str(button_number)
            self.label.config(text=str(button_number))

        elif self.number1 is not 0 and not any([self.add, self.subtract, self.multiply, self.divide]):
            self.top_string += str(button_number)
            self.number1 = int(self.top_string)
            self.label.config(text=self.top_string)

        elif self.number2 is 0:
            self.number2 = button_number
            self.top_string = str(button_number)
            self.label.config(text=str(button_number))

        elif self.number1 is not 0:
            self.top_string += str(button_number)
            self.number2 = int(self.top_string)
            self.label.config(text=self.top_string)


    def sign_pressed(self, sign):
        ''' This function is triggered when +,-,*, or / is pushed. First check num1 and num2 are already storage.
        If so, it performs an num1 equals total, then displays num1, then resets the sign to the last on pushed.
        Which allows for multiply calculations before pushing = button '''
        if self.number2 is not 0 and self.number1 is not 0:
            self.number1 = self.equals()
            self.label.config(text=str(self.number1))
            self.top_string = ''
        if sign is "+":
            self.add = True
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
        if sign is "-":
            self.add = False
            self.subtract = True  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
        if sign is "*":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = True  # x boolean
            self.divide = False
        if sign is "/":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = True
        else:
            if sign is "+":
                self.add = True
            if sign is "-":
                self.subtract = True
            if sign is "*":
                self.multiply = True
            if sign is "/":
                self.divide = True

    def equals(self):
        ''' Triggers calculation then clears all vars '''
        total = 0
        if self.add is True:
            total = self.number1 + self.number2
            self.number2 = 0    # resets for next calculation if clear is not presses

        elif self.subtract is True:
            total = self.number1 - self.number2
            self.number2 = 0

        elif self.multiply is True:
            total = self.number1 * self.number2
            self.number2 = 0

        elif self.divide is True:
            total = round(self.number1 / self.number2, 3)
            total = int(total) if total.is_integer() else total
            self.number2 = 0

        self.top_string = ''
        self.add = False
        self.subtract = False
        self.multiply = False
        self.divide = False
        self.label.config(text=str(total))
        return total

    def clear_all(self):
        '''Clears all vars'''
        self.top_string = ''    # first string to appear after selecting sign ( 9 + )
        self.number1 = 0       # storage of first number selected
        self.number2 = 0       # storage of second number selected
        self.add = False       # + boolean
        self.subtract = False  # - boolean
        self.multiply = False  # x boolean
        self.divide = False    # / boolean
        self.label.config(text='0')  # top label

if __name__ == '__main__':
    ROOT = Tk.Tk()
    ROOT.wm_title('Calculator')
    ROOT.resizable(width=False, height=False)
    Calculator(ROOT)
    ROOT.mainloop()