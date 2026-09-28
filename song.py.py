n=int(input("enter your num:"))
data=[]
for i in range(n):
    value=int(input("enter your value:"))
    data.append(value)

print("Sorted data:",sorted(data))