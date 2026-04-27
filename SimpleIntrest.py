p=int(input("Enter principal amount:"))
r=float(input("Enter interest rate:"))
t=float(input("enter time period:"))
if(1<=p<=100000 and 1<=r<=20 and 1<=t<=10):
        print("Simple interest:",(p*r*t)/10)
