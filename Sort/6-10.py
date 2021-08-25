# Sort
# p.178

# 입력받을 데이터의 개수 n
n = int(input())

# 데이터를 입력받을 리스트
array = []

# 데이터를 입력받아 리스트에 append
for _ in range(n):
    array.append(int(input()))
    
# 내림차순으로 리스트 정렬
array.sort(reverse = True)

# 출력
for i in array:
    print(i, end=' ')
