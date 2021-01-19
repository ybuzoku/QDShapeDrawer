import turtle
import random

dw = turtle.Turtle()        #Drawing turtle
dw.penup()
dw.shape("circle")
dw.speed(0)
window = turtle.Screen()    #Screen turtle
window.tracer(0)

#Lookup list of turtles, made of shape_info dictionaries
shape_list = []             
#Each entry will be a dictionary of entries
program_on = True
#shape class prototype=> {"name":"","function": pass,"colours":[],"xcor":0.0, "ycor":0.0}
#shape names is a lookup table mapping the number of sides to the shape name... for convenience
shapenames = {"0":"Circle","3":"Triangle", "4":"Square", "5":"Pentagon"}
#This function is only called by program. Not by user!
def draw_shape(sides):
    dw.pendown()
    dw.begin_fill()
    #Special case of circle
    if sides == 0:
        dw.circle(25)
    for _ in range(sides):
        dw.forward(50)
        dw.left(360/sides)
    dw.end_fill()
    dw.penup()

def shape_instantiator(passthrough, var1):
    #passthrough=True <=> New instance of shape being drawn
    #passthrough=True  => var1=number of sides the shape should have
    #passthrough=False => var1=offset into list of shapes drawn
    dw.hideturtle()             #Dont show cursor moving to new location
    tempx=dw.xcor()             #Temporary coordinate storage variables
    tempy=dw.ycor()
    sides=0                     #Empty declare to allow for later type appropriate referencing

    if passthrough == True:     #Create a new instance of shape
        sides=var1
        red = random.random()
        green = random.random()
        blue = random.random()
        dw.color(red, green, blue)
        colourtriple = [red, green, blue]
        newshape = {"name":shapenames[str(sides)],"sides": sides,"colours":colourtriple,"xcor":tempx, "ycor":tempy}
        shape_list.append(newshape)
    else:                       #Focus a previous instance of the shape
        instance = shape_list[var1]
        sides = instance["sides"]
        dw.setpos(instance["xcor"],instance["ycor"])
        dw.color(instance["colours"][0],instance["colours"][1], instance["colours"][2])

    draw_shape(sides)   #Draw a shape with n sides
    #Return cursor to original position
    dw.setpos(tempx, tempy) #Return cursor to original position, if it was moved
    dw.color("black")   #Return cursor to normal colour
    dw.showturtle() #Reactivate cursor

def list_shapes():
    print("Shapes List:")
    for i in range(len(shape_list)):
        shape = shape_list[i]
        print("Shape number: "+str(i+1)+" || Shape Type: "+shape["name"])

def move_up():
    dw.sety(dw.ycor() + 5)

def move_down():
    dw.sety(dw.ycor() - 5)

def move_right():
    dw.setx(dw.xcor() + 5)

def move_left():
    dw.setx(dw.xcor() - 5)

def square_stub():
    shape_instantiator(True, 4) #New shape, four sides

def triangle_stub():
    shape_instantiator(True, 3)

def pentagon_stub():
    shape_instantiator(True, 5)

def circle_stub():
    shape_instantiator(True, 0)

def quit_stub():
    program_on = False

def focus_handler():   #Will prompt at console for a number
    incorrect_input1 = True #Assume the user will input poorly!
    window.bgcolor("red")   #Pause, return to console to enter somth at the prompt
    usrinput = "0"
    while incorrect_input1:
        nullifyAsyncFunctions() #Kill async functionality
        print("Shape Menu: Press r to return to unfreeze drawing window!")
        list_shapes()   #List the shapes
        usrinput = input("\nShape#>")
        if usrinput == "r":
            incorrect_input1 = False
        else:
            try:
                usrinput = int(usrinput)
            except ValueError:
                print("Please type a valid number!\a\a\n")
            else:
                usrinput -= 1   #dec usrinput!
                if usrinput >= 0 and usrinput < len(shape_list):
                    shape_instantiator(False, usrinput) #Call the shape drawer to bring up shape
                    incorrect_input1 = False
                else:   #Invalid input
                    print("Please type a valid number or r to return\a\n")
    instantiateAsyncFunctions() #Return async functionality to keys
    window.bgcolor("white") #Return to game!

def print_help():
    print("Use arrow keys to move, c to draw a circle, s for a square, p for a pentagon, t for a triangle")
    print("Alternatively, press space to select a shape to focus!")
    print("Type l for a list of drawn shapes!")

def null():
    pass

def nullifyAsyncFunctions():
    window.onkeypress(null, "Up")
    window.onkeypress(null, "Down")
    window.onkeypress(null, "Left")
    window.onkeypress(null, "Right")
    window.onkeypress(null,"space")
    window.onkeypress(null, "s")
    window.onkeypress(null, "S")
    window.onkeypress(null, "t")
    window.onkeypress(null, "T")
    window.onkeypress(null, "p")
    window.onkeypress(null, "P")
    window.onkeypress(null, "c")
    window.onkeypress(null, "C")
    window.onkeypress(null, "l")
    window.onkeypress(null,"L")
    window.onkeypress(null, "h")
    window.onkeypress(null, "H")

def instantiateAsyncFunctions():
    window.onkeypress(move_up, "Up")
    window.onkeypress(move_down, "Down")
    window.onkeypress(move_left, "Left")
    window.onkeypress(move_right, "Right")
    window.onkeypress(focus_handler,"space")
    window.onkeypress(square_stub, "s")
    window.onkeypress(square_stub, "S")
    window.onkeypress(triangle_stub, "t")
    window.onkeypress(triangle_stub, "T")
    window.onkeypress(pentagon_stub, "p")
    window.onkeypress(pentagon_stub, "P")
    window.onkeypress(circle_stub, "c")
    window.onkeypress(circle_stub, "C")
    window.onkeypress(list_shapes, "l")
    window.onkeypress(list_shapes,"L")
    window.onkeypress(print_help, "h")
    window.onkeypress(print_help, "H")

###################################
############ Main Proc ############
###################################
print("Welcome to PyDraw 3000!!")
print("Written by Yll Buzoku")
instantiateAsyncFunctions()
print_help()

while program_on:
    window.update()
    window.listen()

window.bgcolor("blue")
turtle.done()
###################################
###################################
###################################