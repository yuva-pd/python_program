a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
c=0
x=0
if a[0]>b[0]:
    c+=1
elif a[0]<b[0]:
    x+=1
if a[1]>b[1]:
    c+=1
elif a[1]<b[1]:
    x+=1
if a[2]>b[2]:
    c+=1
elif a[2]<b[2]:
    x+=1
print(c,x)
    


