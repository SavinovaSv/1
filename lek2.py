import math
x=float(input("введите х:"))
y=float(input("введите у:"))
r=float(input("введите радиус круга:"))
xc=float(input("введите координату центра круга по оси ох:"))
yc=float(input("введите координату центра круга по оси оу:"))

if (((x-xc)**2+(y-yc)**2) < r*r):
    print("точка попадает в круг")
else:
    print("точка не попадает в круг")
    
