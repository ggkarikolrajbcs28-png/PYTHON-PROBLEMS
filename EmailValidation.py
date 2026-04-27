t=int(input("Enter the no of testcases:"))
for i in range(t):
   email = input("Enter the email to check: ")
   is_valid = True
   if "@" not in email:
      print("INVALID,The email must contain '@' symbol")
      is_valid = False
   if "." not in email:
      print("INVALID,The email must contain a domain dot (e.g., .com)")
      is_valid = False
   if email.count("@") > 1:
      print("INVALID,The email should not have more than one '@'")
      is_valid = False
   if " " in email:
      print("INVALID ,The email should not contain any spaces")
      is_valid = False
   if email.startswith("@") or email.endswith("."):
      print("INVALID,The email format is incomplete")
      is_valid = False
   if is_valid:
      print("The given email format is correct:", email)
