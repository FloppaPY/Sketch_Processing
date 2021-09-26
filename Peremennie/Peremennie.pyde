x = 600
y = 425
xtr = 500
ytr = 425
xsize = 500
ysize = 325
#xel = 200
#yel = 150
def setup():
    size(1200,650)
    frameRate(1)
    stroke(200,200,50)
    strokeWeight(2)
def draw():
    global x,y,xel,yel
    #point(x,y)
    #stroke(203,250,5)
    #strokeWeight(5)
    #ellipse(500,425,xel,yel)
    fill(random(200,240),random(10,240),20)
    triangle(x,y,xtr,ytr,random(xsize,ysize),random(xsize,ysize))
    y+=1
