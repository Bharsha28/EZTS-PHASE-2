n=int(input())
l=[]
for i in range(n):
    n=int(input())
    l.append(n)
print("original list:",l)
for i in range(len(l)):
    swap=False
    min1=i
    for j in range(i+1,len(l)):
       if l[min1]>l[j]:
           min1=j#finding the min element index
    #swapping minimum and starting index
    l[i],l[min1]=l[min1],l[i]
    if swap==False:
      break
print("\nsorted list:",l)
