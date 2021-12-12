tx=0
bg=255
x=150
y=150
def setup():
    size(1000,600)
    background(255)
    frameRate(1000)
def draw():
    global tx
    background(255)
    fill(0)
    textSize(30)
    text(tx,100,100)
    rect(150,150,100,100)
def mouseClicked():
    global tx
    if mouseX > 150 and mouseX < 250 and mouseY > 150 and mouseY < 250:
        tx=tx+1
