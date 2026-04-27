t=int(input("Enter the no of testcases:"))
for i in range(0,n-1):
   X=int(input("Enter the amount:"))
   s=input("Enter the sequence of wins:")
   n=len(s)
   c1=0
   c2=0
   c3=0
   for j in range(0,n-1):
      if 'C' in s:
         c1=c1+1
      elif 'N' in s:
         c2++
      else:
         c3++
   if(c1>c2):
      print("Chandhru winner:",60*X)
   elif(c1=c2):
      print("Total draw:",55*X,45*X)
