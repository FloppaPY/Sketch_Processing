flr=240
flr2=17
flr3=17
flg=68
flg2=240
flg3=17
flw=17
flw2=240
flw3=197
def setup():
    size(1000,600)
    background(30)
    frameRate(50)
def draw():
    global flr,flr2,flr3,flg,flg2,flg3,flw,flw2,flw3
    strokeWeight(12)
    if key==CODED:
        if keyCode == UP:
            stroke(flg,flg2,flg3)
        if keyCode == SHIFT:
            stroke(flg,flg2,flg3)
        if keyCode == UP:
            stroke(flg,flg2,flg3)
    if mousePressed == True:
        stroke(flr,flr2,flr3)
        line(mouseX,mouseY,pmouseX,pmouseY)
