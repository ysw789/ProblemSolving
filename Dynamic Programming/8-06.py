# Dynamic Programming
# p.222

# 개미들이 식량창고를 몰래 공격하려고 한다.
# 각 식량창고마다 정해진 양의 식량이 들어있다.
# 들키지 않으려면 최소한 한 칸 이상 떨어진 식량창고들을 약탈해야 한다.
# 이때 식량창고 n개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하시오.

# 식량 창고의 개수 n
n = int(input())

# 창고 속 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 계산된 결과를 저장하기 위한 DP 테이블
d = [0] * 100

# 다이나믹 프로그래밍 진행(Bottom-Up)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])
    
print(d[n - 1])
