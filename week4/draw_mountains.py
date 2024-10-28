import turtle as t

n = int(input('Enter n: '))
size = int(input('Enter size: '))

for _ in range(n):
    t.left(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.left(60)

t.exitonclick()