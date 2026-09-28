n = int(input("enter your num:"))
fibu=[0,1]
for i in range(2,n):
	fibu.append(fibu[i-1]+fibu[i-2])
print(fibu)