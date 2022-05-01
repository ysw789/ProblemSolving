# Implementation
# p. 114

# 정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초 까지의
# 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하라.

n = int(input())

count = 0

# n시 59분 59초 까지
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # 시각 중에 3이 하나라도 포함되는가?
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)
