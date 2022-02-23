list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

for i in range(2): #2행
    for j in range(4): #4열
        print(list_a[i][j] * list_b[i][j])
