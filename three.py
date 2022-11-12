ar = [2,3,4,5,7,7]
#we need to find tripplet a+b+c == target
target = 19

def triplet(ar,target):
  j=len(ar)-1;
  for i in range(0,len(ar)-2):
    for k in range(i,len(ar)-1):
      if ar[i]+ar[j]+ar[k]>target:
        j-=1
        print(j)
      elif ar[i]+ar[j]+ar[k]<target:
        k+=1
        print(k)
      else:
        return i,j,k

print(triplet(ar,target))
    