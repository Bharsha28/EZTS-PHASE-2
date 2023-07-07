n=int(input())
l=[]
for i in range(n):
    n=int(input())
    l.append(n)
print("original list",l)
for i in range(n-1):
    swap=False
    for j in range(n-i-1):
        if(l[j]>l[j+1]):
            swap=True
            l[j],l[j+1]=l[j+1],l[j]
    if swap==False:
      break
print(i)
print("\nsorted list",l)