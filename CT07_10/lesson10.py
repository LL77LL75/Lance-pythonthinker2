## Task 1: Function without parameter (w/o turtle)
# You are required to print the same "Motion Detected" phrase
# multiple times as part of a motion detecting program that you
# are creating.

# Create an 'alert()' function that will print "Motion Detected"
# whenever the function is called.

# **Example**
# Input:
#     alert()
# Output:
#     Motion Detected
def alert():
    print('motion detected ' * 100000)
alert()

## Task 2: Function without parameter (w turtle)
# Using the 'turtle' library, create a 'square()' function that
# draws a 20x20 square at the turtle object's current position
# whenever the function is called.

# By calling the 'square()' function, draw a square anywhere
# within the turtle window.
import turtle
t = turtle.Turtle()
window = turtle.Screen()
window.setup(800, 400)
# def square1():
#     for i in range(4):
#         t.forward(40)
#         t.right(90)
# square1()


## Task 3: Function with parameter (w/o turtle)
# Write a Python function 'multiply()', that takes 2 parameters,
# a and b, and prints the product of these 2 numbers.

# **Example**
# Input:
#     multiply(3,5)
# Output:
#     15

## Task 4: Function with parameter (w turtle)
# Using the 'turtle' library, create a function 'drawSquare()',
# with 2 parameters, x and y, and draw a 20x20 square at the
# coordinate (x, y).

# You may use the following steps as a guide:
# 1. Import 'turtle' library
# 2. Create a turtle object using 'turtle.Turtle()'
# 3. Define a function 'drawSqare()' with 2 parameters, x and y
#         a. Lift the pen using '.penup()'
#         b. Reposition the turtle object using '.goto(x, y)'
#         c. Put the pen down using '.pendown()'
#         d. Create a 'for' loop to draw a square
# 4. Test out your program using 'drawSquare(-50, 50)'
# 5. Use '.mainloop()' to keep the window open
def square(x,y):
    t.goto(x,y)
    for i in range(4):
        t.forward(40)
        t.right(90)
square(100,100)


## Task 5: Function with return value (w/o turtle)
# Define an 'isElderly()' function with 1 parameter, age,
# and return True if the age is larger than, or equal to 65.

# Using the 'isElderly()' function created, create a program
# that asks the user for their age. Then use an 'if' statement
# to print "You are eligible for an elderly discount" if
# 'isElderly()' returns True.

# def isElderly(age):
#     return age >= 65
# if isElderly(int(input("age"))):
#     print("u get discount")
# else:
#     print("no discount for u")

## Task 6: Function with return value (w turtle)
# Using 'xcor()' and 'ycor()', create a function 'turtleCoord()'
# that takes in a parameter, turtle_obj, and returns the current
# x and y coordinates of the turtle object.

# Then, using the 'turtleCoord()' function, modify your answer
# from Task 4 to print out the coordinates of the turtle object
# after drawing a square.
# def turtleCoord(turtle):
#     return turtle.xcor(),turtle.ycor()

# print(turtleCoord(t))
## Task 7: Whatsapp link generator
# Imagine you have a website and you want to include a button or
# link that allows people to easily chat with you on Whatsapp.

# Can you write a function called whatsappMe() that takes
# someone's phone number (without any dashes or spaces) and
# creates a link that opens a chat with them on Whatsapp?

# For example, if given '98765432' as the argument, the function
# should print: 'Whatsapp me at https://wa.me/6598765432'

# **Bonus Challenge**
# 1. Write some code that creates a list of 100 random 8-digit
#    phone numbers that starts with either '8' or '9'. Then using
#    the whatsappMe() function, print a list of WhatsApp links
#    for each of the numbers.
# 2. Modify your code so that each of the 100 random 8-digit
#    phone numbers generated is unique.

# def text(numbers):
#     print("whatsapp me at https://wa.me/" + str(numbers))
# text(12942669)

## Task 8: Random Generator
# Imagine you have a magic hat that can only hold numbers between
# 1 and 100. This function, called "randgen", acts like shaking
# that hat.

# You tell "randgen" how many numbers to shake out of the hat
# (let's call this number "shakes").

# "randgen" will then shake out that many numbers and put them
# in a bag.

# Once it's done, "randgen" will tell you:
# 1. How many numbers it shook out (the "shakes" number).
# 2. The biggest number it shook out.
# 3. The smallest number it shook out.

# 4. The average of all the numbers it shook out
import random
# nums = []
# def randgen(times):
#     for i in range(times):
#         nums.append(random.randint(1,100))
# print("numbers generated :" +)

## Task 9: Rock Paper Scissors
# How can we write Python code to play Rock, paper, scissors
# against the computer?

# We need 2 functions:
# 1. A 'generate_computer_move' function to generate a random
#    choice of "rock", "paper", or "scissors" for the computer.
# 2. A 'determine_winner' function to determine the winner based
#    on the player's choice and the computer's random choice.

# After creating the 2 functions, the main part of the code runs
# in a loop:
# 1. Prompt the user for their move ("rock", "paper", or
#    "scissors").
# 2. Validate the user's input.
# 3. Generate the computer's move using the
#    'generate_computer_move' function.
# 4. Print both the player's and computer's moves.
# 5. Determine the winner using the 'determine_winner' function
#    and print the result.
# 6. Ask the user if they want to play again.
# 7. The loop continues until the user chooses not to play again
moves = ["rock","paper","siscors"]
winLose=[]
def generate_computer_move(move):
    if not (random.randint(1,100) == random.randint(1,100)):
        if move == "rock":
            winLose.append("pc")
            return "paper"
        if move == "siscors":
            winLose.append("pc")
            return "stone"
        if move == "paper":
            winLose.append("pc")
            return "siscors"
    else:
        choice = ()
        return moves[random.randint(1,3)]
print(generate_computer_move(input("MOVE ")))









# **Bonus Challenge**
# 1. Keep track of the score for both you and the computer and
#    display the current score after each round.
# 2. Add an option at the start of the program to allow for
#    single or 2-player mode. In 2-player mode, allow 2 players
#    to take turns choosing their moves and determine the winner
#    between them.
# 3. When the game ends, pick a random forfeit from a list that
#    the loser have to do.
window.mainloop()


