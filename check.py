dict = {}

num = [1,2,3,4]
str_eng = ['a', 'b', 'c', 'd']
str_kor = ['가', '나', '다', '라']

for idx, key in enumerate(num):
    dict[idx] = []
    dict[idx].append(str_eng[idx])
    dict[idx].append(str_kor[idx])
    print(dict)
