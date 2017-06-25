from microbit import *

def start (i):
    torpedo_i = i
    torpedo_j = 3
    torpedo = True
    display.set_pixel(torpedo_i, torpedo_j, 9)

def fired ():
    return torpedo

def move ():

i=2
j=3
h=9
inc=1
torpedo=False
it=0
iold=i
display.set_pixel(i,4,h)

while True:
    sleep(200)
    if torpedo:
        display.set_pixel(it,j,0)
        j=j-1
        if j<0:
            torpedo=False
        else:
            display.set_pixel(it,j,9)

    if button_a.is_pressed() and button_b.is_pressed():
        it=i
        j=3
        display.set_pixel(it,j,9)
        torpedo=True
    elif button_a.is_pressed():
        h=9
        if i>0:
            i=i-1
    elif button_b.is_pressed():
        h=9
        if i<4:
            i=i+1
    else:
        h=h+inc
#       inkrement
        if h<1:
            inc=-inc
            h=1
        elif h>9:
            inc=-inc
            h=9

    display.set_pixel(iold,4,0)
    display.set_pixel(i,4,h)
    iold=i


