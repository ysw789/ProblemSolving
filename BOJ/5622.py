# 숫자 1을 걸려면 2초가 필요하다
# (한 칸당 1초)

dial = [[2],                      # 1
        [3, 'A', 'B', 'C'],       # 2
        [4, 'D', 'E', 'F'],       # 3
        [5, 'G', 'H', 'I'],       # 4
        [6, 'J', 'K', 'L'],       # 5
        [7, 'M', 'N', 'O'],       # 6
        [8, 'P', 'Q', 'R', 'S'],  # 7
        [9, 'T', 'U', 'V'],       # 8
        [10, 'W', 'X', 'Y', 'Z'], # 9
        [11]]                     # 0

data = input()
cnt = 0

for i in data:
    for j in range(len(dial)):
        if i in dial[j]:
            cnt += dial[j][0]
            
print(cnt)
