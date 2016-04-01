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

def kochflake(length, levels):
    if levels == 0:
        forward(length)
        return
    length /= 3.0
    kochflake(length, levels-1)
    left(60)
    kochflake(length, levels-1)
    right(120)
    kochflake(length, levels-1)
    left(60)
    kochflake(length, levels-1)
	
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
	
def pentaflake(length,level):
	if level == 0:
		pentagon(length)
		return
	length /= 3
	angle = 216
	pentaflake(length,level-1)
	right(angle)
	pentaflake(length,level-1)
	right(angle)
	pentaflake(length,level-1)
	right(angle)
	pentaflake(length,level-1)
	right(angle)
	pentaflake(length,level-1)
	
	penup()
	right(72)
	forward(length*4.25*(1/level))
	pendown()
	
    
turtle.speed(0)
#left(90)
tree(50)

#for i in range(3):
        #kochflake(300, 4)
        #right(120)
#sier(300,8)

# uhol v 5uholniku je 108
#def pentagon(length):
	#for i in range(0,4):
		#forward(length)
		#left(72)
	#forward(length)
	#back(length)
turtle.speed(0)
#pentaflake(300,3)










turtle.exitonclick()





































