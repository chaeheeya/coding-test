from itertools import permutations

def solution(k, dungeons):
    
    results = []
    # print(list(permutations(dungeons)))
    
    for ds in list(permutations(dungeons)):
        # print("ds: ", ds)
        power = k
        cnt = 0
        for d in ds:
            # print("d: ", d)
            if power >= d[0]:
                power -= d[1]
                cnt += 1
                # print("power, cnt: ", power, cnt)
        
        results.append(cnt)
        
        # print(results)
    
    
#     answer = -1
#     result = []
    
    
#     power, cnt = k, 0
#     for i in dungeons:
#         if power >= i[0]:
#             power -= i[1]
#             cnt += 1
#         else:
#             continue
        
#         print('idx1: ', i, power, result)
#         for j in dungeons:
#             print("i, j: ", i, j)
#             if i == j:
#                 continue
#             else:
#                 if power >= j[0]:
#                     power -= j[1]
#                     cnt +=1    
#                     print('idx2: ', j, power, result)
        
#         result.append(cnt)
#         cnt = 0
#         power = k
            
#         print(result)
    return max(results)