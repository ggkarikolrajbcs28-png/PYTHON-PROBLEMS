t = int(input("enter the no of testcases:"))
for _ in range(t):
    start_str = input()
    end_str = input()
    start_h = int(start_str.split()[1].split(":")[0])
    end_h = int(end_str.split()[1].split(":")[0])
    if end_h < start_h:
        print("INVALID")
    else:
        duration = end_h - start_h
        if duration > 5:
            duration = duration - 1

        print(duration)
