t=int(input("Enter no.of test cases: "))
for i in range(t):
   a=int(input("suresh coins: "))
   b=int(input("sundar coins: "))
   c=int(input("raja donation: "))
   d=int(input("suresh donation: "))
   print("Game 1")
   if a < b:
      print("Sundar Wins")
      a=a+c
   else:
      print("Suresh Wins")
      b=b+c
   print("Game 2")
   if a < b:
      print("Sundar Wins")
      a=a+d
   else:
      print("Suresh Wins")
      b=b+d
   if a < b:
      print("Final Winner: S")
   else:
      print("Final Winner: N")
