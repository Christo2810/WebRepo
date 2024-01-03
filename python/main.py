from graphics import rectangle, circle
from graphics.ThreeDGraphics import cuboid, sphere
#using rectange module
length =5
width=3
print("Area of a rectangle =", rectangle.area(length, width))
print("Area of a rectangle =", rectangle.perimeter(length, width))
#using circle module
radius=4
print("Area of the circle =", circle.area(radius))
print("Perimeter of the circle=", circle.perimeter(radius)) 
#using cuboid module
length=4
width=5
height=5
print("cuboid of surface area =", cuboid.surfacearea(length, width, height))
print("Volume of a cuboid =", cuboid.volume(length, width, height))
#using sphere module
radius=4
print("sphere of surface area =", sphere.sp(radius))
print("Volume of a sphere =", sphere.volume(radius))
