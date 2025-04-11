n = int(input())


arr = list(map(int,input().split()))

for i in range(n):
    for j in range(n-1-i):
        if (arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]

max_value = -1
min_value = -1
for i in range(n):
    if (arr[i]>=60 and max_value==-1):
        max_value = arr[i]
    elif (arr[i]<60):
        min_value = arr[i]


for i in range(n-1):
    print(arr[i],end=" ")
print(arr[-1])

if (min_value == -1):
    print("best case")
else:
    print(min_value)

if (max_value == -1):
    print("worst case")
else:
    print(max_value)
