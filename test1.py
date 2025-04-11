n = int(input())
arr = sorted(list(map(int,input().split())))

max_value = -10000
min_value = 10000

print(*arr)

for i in range(n):
    if (arr[i]<60):
        min_value = arr[i]
    elif (arr[i]>=60):
        max_value = arr[i]
        break

if (min_value > 100):
    print("best case")
else:
    print(min_value)

if (max_value < 0):
    print("worst case")
else:
    print(max_value)

