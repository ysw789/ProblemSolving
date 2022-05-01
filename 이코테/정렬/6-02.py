# Sort
# p.164

# 삽입정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 첫 번째 데이터는 정렬되어 있다는 가정
    for j in range(i, 0, -1): # 앞에 위치한 데이터들과 비교하기 위해 1씩 감소
        if array[j] < array[j - 1]: 
            array[j], array[j - 1] = array[j - 1], array[j] # 스왑
        else:
            break
        
print(array)
