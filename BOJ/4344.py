# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

c = int(input())

for i in range(c):
    data = list(map(int, input().split())) 
    # 리스트의 첫 데이터는 데이터의 개수를 가리키므로 슬라이싱을 통해 데이터를 구분한다
    avg = sum(data[1:]) / data[0]
    overavg = 0
    
    for score in data[1:]:
        if score > avg:
            overavg += 1
    
    result = (overavg / data[0]) * 100
    
    print(f'{result:.3f}%')
