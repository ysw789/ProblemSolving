# target이 동전(i)보다 작다면 그 값은 아예 만들수가 없기 때문에 즉각 종료시킨다.
# 반대로 생각하면 쉬운 문제(너무 깊게 생각하지 말자!)

# 동전의 갯수
n = int(input())

# 갖고 있는 동전들
data = list(map(int, input().split()))
data.sort()

target = 1
for i in data:
    # 만들 수 없는 금액을 찾았을 경우 반복 종료
    if target < i:
        break
    target += i
    
print(target)
