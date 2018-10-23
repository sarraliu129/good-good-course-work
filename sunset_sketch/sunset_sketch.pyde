# while loop
# increase variable
#use draw() for animation

cloud = 0
sun_and_colour = 0

def setup():
    size(640, 480)


def draw():
    global cloud
    global sun_and_colour
    noStroke()
   
    background(100 + sun_and_colour , 80 + sun_and_colour , 0)
    sun_and_colour += 0.5
    fill(255, 255, 0)
    ellipse(width/2, 350 - sun_and_colour , 70, 70)
         
        
    fill(0, 30, 179)
    rect(0, 350, 700 , 250)

    if cloud >= 640:
        cloud = 0
    cloud += 1
    fill(250, 250, 250)
    ellipse(cloud, height / 5, 50 , 50 )
    ellipse (cloud + 35, height / 5 , 70 , 50)
    ellipse (cloud - 35, height / 5 + 15, 65, 50 )
    ellipse (cloud - 10, height / 5 - 15, 65, 50 )
    ellipse (cloud, height / 5, 50, 50)
    
    
    
    
         

    
    
