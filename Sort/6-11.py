# Sort
# p.181

# 입력될 데이터의 개수 n
n = int(input())

# 데이터가 입력될 리스트 n
array = []
for _ in range(n):
    # 공백으로 구분하여 이름, 성적 입력받음
    input_data = input().split()
    # 이름은 문자열 그대로, 성적은 정수형으로 변환하여 리스트에 입력
    array.append((input_data[0], int(input_data[1])))
    
# key를 이용해 학생 성적을 기준으로 정렬
array = sorted(array, key = lambda student: student[1])

for student in array:
    print(student[0], end=' ')
