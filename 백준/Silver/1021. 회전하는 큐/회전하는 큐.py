from collections import deque

N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
targets = list(map(int, input().split()))


answer = 0
for t in targets:
    idx = nums.index(t)
    temp = []

    if idx == 0:
        if len(nums) > 0:
            nums = nums[1:]
        else:
            break
    else:
        if idx <= len(nums)-idx:
            answer += idx
        else:
            answer += (len(nums)-idx)

        temp.extend(list(nums)[idx+1:])
        temp.extend(list(nums)[:idx])
        nums = temp
        # print('new nums: ', nums)
        # print('answer: ', answer)

print(answer)
