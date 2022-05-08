data = input()

# 첫 번째 문자를 숫자형으로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에 하나라도 0 혹은 1인 경우 더하기 수행
    if int(data[i]) <= 1 or result <= 1:
        result += int(data[i])
    # 이외에는 곱하기 수행
    else:
        result *= int(data[i])
        
print(result)
