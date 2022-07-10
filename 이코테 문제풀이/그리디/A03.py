s = input() # s < 1,000,000
count0 = 0
count1 = 0

# 첫 번째 원소부터 처리한다
if s[0] == '1':
    count0 += 1
else:
    count1 += 1
    
# 두 번째 원소부터 확인해가며 처리한다
for i in range(len(s) - 1):
    # 현재 원소와 다음 원소의 값이 다를 경우
    if s[i] != s[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if s[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1
        
# 더 적은 변경 횟수를 가지는 경우를 출력
print(min(count0, count1))
