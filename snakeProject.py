
#part 1
import turtle
import random

turtle.tracer(1,0)

size_x=800
size_y=500
turtle.setup(size_x,size_y)

turtle.penup()

square_size = 20
start_length = 6
time_step = 100

pos_list = []
stamp_list = []
food_pos_list = []
food_stamp_list = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos)
    var = snake.stamp()
    stamp_list.append(var)


for bunny in range(start_length):
    x_pos = snake.xcor()
    y_pos = snake.ycor()

    x_pos+= square_size

    snake.goto(x_pos,y_pos)

    new_stamp()
    
#part 2
def remove_tail():
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

snake.direction = "Up"
def up():
    snake.direction="Up"
    print("You pressed the up key!")

turtle.onkeypress(up,"Up")
# part 3
up_edge = 250
down_edge = -250
right_edge = 400
left_edge = -400


#part 2
def down():
    snake.direction="Down"
    print("You pressed the down key!")

turtle.onkeypress(down,"Down")

def right():
    snake.direction="Right"
    print("You pressed the right key!")

turtle.onkeypress(right,"Right")

def left():
    snake.direction="Left"
    print("You pressed the left key!")

turtle.onkeypress(left,"Left")
turtle.listen()
#part 5
##time_step_2 = 10
##def new_stamp_2():
##    random_y=random.randint(down_edge , up_edge)
##    random_x=random.randint(left_edge,right_edge)
##    food_pos = (random_x,random_y)
##    return food_pos
##    
##
##random_y=random.randint(down_edge , up_edge)
##random_x=random.randint(left_edge,right_edge)
##food_pos=(random_x,random_y)

turtle.register_shape("donut2.gif")
food = turtle.clone()
food.shape("donut2.gif")
food_pos_list = [(100,100),(-100,100),(100,-100),(-100,-100)]
food_stamp_list = []
for this_food_pos in food_pos_list:
    food.goto(this_food_pos[0],this_food_pos[1])
    var2 = food.stamp()
    food_stamp_list.append(var2)

 
def make_food():
    min_x = -int(size_x/2/square_size)+1
    max_x = int(size_x/2/square_size)-1
    min_y = -int(size_y/2/square_size)+1
    max_y = int(size_y/2/square_size)-1

    food_x = random.randint(min_x,max_x)*square_size
    food_y = random.randint(min_y,max_y)*square_size

    food.goto(food_x,food_y)
    food.stamp()
        
    food_pos_list.append(food.pos())
    food_stamp_list.append(food.stamp())
#part 2
def move_snake():
    my_pos = snake.pos()


    if snake.pos() in pos_list[:-1]:
       print("Game Over!!!")
       quit()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
#part 3
    if x_pos >= right_edge:
        print("Game Over!!!")
        quit()
    elif x_pos <= left_edge:
        print("Game Over!!!")
        quit()
    elif y_pos >= up_edge:
        print("Game Over!!!")
        quit()
    elif y_pos <= down_edge:
        print("Game Over!!!")
        quit()
#part 2
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + square_size)
    elif snake.direction == "Down":
        snake.goto(x_pos, y_pos - square_size)
    elif snake.direction == "Right":
        snake.goto(x_pos + square_size, y_pos)
    elif snake.direction == "Left":
        snake.goto(x_pos - square_size, y_pos)
    new_stamp()
    
    ####rememeber it for part 5
    if snake.pos() in food_pos_list:
        food_index=food_pos_list.index(snake.pos())
        food.clearstamp(food_stamp_list[food_index])
        food_pos_list.pop(food_index)
        food_stamp_list.pop(food_index)
        print("You have eaten the food!")
    else:
        remove_tail()
    

    #####useful for part 8!!!!!!      
    if len(food_stamp_list) <= 6:
        make_food()
    turtle.ontimer(move_snake,time_step)
move_snake()
turtle.mainloop()
#Part 4
# remove move_snake from "up","down","right","left"


