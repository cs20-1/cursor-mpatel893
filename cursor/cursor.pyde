# Name:Mann Patel
# Class:CS20
# Date:2020-09-17
# Description: coursoer

def setup():
    size(500, 500)
    frameRate(100)

def draw():
    background(57, 0, 0)
    stroke(255) # white
    
    # big outter square
    fill(167, 38, 0) # dark orange
    square(mouseX+50, mouseY+50, 60)
    
    # middle rotated square
    fill(214, 151, 0) # yellow
    square(mouseX+50, mouseY+50, 40)
    
    # small square insidde the middle rotated square
    fill(220, 94, 0) # orange
    square(mouseX+50, mouseY+50, 20)
   
