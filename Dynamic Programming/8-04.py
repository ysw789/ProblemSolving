# Dynamic Programming
# p.215

# 메모이제이션 기법을 이용한 피보나치 수열 구현 코드(반복적)

# 구하고자 하는 피보나치 수열의 n번째 수
n = int(input())

# 계산된 결과를 저장하기 위한 DP 테이블
d = [0] * 100

# 피보나치 수열의 첫 번째, 두 번째 수는 1
d[1] = 1
d[2] = 1

# 피보나치 수열을 반복문으로 구현(Bottom-Up)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
    
print(d[n])
