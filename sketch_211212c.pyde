myText=""
def setup():
    size(1000,600)
    background(30)
    frameRate(50)
def draw():
    global myText
    textSize(30)
def keyPressed():
    global myText
    text(myText,50,300)
    myText=myText+key
