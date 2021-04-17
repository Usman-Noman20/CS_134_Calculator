import math
import inspect


class Calculate:
    """
    Class for calculating all the different functions of the calculator

    add(number1, number2)
    subtract(number1, number2)
    multiply(number1, number2)
    divide(number1, number2)
    factorial(number)
    area_of_triangle(height, width)

    Every function will always return a number, either an int
    or, if a float is used as an input (or it is division), it will return
    a float.

    """
    def __init__(self):
        pass

    def add(self, number1, number2):
        # adds number 1 + number2
        return number1 + number2

    def subtract(self, number1, number2):
        # subtracts number1 - number2
        return number1 - number2

    def multiply(self, number1, number2):
        # multiplies number1 - number2
        return number1 * number2

    def divide(self, number1, number2):
        # divides number1 / number2, uses math.floor to remove trailing decimals if not a float
        if isinstance(number1, float):
            return number1 / number2
        return math.floor(number1 / number2)

    def factorial(self, number):
        # uses builtin module math to get factorial
        return math.factorial(number)

    def area_of_triangle(self, height, width):
        # not flattening with math.floor to keep precision
        return 0.5 * (height * width)


class UserInput:
    """
    Class to parse and ask for user input using the input() builtin

    get_function() -> Asks the user what function of the calculator they would like to use. Returns a
    lowercase string from the following list: ["add", "subtract", "divide", "multiply", "factorial", "triangle", "quit"]
    get_number(amount) -> Asks the user for a certain amount of numbers (or height + width if amount == triangle)
    Returns a tuple of the numbers that the user input.
    incorrect_input(input_given) -> Prints an error to the user depending on what function called incorrect_input().
    Searches through local dict list_of_responses to print out the proper error message.
    """

    def __init__(self):
        pass

    def incorrect_input(self, input_given):
        """Prints out an error message to the user depending on what function called incorrect_input.
        :param input_given: The incorrect value
        :return: None
        """
        caller = inspect.currentframe().f_back.f_code.co_name
        # https://stackoverflow.com/questions/2654113/how-to-get-the-callers-method-name-in-the-called-method
        list_of_responses = {"get_function":
                             "Expected add, subtract, divide, multiply, factorial, or triangle. Instead got [",
                             "get_number": "Expected a number. Instead got ["}
        # list_of_responses = function name as key, error message as value
        print(list_of_responses[caller] + str(input_given) + "] Try again.")
        # print the error message using the calling functions key
        # converts to str explicitly in case python does not

    def get_function(self):
        """
        Asks the user what function they would like to perform. Continues asking until a valid answer
        is provided.
        :return: The users input
        """
        valid_functions = ["add", "subtract", "divide", "multiply", "factorial", "triangle", "quit"]
        #  ensure input is valid, if not, ask again for a valid input
        user_in = input("What would you like to do? "
                        "(Add/Subtract/Divide/Multiply/Factorial/Triangle/Quit)\n> ").lower().strip()
        if user_in not in valid_functions:
            self.incorrect_input(user_in)
            return self.get_function()
        return user_in

    def get_number(self, amount):
        """
        Asks the user for a specified amount of numbers, depending on the amount param

        :param amount: Amount of numbers to ask the user for. if amount == triangle, amount = 2
        :type amount: int or str
        :return: A tuple of int or float
        """
        number_list = []  # used when going through while number < amount:
        to_return = []  # used at the end of the function to avoid issues with floats, i.e. having
        # int + float (which could result in a TypeError)
        triangle_list = ["height", "width"]
        triangle = False
        number = 0
        is_float = False
        if amount == "triangle":  # if amount is "triangle", change how the user is prompted
            triangle = True
            amount = 2  # triangle needs 2 numbers, height + width
        while number < amount:
            if triangle:
                user_in = input("Enter {}\n> ".format(triangle_list[number]))  # [0] = height, [1] = width
            else:
                user_in = input("Enter Number #{}\n> ".format(number+1))
            if "." in user_in:  # not the cleanest way of doing it, but since input() always returns str, it makes
                #                 some level of sense.
                try:
                    user_in = float(user_in)  # ensure we can convert to float
                    number_list.append(user_in)
                    is_float = True
                    number = number + 1
                except ValueError:  # check if variable is float
                    self.incorrect_input(user_in)
            else:
                try:
                    user_in = int(user_in)  # ensure we can convert to int
                    number_list.append(user_in)
                    number = number + 1
                except ValueError:  # check if variable is valid. if not, ask again and DO NOT increment counter
                    self.incorrect_input(user_in)
        if is_float:  # is_float triggered, change all variables (including previous) to floats, then return
            #           as a tuple
            for number in number_list:
                to_return.append(float(number))
            return tuple(to_return)
        return tuple(number_list)  # no else needed because of previous return, no floats detected so we don't need
        #                            to iterate over anything


def print_result(number):
    """
    Simple function, just reduces number of duplicate lines
    :param number:
    :return:
    """
    print("The result is: {}\n".format(number))  # .format() puts the variable in the {} placeholder, \n for linebreak


# if __name__ == "__main__" allows calculator.py to be imported into another program without it running on import
if __name__ == "__main__":
    # main loop of the program, goes through loop if called directly.
    user_input = UserInput()  # create instances of both UserInput and Calculate
    calc = Calculate()
    while True:  # we want to keep asking the user until the program is ended using "quit"
        function = user_input.get_function()
        # large if statement to check what the function is. we know it HAS to be one of the following choices
        # because of how UserInput.get_function() is wrote.
        # no switch statements in python
        if function == "add":
            numbers = user_input.get_number(2)
            print_result(calc.add(numbers[0], numbers[1]))
        if function == "subtract":
            numbers = user_input.get_number(2)
            print_result(calc.subtract(numbers[0], numbers[1]))
        if function == "divide":
            numbers = user_input.get_number(2)
            print_result(calc.divide(numbers[0], numbers[1]))
        if function == "multiply":
            numbers = user_input.get_number(2)
            print_result(calc.multiply(numbers[0], numbers[1]))
        if function == "factorial":
            numbers = user_input.get_number(1)  # different from other lines as only 1 input is needed to get
            #                                     a numbers factorial
            print_result(calc.factorial(numbers[0]))
        if function == "triangle":
            numbers = user_input.get_number("triangle")  # see UserInput.get_number() for more info on why we are
            #                                              sending it a string instead of a number
            print_result(calc.area_of_triangle(height=numbers[0], width=numbers[1]))
        if function == "quit":
            exit()  # stop the program
        # no else needed, if some super bad error occurs the while True: will keep us going through the loop

