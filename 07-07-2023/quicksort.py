n=int(input())
l=[]
for i in range(n):
    n=int(input())
    l.append(n)
print("original list:",l)
def quick_sort(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=[i for i in  l if  i<pivot ]
    right=[i for i in  l if  i>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
res=quick_sort(l)
print("sorted array",res)

    
