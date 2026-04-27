t = int(input("Enter no of test cased"))
for i in range(t):
    n = int(input())
    triangle = []
    for j in range(n):
        row = list(map(int, input().split()))
        triangle.append(row)
    for r in range(n - 2, -1, -1):
        for c in range(len(triangle[r])):
            left_below = triangle[r + 1][c]
            right_below = triangle[r + 1][c + 1]

            if left_below > right_below:
                triangle[r][c] = triangle[r][c] + left_below
            else:
                triangle[r][c] = triangle[r][c] + right_below

    print(triangle[0][0])
