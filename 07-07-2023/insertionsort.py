n=int(input())
l=[]
for i in range(n):
    n=int(input())
    l.append(n)
print("original list:",l)
for i in range(1,len(l)):
    j=i
    while l[j-1]>l[j] and j>0:
          l[j-1],l[j]=l[j],l[j-1]
          j-=1
print("\nsorted list:",l)

