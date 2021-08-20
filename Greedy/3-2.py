# Greedy
# p.92

# 배열의 크기 n, 수열의 길이 m, 가장 큰 수가 연속으로 더해지는 횟수 k

# n, m, k를 공백으로 구분하여 입력받음
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받아 리스트 형식으로 변환
data = list(map(int, input().split()))

data.sort() # 리스트 정렬 (오름차)
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

# count = 가장 큰 수가 더해지는 횟수
# 반복되는 수열의 길이는 (k + 1)을 통해 알 수 있음
count = int(m / (k + 1)) * k
count += m % (k + 1) # m을 (k+1)로 나눈 나머지 만큼 가장 큰 수를 추가로 더함

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기
# 수열의 길이 - 가장 큰 수가 더해지는 횟수 = 두번째로 큰 수가 더해지는 횟수

print(result)
