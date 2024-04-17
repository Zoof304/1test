import turtle
import random
from turtle import *

speed(10000)
def oblaka():
    for i in range(5):
            color('white')
            begin_fill()
            circle(100)
            end_fill()
            left(90)
            forward(100)
            right(90)
            forward(90)
            right(90)
            color('lightblue')
            forward(100)
            left(90)
            
time_day=str(input('Введите время суток: \n(Например: день\вечер\ночь\утро)\n\n: '))
if time_day=='день':
    bgcolor('lightblue')
    color('lightblue')
    forward(150)
    color('white')
    oblaka()
    home()
    right(90)
    forward(50)
    left(90)
    forward(-700)
    oblaka()
    
    home()
    left(90)
    forward(150)
    right(90)
    forward(-300)
    oblaka()
    home()
    
if time_day=='утро':
    bgcolor('lightyellow')
if time_day=='ночь':
    bgcolor('darkblue')
if time_day=='вечер':
    bgcolor('purple')
    color_block='blue'
pensize(1)
size_block=15
color_block=str('darkred')
a1=0
a2=0
a3=0
a4=0
a5=0

def vibor_pen():
    if time_day=='день':
        pencolor('lightblue') 
    if time_day=='ночь':
        pencolor('darkblue')
    if time_day=='вечер':
        pencolor('purple')
    if time_day=='утро':
        pencolor('lightyellow')


def house_block():
    fillcolor(color_block)
    pencolor(color_block)
    begin_fill()
            
    forward(size_block)
    left(90)
    forward(size_block)
    left(90)
    forward(size_block)
    left(180)
    end_fill()
    forward(size_block)

def house1():
    fillcolor(color_block)
    begin_fill()
    
    pencolor(color_block)
    forward(165)
    right(90)
    forward(30)
    right(90)
    forward(165)
    right(90)
    forward(30)
    
    end_fill()
    
    right(180)
    forward(45)
    left(90)
    
    for i in range(12):
        for i in range(5):
            house_block()
            
            pencolor('white')
            fillcolor('white')
            
            begin_fill()
            forward(size_block)
            right(90)
            forward(size_block)
            right(90)
            forward(size_block)
            right(90)
            forward(size_block)
            right(90)
            forward(size_block)
            right(90)
            forward(size_block)
            left(90)
            end_fill()
            
        house_block()
        right(90)
        forward(15)
        begin_fill()
        forward(15)
        right(90)
        forward(165)
        right(90)
        forward(15)
        right(180)
        end_fill()
        forward(30)
        left(90)

def zvezda():
    if time_day=='ночь':
        color('darkblue')
        home()
        color('darkblue')
        right(a1)
        forward(a2)
        color('white')
        fillcolor('white')
        begin_fill()
        circle(a3)
        end_fill()
        color('darkblue')
    if time_day=='вечер':
        color('purple')
        home()
        color('purple')
        right(a1)
        forward(a2)
        color('white')
        fillcolor('white')
        begin_fill()
        circle(a3)
        end_fill()
        color('purple')
    
    
if time_day=='ночь':  
    for i in range(50):
        a1=random.randint(50,360)
        a2=random.randint(100,600)
        a3=random.randint(2,3)
        zvezda()

if time_day=='вечер':  
    for i in range(50):
        a1=random.randint(50,360)
        a2=random.randint(100,600)
        a3=random.randint(2,3)
        zvezda()

if time_day=='ночь':
    color('darkblue')
    home()
    left(90)
    forward(150)
    color('white')
    begin_fill()
    circle(35)
    end_fill()
    right(45)
    forward(1)
    color('darkblue')
    begin_fill()
    circle(32)
    end_fill()
    
if time_day=='день':
    color('lightblue')
    home()
    left(90)
    forward(100)
    right(90)
    color('yellow')
    begin_fill()
    circle(90)
    end_fill()
    color('lightblue')

if time_day=='утро':
    color('lightyellow')
    home()
    left(90)
    forward(250)
    left(90)
    forward(-39)
    color('yellow')
    right(180)
    begin_fill()
    circle(50)
    end_fill()
    
if time_day=='вечер':
    color('purple')
    home()
    right(180)
    color('yellow')
    begin_fill()
    circle(300)
    end_fill()
    pendown()
    forward(-10)
    color('orange')
    begin_fill()
    circle(300)
    end_fill()
      
ot_centra=-300
werh=-20
def dom():
    if time_day=='день':
        color('lightblue')
    if time_day=='ночь':
        color('darkblue')
    if time_day=='вечер':
        color('purple')
    if time_day=='утро':
        color('lightyellow')
    home()
    forward(ot_centra)
    left(90)
    forward(werh)
    right(90)
    house1()
    
ot_centra=-100
def red(ralivka): 
    color('red') 
    if ralivka: 
        begin_fill() 
        circle(5) 
    if ralivka: 
        end_fill() 
         
def yellow(ralivka): 
    color('yellow') 
    if ralivka: 
        begin_fill() 
        circle(5) 
    if ralivka: 
        end_fill() 
         
def green(ralivka): 
    color('light green') 
    if ralivka: 
        begin_fill() 
        circle(5) 
    if ralivka: 
        end_fill() 
 
 
 
 
# ЭТО АСФАЛЬТ 
 
home()
penup() 
goto(0, -345) 
pendown() 
begin_fill() 
color('gray') 
forward(680) 
left(90) 
forward(20) 
left(90) 
forward(1360) 
left(90) 
forward(20) 
end_fill() 
 
left(-180) 
forward(21) 
 
# ЭТО ЗЕМЛЯ 

begin_fill() 
color('green') 
right(90) 
forward(1360) 
left(90) 
forward(12) 
left(90) 
forward(1360) 
end_fill() 
 
forward(-1000) 
left(90) 
forward(12) 
 
# cyber truck 
 
begin_fill() 
color('purple') 
left(90) 
forward(75) 
left(90) 
forward(18) 
left(90) 
forward(75) 
end_fill() 
pencolor('purple') 
pensize(4) 
begin_fill() 
color('light blue') 
left(70) 
forward(-5) 
right(50) 
forward(-5) 
right(-2) 
forward(-10) 
left(180) 
forward(20) 
right(22) 
forward(33) 
right(70) 
forward(22) 
end_fill() 
pensize(1) 
pencolor('purple') 
right(20) 
forward(10) 
right(90) 
forward(10) 
pensize(4) 
color('black') 
circle(8) 
color('purple') 
pensize(1) 
forward(60) 
pensize(4) 
color('black') 
circle(8) 
pensize(1) 
color('purple') 
right(90) 
forward(10) 
begin_fill() 
color('yellow') 
circle(3) 
end_fill() 
 
vibor_pen()
 
home() 
penup() 
goto(0, -317) 
pendown() 
 
# это дерево 1 
 
forward(400)

begin_fill() 
color('brown') 
forward(6) 
left(90) 
forward(70) 
left(90) 
forward(6) 
left(90) 
forward(70) 
end_fill() 
 
pencolor('brown') 
left(180) 
forward(70) 
right(90) 
forward(6) 
begin_fill() 
color('green') 
circle(50) 
end_fill() 
 
penup() 
goto(-300, 0) 
pendown() 

vibor_pen()
right(90) 
forward(312) 
pencolor('green') 
forward(13) 
 
right(-90) 
 
# Дерево 2 

begin_fill() 
color('brown') 
forward(6) 
left(90) 
forward(60) 
left(90) 
forward(6) 
left(90) 
forward(60) 
end_fill() 
 
pencolor('brown') 
left(180) 
forward(60) 
right(90) 
forward(6) 
begin_fill() 
color('green') 
circle(40) 
end_fill() 
 
vibor_pen()
forward(100) 
home() 
forward(500) 
right(90) 
forward(312) 
color('green') 
forward(15) 
 
# светофор 
 
begin_fill() 
color('black') 
forward(9) 
left(90) 
forward(5) 
left(90) 
forward(50) 
left(90) 
forward(5) 
end_fill() 
 
begin_fill() 
color('black') 
forward(5) 
right(90) 
forward(40) 
right(90) 
forward(15) 
right(90) 
forward(40) 
end_fill() 
 
# //////// 
right(90) 
forward(2) 
right(90) 
forward(10) 
red(True) 
pencolor('black') 
forward(12) 
yellow(True) 
pencolor('black') 
forward(12) 
green(True) 
pencolor('black')

werh=1
if time_day=='вечер':
    color_block='lightblue'
dom()


ot_centra=-500
werh=-20
color_block='yellow'
if time_day=='вечер':
    color_block='lightblue'
dom()

werh=50
ot_centra=300
color_block='red'
if time_day=='вечер':
    color_block='lightblue'
dom()

werh=-40
color_block='green'
if time_day=='вечер':
    color_block='lightblue'
ot_centra=500
dom()

werh=30
color_block='blue'
if time_day=='вечер':
    color_block='lightblue'
ot_centra=-200
dom()

exitonclick()
