els=50
def setup():
    size(1000,600)
    background(30)
    frameRate(50)
def draw():
    global els
    background(0)
    ellipse(250,250,els,els)
    if keyPressed == True:
        els=els+4
    if keyPressed == False:
        els=els-4
    #if key==CODED:
        #if keyCode == UP:
            #els=els+5
        #if keyCode == DOWN:
            #els=els-5
    
