angle=1
def setup():
    size(1300,690)
    background(150)
    frameRate(100)
def draw():
    background(50)
    global angle
    if mousePressed == True:
        translate(100,100)
        rotate(radians(angle))
        rect(mouseX,mouseY,50,50)
        angle+=1
        
