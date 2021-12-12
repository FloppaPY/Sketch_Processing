texts=50
def setup():
    size(1000,600)
    background(30)
    frameRate(50)
def draw():
    global texts
    textSize(30)
def keyPressed():
    global texts
    text(key,texts,300)
    texts=texts+22
#if key==CODED:
    #if keyCode == UP
       
