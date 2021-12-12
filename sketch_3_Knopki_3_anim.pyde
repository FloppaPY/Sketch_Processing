bg=255
bk=255
x=150
y=150
angle = 1
red=random(0,50)
green=random(0,100)
blue=random(0,200)
def setup():
    size(1000,600)
    frameRate(100)
def draw():
    global x,y,bg,bk
    strokeWeight(3)
    stroke(random(0,255),random(0,255),random(0,255))
    fill(red,green,blue)
    rect(x,y,100,100)
    rect(100,50,100,50)
    rect(250,50,100,50)
    if mousePressed == True:
        if mouseX > 150 and mouseX < 250 and mouseY > 150 and mouseY < 250:
            global angle,bk
            background(bk)
            fill(random(0,255),random(0,255),random(0,255))
            translate(400,300)
            rotate(radians(angle))
            translate(120,120)
            ellipse(0,0,50,50)
            rect(0,0,30,55)
            angle+=4
        if mouseX > 100 and mouseX < 200 and mouseY > 50 and mouseY < 50+50:
            global bk
            background(bk)
            fill(random(100,255),random(55,255),random(22,155))
            translate(380,300)
            rotate(radians(angle))
            translate(120,120)
            ellipse(0,0,50,50)
            rect(0,0,20,55)
            angle-=4
        if mouseX > 250 and mouseX < 350 and mouseY > 50 and mouseY < 50+50:
            global bk
            background(bk)
            fill(random(100,255),random(55,255),random(22,155))
            translate(380,300)
            rotate(radians(angle))
            translate(120,120)
            ellipse(0,0,50,50)
            rect(0,0,20,55)
            angle-=20
