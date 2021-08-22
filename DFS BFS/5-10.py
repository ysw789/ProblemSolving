# DFS
# p.151

# n*m크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1이다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하시오.

n, m = map(int, input().split())

# 얼음 틀의 모양 입력받음(2차원 리스트)
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들을 방문한다
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False # 틀 모양을 벗어날 경우 False
    if graph[x][y] == 0: # 해당 노드를 방문하지 않았는가?
        graph[x][y] = 1 # 방문 확인
        # 재귀적으로 상, 하, 좌, 우에 위치한 노드들 체크
        dfs(x-1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        return True
    return False
    
# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n): # 가로
    for j in range(m): # 세로
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            
print(result)
