m=int(input("Enter no of minutes:"))
if 0<= m <=1000:
   print("No of seconds:", m*60)
[24bcs044@mepcolinux e1]$cat salary.py
s=int(input("Enter basic salary of employee:"))
hra=0.20*s
da=0.1*s
if 5000<=s<=50000:
   print("Gross salary:",hra+da+s)
