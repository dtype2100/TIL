board = []
for _ in range(8):
    board.append(list(map(str, list(input()))))

ans = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: #하얀칸일 경우
            if board[i][j] == 'F': #F있을 경우
                ans += 1
print(ans)