"""
This a program for visualizing 2D vector addition
Author: ORION-CS
"""
from tkinter import *

vectors = {}
composited = False
composited_vector_id = 0

def move(event):
    global vectors
    canvas = event.widget
    canvasx = canvas.canvasx(event.x)
    canvasy = canvas.canvasy(event.y)
    item = canvas.find_closest(canvasx, canvasy)
    cv.coords(item[0], 400, 300, event.x, event.y)
    vectors[item[0]] = [event.x-400, event.y-300]
    vector_composite()

def create(event):
    global vectors
    id = cv.create_line(400, 300, event.x, event.y, arrow='last')
    vectors[id] = [event.x-400, event.y-300]
    vector_composite()

def vector_composite():
    global composited_vector_id, composited, vectors
    x, y = 0, 0
    for x_, y_ in vectors.values():
        x += x_
        y += y_
    if composited:
        cv.coords(composited_vector_id, 400, 300, x+400, y+300)
    else:
        composited_vector_id = cv.create_line(400, 300, x+400, y+300, arrow='last', fill='red', width=2)
        composited = True

root = Tk(className='Vectors')
cv = Canvas(root, bg='white', width=800, height=600)
cv.bind("<B1-Motion>", move)
cv.bind("<Button-3>", create)
cv.pack()
root.mainloop()
