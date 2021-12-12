bg=0
def setup():
    size(600,400)
    frameRate(10)
def draw():
    global bg
    background(bg)
    stroke(random(0,255),random(0,255),random(0,255))
    line(random(0,600),random(0,400),20,30)
    stroke(0)
    ellipse(400,350,70,70)
def mouseClicked():
    global bg
    xDif = 400 - mouseX
    yDif = 350 - mouseY
    strokeWeight(20)
    fill(200,100,200)
