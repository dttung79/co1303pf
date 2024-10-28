import turtle as t

size = int(input('Enter size: '))
angle = 144

for _ in range(5):
    t.forward(size)
    t.right(angle)

t.exitonclick()