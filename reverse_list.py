a = [1,2,3,4,5]
size=len(a)
print(int(size/2))
for i,j in zip(range(0,int(size/2),1),range(size-1,0,-1)):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

print(a)
