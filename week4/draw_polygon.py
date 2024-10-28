import turtle as t

n = int(input('Enter n: '))
size = int(input('Enter size: '))
angle = 180 * (n - 2) / n

for i in range(n):
    t.forward(size)
    t.left(180 - angle)

t.exitonclick()