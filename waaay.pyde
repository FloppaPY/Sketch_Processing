x=0
y=0
o=0
g=2
k=3
x1=500
y1=300
def setup():
    size(1000,600)
    background(100)
    frameRate(random(100,200))
def draw():
    global o,g,k,x1,y1,x,y
    rotate(radians(o))
    translate(x1,y1)
    if mousePressed == True:
        fill(random(0,255),random(0,255),random(0,255))
        rect(x,y,100,50)
        x1=x1+k
        y1=y1+g
        if x1>975:
            k=-3
        if y1<25:
            g=2
        if x1<25:
            k=3
        if y1>575:
            g=-2
