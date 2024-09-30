# Write a program to calculate area and perimeter of a rectangle.
# The program should ask the user to enter the length and width of the rectangle.
length = int(input('Enter rectangle length: '))
width = int(input('Enter rectangle width: '))

area = length * width
perimeter = 2 * (length + width)

print(f'Rectangle {length}x{width} has area {area} and perimeter {perimeter}')

# Calculate area and perimeter of a circle
r = int(input('Enter circle radius: '))

PI = 3.14
area = PI * r ** 2
perimeter = 2 * PI * r

print(f'Circle with radius {r} has area {area} and perimeter {perimeter}')

# Calculate area and perimeter of a triangle
a = int(input('Enter triangle side a: '))
b = int(input('Enter triangle side b: '))
c = int(input('Enter triangle side c: '))

perimeter = a + b + c
p = perimeter / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(f'Triangle with sides {a}, {b}, {c} has area {area} and perimeter {perimeter}')