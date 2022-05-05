# //와 %를 이용하여 자릿수를 구분하면 매우 쉽게 푸는 문제
# 괜히 str로 슬라이싱 하다가 머리 터짐

num = int(input())
origin_num = num # 원본 값 저장
count = 0

while True:
    a = num // 10 # 첫째 자리 수
    b = num % 10 # 둘째 자리 수
    c = (a + b) % 10 # 위 둘의 합
    num = (b * 10) + c # 새로 만들어진 수
    
    count += 1
    if num == origin_num: # 새로 만들어진 수와 원본 값이 같은지 확인
        break

print(count)
