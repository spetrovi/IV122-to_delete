import sys , turtle

def forward(k):
  return turtle.forward(k)

def left(k):
  return turtle.left(k)

def right(k):
  return turtle.right(k)

def back(k):
  return turtle.back(k)

def penup():
  return turtle.penup()

def pendown():
  return turtle.pendown()

def done():
  return turtle.done()

def tree(length, min_length=1):
    forward(length)
    if length > min_length:
        left(45)
        tree(0.6*length, min_length)
        right(90)
        tree(0.6*length, min_length)
        left(45)
    back(length)


def kochside(length, levels):
    if levels == 0:
        forward(length)
        return
    length /= 3.0
    kochside(length, levels-1)
    left(60)
    kochside(length, levels-1)
    right(120)
    kochside(length, levels-1)
    left(60)
    kochside(length, levels-1)

def kochflake(level):
	for i in range(3):
        	kochside(100*level, level)
        	right(120)

def sier(length, level):
    if level == 1:
        for i in range(3):
            forward(length)
            left(120)
    else:
        sier(length/2, level-1)
        forward(length/2)
        sier(length/2, level-1)
        back(length/2)
        left(60)
        forward(length/2)
        right(60)
        sier(length/2, level-1)
        left(60)
        back(length/2)
        right(60)


def pent_side(length,level):
	if level == 0:
        	forward(length/5)
        	return
	length /= 5
	pent_side(length,level-1)
	right(72)
	pent_side(length,level-1)

	left(36)
	pent_side(length,level-1)
	penup()
	left(180)
	pent_side(length,level-1)
	right(180)
	pendown()
	
	#department of redundancy department
	right(144-36)
	pent_side(length,level-1)
	penup()
	left(180)
	pent_side(length,level-1)
	right(180)
	pendown()
	left(144-36)
	
	left(144-36)
	pent_side(length,level-1)
	right(72)
	pent_side(length,level-1)

def pentaflake(level):
	for i in range(5):
		pent_side(1000*level,level)
		right(72)

	

turtle.speed(0)
left(90)
tree(50)

penup()
back(200)
pendown()
pentaflake(3)
kochflake(4)

turtle.exitonclick()





































