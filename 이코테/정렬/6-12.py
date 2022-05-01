# Sort
# p.183

# 배열의 길이 n, 바꿔치기 할 횟수 k를 공백으로 구분하여 입력받음
n, k = map(int, input().split())

# 각 리스트 a, b의 원소를 공백으로 구분하여 입력받음
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

a.sort() # a는 오름차순으로 정렬
b.sort(reverse = True) # b는 내림차순으로 정렬

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 스왑
        a[i], b[i] = b[i], a[i]
    else: # a의 원소가 b의 원소보다 크거나 같을 때, 반복문 탈출
        break
    
print(sum(a))
