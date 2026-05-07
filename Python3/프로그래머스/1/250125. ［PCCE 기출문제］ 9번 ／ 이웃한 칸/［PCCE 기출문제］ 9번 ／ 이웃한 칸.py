def solution(board, h, w):
    n = len(board)
    count = 0
    dh = [0, 1, -1, 0] #오왼
    dw = [1, 0, 0, -1] #상하
    for i in range(0,4):
        h_check , w_check = h + dh[i], w +dw[i]
        if 0 <= h_check < n and 0 <= w_check < n: #범위 안에 있을 떄
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count