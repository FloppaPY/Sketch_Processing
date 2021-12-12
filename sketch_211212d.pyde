rct=50
rct1=50
rct2=50
rct3=50
def setup():
    size(1000,600)
    background(30)
    frameRate(50)
def draw():
    global rct,rct1,rct2,rct3
    background(20,54,205)
    fill(2,51,59)
    rect(rct,rct1,rct2,rct3)
    if key==CODED:
        if keyCode == UP:
            rct1=rct1-5
        if keyCode == DOWN:
            rct1=rct1+5
        if keyCode == LEFT:
            rct=rct-5
        if keyCode == RIGHT:
            rct=rct+5
