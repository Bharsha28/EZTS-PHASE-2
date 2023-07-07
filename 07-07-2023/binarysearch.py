key=int(input())
l=[3,1,44,5,6,88]
l=sorted(l)
m=l[0]
n=len(l)-1
c=0
while(m<=n):
    mid=(m+n)//2
    if l[mid]==key:
        print("element found at:",mid)
        break
    elif(n<l[mid]):
        n=mid-1
    elif n>l[mid]:
        m=mid+1
if(c==0):
    print(" not Found")
    
