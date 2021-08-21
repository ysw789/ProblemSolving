# Implementation
# p.117

# 체스판 말은 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
# 말은 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다
#   1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
#   2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
# 말의 위치가 주어졌을 때 말이 이동할 수 있는 경우의 수를 구하시오.
# 열은 a~h, 행은 1~8로 나타냄

input_data = input()
row = int(input_data[1])
# 열은 알파벳으로 입력되기 때문에 문자의 순번을 숫자로 변환해야 함
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 말이 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 정원 안에 있는지 여부 확인
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
    
print(result)
