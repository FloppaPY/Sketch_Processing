x=0
y=0
px=0
py=0
def setup():
    size(1000,600)
def draw():
    global x,y
    background(255)
    rect(x,50,200,200)
    rect(x,y,px,py)
    if mousePressed == True:
        global x
        rect(x,50,300,100)
        if mouseX > 50 and mouseX < 150 and mouseY > 50 and mouseY < 350:
            x=x+1
