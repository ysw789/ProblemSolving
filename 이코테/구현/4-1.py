# Implementation
# p.112

# 여행자의 이동 계획(plans)에 따라 여행자를 이동시키시오.
# 다만 공간을 벗어날 경우 그 계획은 무시함.
# 최종 도착 위치 x, y를 구하시오.

n = int(input())  # 공간의 크기
plans = input().strip()  # 이동 계획
x, y = 1, 1  # 시작 지점

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']

for plan in plans:  # 이동 계획(plans)과 이동 방향 리스트(direction)을 하나씩 대조
    for i in range(len(direction)):
        if plan == direction[i]:
            # 이동 방향에 따라 x, y값 변화
            nx = x + dx[i]
            ny = y + dy[i]
    # n * n 공간을 벗어날 경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
    
print(x, y)
