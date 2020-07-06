# import everything from tkinter module
from tkinter import *
import random
import re
from playsound import playsound

# globally declare the expression variable
expression = ""


class NumberButton(Button):
    def __init__(self, parent, *args, **kwargs):
        Button.__init__(self, parent, bg='pink', fg='black', font=('Helvetica', '20'), height=2, width=7
                        , *args, **kwargs)
        self.parent = parent


class OperatorButton(Button):
    def __init__(self, parent, *args, **kwargs):
        Button.__init__(self, parent, bg='orange', fg='black', font=('Helvetica', '20'), height=2, width=7
                        , *args, **kwargs)
        self.parent = parent


class SpecialButton(Button):
    def __init__(self, parent, *args, **kwargs):
        Button.__init__(self, parent, bg='plum', fg='black', font=('Helvetica', '20'), height=2, width=7
                        , *args, **kwargs)
        self.parent = parent


def is_int(value):
    try:
        number = int(value)
        return TRUE
    except ValueError:
        return False


# Function to update expression
# in the text entry box
def press(value):
    # point out the global expression variable
    global expression

    # play sound
    if is_int(value):
        read_digit(value)
    else:
        read_operator(value)

    # concatenation of string
    expression = expression + str(value)

    # update the expression by using set method
    equation.set(expression)


def random_number():
    # point out the global expression variable
    global expression

    # pick a random integer
    random_num = random.randint(0, 100)
    # concatenation of string
    expression = expression + str(random_num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equal_press():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression
        playsound('HebrewEquals.mp3')

        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        expression = ""

    # if error is generate then handle
    # by the except block
    except:
        playsound('Error.mp3')
        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# read the number string
def read_number(number_string):
    pass


def read():
    print(equation.get())
    numbers_to_read = re.split('[+*-/]', equation.get())
    print(numbers_to_read)
    for number_string in numbers_to_read:
        if len(number_string) == 0:
            return
        elif len(number_string) == 1:
            read_digit(int(number_string))
        else:
            read_number(number_string)


def read_number(number_to_read):
    if len(number_to_read) <= 3:
        for i in range(len(number_to_read)):
            if len(number_to_read) > 1:
                read_digit_by_location(number_to_read[i], len(number_to_read) - i, i == len(number_to_read) - 1)
    else:
        simple_number = number_to_read[-3:]
        thousands_number = number_to_read[-6:-3]
        millions_number = number_to_read[-9:-6]
        print("simple number " + str(simple_number))
        print("thousands " + str(thousands_number))
        print("millions " + str(millions_number))


def read_digit_by_location(digit, location, and_before_ahadot):
    print(str(digit) + " in location " + str(location))
    if location == 1:
        if and_before_ahadot:
            playsound('HebrewAnd.mp3')
        read_digit(int(digit))





# Given the chosen digit - play the relevant sound
def read_digit(digit):
    digit_to_audio = {
        0: 'HebrewZero.mp3',
        1: 'HebrewOne.mp3',
        2: 'HebrewTwo.mp3',
        3: 'HebrewThree.mp3',
        4: 'HebrewFour.mp3',
        5: 'HebrewFive.mp3',
        6: 'HebrewSix.mp3',
        7: 'HebrewSeven.mp3',
        8: 'HebrewEight.mp3',
        9: 'HebrewNine.mp3'
    }
    playsound(digit_to_audio.get(digit))


def read_operator(operator):
    operator_to_audio = {
        '+': 'HebrewPlus.mp3',
        '-': 'HebrewMinus.mp3',
        '*': 'HebrewMultiply.mp3',
        '/': 'HebrewDivide.mp3'
    }
    playsound(operator_to_audio.get(operator))


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light steel blue")

    # set the title of GUI window
    gui.title("Shir-ran's talking calculator!")

    # set the configuration of GUI window
    gui.geometry("650x650")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation, font=('Helvetica', '20'))

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=160)

    equation.set('enter your expression')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = NumberButton(gui, text=' 1 ', command=lambda: press(1))
    button1.grid(row=2, column=0)

    button2 = NumberButton(gui, text=' 2 ', command=lambda: press(2))
    button2.grid(row=2, column=1)

    button3 = NumberButton(gui, text=' 3 ', command=lambda: press(3))
    button3.grid(row=2, column=2)

    button4 = NumberButton(gui, text=' 4 ', command=lambda: press(4))
    button4.grid(row=3, column=0)

    button5 = NumberButton(gui, text=' 5 ', command=lambda: press(5))
    button5.grid(row=3, column=1)

    button6 = NumberButton(gui, text=' 6 ', command=lambda: press(6))
    button6.grid(row=3, column=2)

    button7 = NumberButton(gui, text=' 7 ', command=lambda: press(7))
    button7.grid(row=4, column=0)

    button8 = NumberButton(gui, text=' 8 ', command=lambda: press(8))
    button8.grid(row=4, column=1)

    button9 = NumberButton(gui, text=' 9 ', command=lambda: press(9))
    button9.grid(row=4, column=2)

    button0 = NumberButton(gui, text=' 0 ', command=lambda: press(0))
    button0.grid(row=5, column=1)

    plus = OperatorButton(gui, text=' + ', command=lambda: press("+"))
    plus.grid(row=2, column=3)

    minus = OperatorButton(gui, text=' - ', command=lambda: press("-"))
    minus.grid(row=3, column=3)

    multiply = OperatorButton(gui, text=' * ', command=lambda: press("*"))
    multiply.grid(row=4, column=3)

    divide = OperatorButton(gui, text=' / ', command=lambda: press("/"))
    divide.grid(row=5, column=3)

    equal = SpecialButton(gui, text=' = ', command=equal_press)
    equal.grid(row=7, column=1)

    clear = SpecialButton(gui, text='Clear', command=clear)
    clear.grid(row=7, column=2)

    readme = SpecialButton(gui, text='Read', command=read)
    readme.grid(row=7, column=3)

    random_button = SpecialButton(gui, text='Rand', command=random_number)
    random_button.grid(row=7, column=0)

    # Decimal = NumberButton(gui, text='.', command=lambda: press('.'))
    # Decimal.grid(row=6, column=0)
    # start the GUI
    playsound('CalcAnnouncement.mp3')
    gui.mainloop()
    playsound('goodbye.mp3')
