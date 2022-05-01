# Binary Search
# p.190

# 일반 반복문을 이용한 이진탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        # target을 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        
        # 중간점의 값 보다 target이 작을 경우, 중간점을 기준으로 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
            
        # 중간점의 값 보다 target이 클 경우, 중간점을 기준으로 오른쪽 확인
        else:
            start = mid + 1
    return None

# 원소의 개수 n과 찾고자 하는 문자열 target 입력받기
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다!')
else:
    print(result + 1)
