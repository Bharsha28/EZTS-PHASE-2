n=int(input())
l=[]
for i in range(n):
    n=int(input())
    l.append(n)
print("original list:",l)
def merge(l,left,mid,right):
       left=l[left:mid+1]
       right=l[mid+1:right+1]
       left_index=0
       right_index=0
       ind=left
       while(left_index <len(left) and right_index<len(right)):
           if(left[left_index]<right[right_index]):
               l[ind]=left[left_index]
               left_index+=1
           else:
                l[ind]=right[right_ind]
                right_index+=1
       while(right_index <len(right)):
            l[ind]=right[right_index]
            right_index+=1
            ind+=1
       while(left_index <len(left)):
            l[ind]=left[left_index]
            left_index+=1
            ind+=1
def dividing(l,start,end):
     if len(l)==1:
         return 
     mid=start+end//2
     dividing(l,start,mid)
     dividing(l,mid+1,end)
     merge(l,start,mid,end)
res=merge(l)
print("sorted list",res)