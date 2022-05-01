# Greedy
# p.101

# n이 1이 될 때 까지 다음 연산을 반복 함. 
# 다만 2번 연산은 n이 k로 나누어 떨어질 때만 가능함.
#   1. n에서 1을 뺀다
#   2. n을 k로 나눈다

# n, k를 공백으로 구분하여 입력받음
n, k = map(int, input().split())
result = 0

# n이 k 이상일 경우 k로 계속 나누기
while n >= k:
    # n이 k로 나누어떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # n을 k로 나누기
    n //= k
    result += 1
    
# n이 더 이상 k로 나누어지지 않을 경우 1씩 빼기
while n > 1:
    n -= 1
    result += 1
    
print(result)

# 본 방식은 1씩 빼가며 계속 확인하는 방식으로, 
# 더 큰 정수가 입력 될 경우 매우 느리게 동작 할 것임.

# 예제 3-6 보기
