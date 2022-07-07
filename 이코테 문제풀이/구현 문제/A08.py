s = input()

result = []
sumnum = 0

for i in s:
    # 알파벳인 경우 리스트에 삽입
    if i.isalpha():
        result.append(i)
    # 숫자일 경우 따로 더하기
    else:
        sumnum += int(i)

# 알파벳 오름차순 정렬
result.sort()

# 숫자가 하나라도 있을 경우 리스트의 마지막에 삽입
if sumnum != 0:
    result.append(str(sumnum))
    
print(''.join(result))
