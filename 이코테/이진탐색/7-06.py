# Binary Search
# p.199

# 7-05 예제를 계수 정렬 방법으로 푼 경우

n = int(input())
products = [0] * 1000001

for i in input().split():
    products[int(i)] = 1
    
m = int(input())
order = list(map(int, input().split()))

for i in order:
    if products[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
