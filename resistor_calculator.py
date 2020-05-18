#!/usr/bin/python3
#this app uses GUIZERO
from guizero import *
import math

#define colors
black = (0, 0, 0)
brown = (165, 42, 42)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
violet = (128, 0, 128)
grey = (128, 128, 128)
white = (255, 255, 255)

#app parameters
app = App(title='Resistor Value', width=500, height=200, bg=grey, layout='grid')
def one():
    if band1.value == 'black':
        color1.value = int(0)
    if band1.value == 'brown':
        color1.value = int(1)
    if band1.value == 'red':
        color1.value = int(2)
    if band1.value == 'orange':
        color1.value = int(3)
    if band1.value == 'yellow':
        color1.value = int(4)
    if band1.value == 'green':
        color1.value = int(5)
    if band1.value == 'blue':
        color1.value = int(6)
    if band1.value == 'violet':
        color1.value = int(7)
    if band1.value == 'grey':
        color1.value = int(8)

def two():
    if band2.value == 'black':
        color2.value = int(0)
    if band2.value == 'brown':
        color2.value = int(1)
    if band2.value == 'red':
        color2.value = int(2)
    if band2.value == 'orange':
        color2.value = int(3)
    if band2.value == 'yellow':
        color2.value = int(4)
    if band2.value == 'green':
        color2.value = int(5)
    if band2.value == 'blue':
        color2.value = int(6)
    if band2.value == 'violet':
        color2.value = int(7)
    if band2.value == 'grey':
        color2.value = int(8)

def three():
    if band3.value == 'black':
        color3.value = int(1)
    if band3.value == 'brown':
        color3.value = int(10)
    if band3.value == 'red':
        color3.value = int(100)
    if band3.value == 'orange':
        color3.value = int(1000)
    if band3.value == 'yellow':
        color3.value = int(10000)
    if band3.value == 'green':
        color3.value = int(100000)
    if band3.value == 'blue':
        color3.value = int(1000000)
    if band3.value == 'violet':
        color3.value = int(10000000)
    if band3.value == 'grey':
        color3.value = int(100000000)

def band1_color():
    if band1.value == 'black':
        band1.bg=black
        band1.text_color=white
    if band1.value == 'brown':
        band1.bg=brown
        band1.text_color=black
    if band1.value == 'red':
        band1.bg=red
        band1.text_color=black
    if band1.value == 'orange':
        band1.bg=orange
        band1.text_color=black
    if band1.value == 'yellow':
        band1.bg=yellow
        band1.text_color=black
    if band1.value == 'green':
        band1.bg=green
        band1.text_color=black
    if band1.value == 'blue':
        band1.bg=blue
        band1.text_color=black
    if band1.value == 'violet':
        band1.bg=violet
        band1.text_color=black
    if band1.value == 'grey':
        band1.bg=grey
        band1.text_color=black

def band2_color():
    if band2.value == 'black':
        band2.bg=black
        band2.text_color=white
    if band2.value == 'brown':
        band2.bg=brown
        band2.text_color=black
    if band2.value == 'red':
        band2.bg=red
        band2.text_color=black
    if band2.value == 'orange':
        band2.bg=orange
        band2.text_color=black
    if band2.value == 'yellow':
        band2.bg=yellow
        band2.text_color=black
    if band2.value == 'green':
        band2.bg=green
        band2.text_color=black
    if band2.value == 'blue':
        band2.bg=blue
        band2.text_color=black
    if band2.value == 'violet':
        band2.bg=violet
        band2.text_color=black
    if band2.value == 'grey':
        band2.bg=grey
        band2.text_color=black

def band3_color():
    if band3.value == 'black':
        band3.bg=black
        band3.text_color=white
    if band3.value == 'brown':
        band3.bg=brown
        band3.text_color=black
    if band3.value == 'red':
        band3.bg=red
        band3.text_color=black
    if band3.value == 'orange':
        band3.bg=orange
        band3.text_color=black
    if band3.value == 'yellow':
        band3.bg=yellow
        band3.text_color=black
    if band3.value == 'green':
        band3.bg=green
        band3.text_color=black
    if band3.value == 'blue':
        band3.bg=blue
        band3.text_color=black
    if band3.value == 'violet':
        band3.bg=violet
        band3.text_color=black
    if band3.value == 'grey':
        band3.bg=grey
        band3.text_color=black

def final_result():
    one = color1.value
    two = color2.value
    three = color3.value
    intthree = int(three)
    combine = (str(one) + str(two))
    intcombine = int(combine)
    end_result.value = (intcombine) * (intthree)
    return int(end_result.value)

def how_many_ohms():
    result = int(final_result())
    if result < int(1000):
        how_many.value = 'ohms'
    if result > int(999):
        how_many.value = 'K ohms'
    if result > int(999999):
        how_many.value = 'M ohms'   

color1 = Text(app, text='0', grid=[0, 1])

color2 = Text(app, text='0', grid=[1, 1])

color3 = Text(app, text='0', grid=[2, 1])

band1 = Combo(app, grid=[0, 0], command=one, options=['black', 'brown', 'red', 'orange',
                            'yellow', 'green', 'blue', 'violet', 'grey'])
band1.width=8
band1.repeat(100, band1_color)

band2 = Combo(app, grid=[1, 0], command=two, options=['black', 'brown', 'red', 'orange',
                            'yellow', 'green', 'blue', 'violet', 'grey'])
band2.width=8
band2.repeat(100, band2_color)

band3 = Combo(app, grid=[2, 0], command=three, options=['black', 'brown', 'red', 'orange',
                            'yellow', 'green', 'blue', 'violet', 'grey'])
band3.width=8
band3.repeat(100, band3_color)

end_result = Text(app, text='0', grid=[3, 0])
end_result.repeat(100, final_result)

how_many = Text(app, text='', grid=[4,0])
how_many.repeat(100, how_many_ohms)

app.display()
