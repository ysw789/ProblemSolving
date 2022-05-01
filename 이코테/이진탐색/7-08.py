# Binary Search
# p.205

# 떡의 개수 n, 손님이 요청한 떡의 길이 m 입력
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while start <= end:
    total= 0
    mid = (start + end) // 2
    for x in array:
        if x > mid: # 잘랐을 때의 떡의 양 계산
            total += x - mid
    # 떡의 양이 부족할 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분할 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1
        
print(result)

# 결과값은 'm이 되기 위한 최적의 중간점'이기 때문에 잘랐을 때 정확히 m의 길이가 안 나올 수 있다.
