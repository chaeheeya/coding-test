N, K = map(int, input().split(' '))
tems = list(map(int, input().split(' ')))
# print(tems)

current = sum(tems[:K])
max_num = current

for idx in range(1, N-K+1):
    temp = current-tems[idx-1]+tems[idx+K-1]
    current = temp
    max_num = max(max_num, temp)
    # print(max_num, temp)
print(max_num)