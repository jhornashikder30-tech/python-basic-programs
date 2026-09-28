a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
op=input()
if op=='+':
	print(a+b+c+d+e+f)
elif op=='-':
	print(a-b-c-d-e-f)
elif op=='*':
	print(a*b*c*d*e*f)
elif op=='/':
	if f!=0:
		print("error")
	else:
		print("invaible number")