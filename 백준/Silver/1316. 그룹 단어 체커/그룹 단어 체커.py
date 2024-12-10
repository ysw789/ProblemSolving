n = int(input())
group_word = 0

for _ in range(n):
    word = input()
    err = 0
    for i in range(len(word) - 1):
        if word[i] != word[i+1]: # 연속된 문자가 일치하지 않다면
            new_word = word[i+1:] # 현재 문자를 제외한 나머지를 슬라이싱
            if new_word.count(word[i]) > 0: # 슬라이싱 한 문자열에 이 단어가 남아있는지 확인
                err += 1 # 남아있다면 그룹 단어가 아니므로 err
    if err == 0:
        group_word += 1
            
print(group_word)