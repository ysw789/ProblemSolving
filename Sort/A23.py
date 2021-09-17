# 정렬 문제
# p.359

# 학생 수 n 입력받음
n = int(input())

# n명 학생의 이름, 국어, 영어, 수학점수를 한 줄씩 공백으로 구분하여 입력
students = []
for _ in range(n):
    students.append(input().split())
    
#   정렬 조건
#   1. 국어 점수 내림차순
#   2. 국어 점수가 같을 경우 영어 점수 오름차순
#   3. 영어 점수가 같을 경우 수학 점수 내림차순
#   4. 수학 점수가 같을 경우 이름 오름차순
students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬 후 학생 이름 출력
for student in students:
    print(student[0])
