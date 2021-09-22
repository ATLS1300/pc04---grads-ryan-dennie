"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Ryan Dennie

This code relates to an artist's painting that accomplishes the following:
    -It has a frame
    -It has a generative chessboard in the center that uses https://coolors.co template 
    -It has a generative background color
    -It has a generative signature that uses 2 turtles and changes each time to represent the new artist's input
    -Incorporates signature idea from classmate's psuedocode

"""
#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Ryan Dennie
Sept 20, 2021
'''

import math as re
import numpy as np 
import random
    
def corner(segments, size, width, height, spot = 0, dist = 10):
    turtle.speed(10)
    horizontal = []
    vertical = []
    if spot == 0:
        x, y = -(width/2) + dist, (height/2) - dist
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        for i in range(segments):
            horizontal.append((x+(i+1)*size, y))
        for i in range(segments):
            vertical.append((x, y-(i+1)*size))
    
    if spot == 1:
        x, y = (width/2) - dist, (height/2) - dist
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        for i in range(segments):
            horizontal.append((x-(i+1)*size, y))
        for i in range(segments):
            vertical.append((x, y-(i+1)*size))
    
    if spot == 2:
        x, y = (width/2) - dist, -(height/2) + dist
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        for i in range(segments):
            horizontal.append((x-(i+1)*size, y))
        for i in range(segments):
            vertical.append((x, y+(i+1)*size))
            
    if spot == 3:
        x, y = -(width/2) + dist, -(height/2) + dist
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        for i in range(segments):
            horizontal.append((x+(i+1)*size, y))
        for i in range(segments):
            vertical.append((x, y+(i+1)*size))
    
    for i, point in enumerate(vertical):
        if i % 2 == 0:
            turtle.color("orange")
        else:
            turtle.color("blue")
            
        i = i+1
        turtle.penup()
        turtle.setpos(point)
        turtle.pendown()
        turtle.setheading(turtle.towards(horizontal[-i]))
        x0 = point[0]
        y0 = point[1]
        x1 = horizontal[-i][0]
        y1 = horizontal[-i][1]
        distance = re.sqrt((x0-x1)**2 + (y0-y1)**2)
        turtle.forward(distance)
        
    
    
def checkerboard(width, size):
    turtle.speed(10)
    start_x = width*size/2.0
    start_y = width*size/2.0
    turtle.penup()
    x, y = turtle.pos()
    turtle.setpos(x - start_x, y - start_y)
    length = width*size
    
    fill = 0
    turtle.fillcolor(0,0,0)
    for i in range(width):
        for j in range(width):
            turtle.begin_fill()
            if fill % 2 == 0:                
                turtle.fillcolor(0,0,0)
            else:
                turtle.fillcolor(random.choice([(116, 0, 184), (105, 48, 195), (94, 96, 206), (83, 144, 217), (78, 168, 222), (72, 191, 227),(86, 207, 225),(100, 223, 223), (114, 239, 221), (128, 255, 219)]))
            turtle.pendown()
            turtle.forward(size)
            turtle.left(90)
            turtle.forward(size)
            turtle.left(90)
            turtle.forward(size)
            turtle.left(90)
            turtle.forward(size)
            turtle.left(90)
            turtle.end_fill()
            fill += 1
            x, y = turtle.pos()
            turtle.setpos(x+size, y)
        
        if width % 2 == 0:
            fill += 1
        turtle.penup()
        x, y = turtle.pos()
        turtle.setpos(x-length,y+size)

#built with idea from Kevin Ecke's pseudocode
# enter code below
def signature(width, height):
    start_x = -75
    start_y = -height*6.0/16.0
        
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    
    t1.speed(10)
    t2.speed(10)
    t1.color(255,0,0)
    t2.color(0,0,255)
    t1.penup()
    t2.penup()
    t1.setpos(start_x, start_y)
    t2.setpos(start_x, start_y+2)
    t1.pendown()
    t2.pendown()
    
    x_offset = 5
    
    for i in range(30):
        
        r = random.randint(1, 100)
        new_offset = x_offset
        if r <= 20:
            new_offset = -x_offset
            
        x1, y1 = t1.pos()
        x2, y2 = t2.pos()
        y_offset = random.randint(-7, 7)
        d = re.sqrt(new_offset**2 + y_offset**2)
        x1 += new_offset
        x2 += new_offset
        y1 += y_offset
        y2 += y_offset
        t1.setheading(t1.towards((x1, y1)))
        t1.forward(d)
        t2.setheading(t2.towards((x2, y2)))
        t2.forward(d)

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)


# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#=======Add your code here======
turtle.tracer(0)
checkerboard(12, 30)
corner(30, 15, w, h, spot = 0)
corner(30, 15, w, h, spot = 1)
corner(30, 15, w, h, spot = 2)
corner(30, 15, w, h, spot = 3)
turtle.tracer(1)
signature(w, h)

#=============================== 
# This section allows for clean execution of the code! (Ignore it)
turtle.up()    


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
panel.bgcolor(random.choice(["grey","yellow","green","black"]))

turtle.done()