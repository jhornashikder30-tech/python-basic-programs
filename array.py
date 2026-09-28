import cmath
a =float(input("enter a"))
b =float(input("enter b"))
c =float(input("enter c"))
d=((b*b)-4*a*c)
x1=(-b+cmath.sqrt(d))
x2=(-b-cmath.sqrt(d))
print(x1,x2)