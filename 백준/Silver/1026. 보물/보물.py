N = int(input())
arr = []
for __ in range(2):
    arr.append(list(map(int, input().split())))

arr1 = arr[0]
arr1.sort()
arr2 = arr[1]
arr2.sort(reverse=True)


answer = 0
for i, j in zip(arr1, arr2):
    answer += (i * j)

print(answer)