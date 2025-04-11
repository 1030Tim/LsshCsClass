n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(n-1-i):
        if (arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]


max_sorce = -10000
min_sorce = 100000
for i in range(n):
    if (arr[i]<60):
        max_sorce = arr[i]
    elif (arr[i]>=60):
        min_sorce = arr[i]
        break
if (max_sorce<0):
    print("best case")
else:
    print(max_sorce)

if (min_sorce>100):
    print("worst cast")
else:
    print(min_sorce)
