nums=[1,0,-1,0,-2,2]
res=[]
for i in range(len(nums)):
   sum=-1
   for j in range(i+1,3):
      sum+=arr[j]
   if sum==0:
      res+=a.copy(i,j)
