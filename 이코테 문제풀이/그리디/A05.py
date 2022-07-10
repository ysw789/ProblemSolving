n, m = map(int, input().split()) # 볼링공의 최대 무게는 10kg이다 (m <= 10)
data = list(map(int, input().split())) # 볼링공 n개

array = [0] * 11 # 1~10kg까지의 볼링공 종류를 담을 수 있는 리스트
for x in data:
    # 각 무게에 해당하는 볼링공의 갯수 카운트
    array[x] += 1
    
result = 0
# 1부터 m(최대 무게)까지의 각 무게에 대하여 처리
for i in range(m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 갯수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기
    
print(result)
