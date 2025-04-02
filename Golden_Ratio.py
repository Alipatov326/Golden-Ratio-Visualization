from turtle import*
speed(5)
golden_num = [1, 1]
inp_num = int(input("Enter the number of squares you want to see: "))
for i in range(inp_num + 2):
    golden_num.append(max(golden_num) + golden_num[i])
def square(side_length):

    for i in range(4):

        forward(side_length)
        right(90)


num_sq = len(golden_num)

factor = 3
penup()
goto(50, 50)
pendown()

# Draws squares
for i in range(num_sq):

    square(factor * golden_num[i])
    penup()
    forward(factor * golden_num[i])
    right(90)
    forward(factor * golden_num[i])
    pendown()

penup()
goto(50, 50)
setheading(0)
pencolor('red')
pensize(3)
pendown()

# Draws red spiral
for i in range(num_sq):

    circle(-factor * golden_num[i], 90)

exitonclick()
