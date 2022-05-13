'''
numlist = [1, 3, 2, 10, 12, 11, 15]

def print_even():
    for i in numlist:
        if i % 2 == 0:
            print(i)

print_even()
'''

'''
def make_list(str):
    tmp = []
    for c in str:
        tmp.append(c)
    return tmp

print(make_list("abcd"))
'''

icecream = {'탱크보이': [1200, 5], '폴라포': [1200, 2], '빵빠레': [1800, 3], '월드콘': [1500, 6], '메로나': [1000, 1]}

def sum_value():
    total = 0
    tmp = []
    for key, value in icecream.items():
        total += value[0] * value[1]
        if value[1] <= 3:
            tmp.append(key)
    print(total)
    return tmp

print(sum_value())