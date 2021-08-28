# Dynamic Programming
# p.212

# 메모이제이션 기법을 이용한 피보나치 수열 구현 코드(재귀적)

# 구하고자 하는 피보나치 수열의 n번째 수
n = int(input())

# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

# 피모나치 수열을 재귀함수로 구현(Bottom-Down)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(n))
