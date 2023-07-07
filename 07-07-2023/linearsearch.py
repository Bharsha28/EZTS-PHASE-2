n=int(input())
l=[1,2,3,4,5]
c=0
for i in range(len(l)):
    if(n==l[i]):
        print("element found at:",i+1)
        c+=1
        break
if(c==1):
    print("Found")
else:
    print("not found")
    