bg=255
x=150
y=150
def setup():
    size(1000,600)
    background(0)
def draw():
    global bg
    rect(x,y,100,100)
    stroke(bg)
    strokeWeight(10)
    if mousePressed == True:
            fill(200,100,50)
            line(mouseX,mouseY,pmouseX,pmouseY)
def mouseClicked():
    global bg
    if mouseX > 150 and mouseX < 350 and mouseY > 150 and mouseY < 250:
        bg=100
