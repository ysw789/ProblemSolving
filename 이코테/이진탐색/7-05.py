# Binary Search
# p.198

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 가게의 부품 개수 n 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
products = list(map(int, input().split()))
products.sort() # 이진탐색을 수행하기 위해 리스트 정렬

# 손님이 요청한 부품 개수 m 입력
m = int(input())
# 손님이 요청한 전체 부품 번호를 공백으로 구분하여 입력
order = list(map(int, input().split()))

# 손님이 요청한 부품 번호를 하나씩 확인
for i in order:
    result = binary_search(products, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
