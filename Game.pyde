tx=0
ttx=30
def setup():
    size(1000,600)
    frameRate(500)
def draw():
    global tx,ttx
    push()
    frameRate(500)
    background(150)
    textSize(40)
    text(tx,20,60)
    rect(150,150,100,100)
    text(ttx,500,60)
    frameRate(1)
    ttx=ttx-1
    if tx>29:
        background(55,240,19)
        textSize(150)
        text(u"Победаа!!!",110,300)
    if ttx<0:
        background(237,7,7)
        textSize(150)
        text(u"Проигрыш",110,300)
def mouseClicked():
    global tx
    if mouseX > 150 and mouseX < 250 and mouseY > 150 and mouseY < 250:
        tx=tx+1
