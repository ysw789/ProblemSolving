# 짝수 정수를 절반으로 나누어
# 왼쪽 부분과 오른쪽 부분의 합이 서로 같은지만 확인하면 되기 때문에
# 쉽게 생각해서 풀 수 있다!

n = input() # n은 항상 짝수
m = len(n)
temp = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(m // 2):
    temp += int(n[i])
    
# 오른쪽 부분의 자릿수 합 빼기
for j in range(m // 2, m):
    temp -= int(n[j])
   
# 0일 경우 두 합이 같음
if temp == 0:
    print('LUCKY')
else:
    print('READY')
