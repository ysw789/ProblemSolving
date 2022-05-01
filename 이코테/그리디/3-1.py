# Greedy
# p.90

# - 거스름돈
#   가장 큰 화폐 단위부터 거슬러 줘야 함
#   거슬러 줘야 할 동전의 최소 개수를 구하시오

n = int(input())
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 동전으로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin # 해당 동전으로 거슬러 준 후 나머지 금액

print(count)
