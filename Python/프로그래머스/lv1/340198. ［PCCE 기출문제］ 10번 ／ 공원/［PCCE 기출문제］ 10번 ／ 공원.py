def solution(mats, park):
    n = len(park)
    m = len(park[0])

    dp = [[0]*m for _ in range(n)]

    max_size = 0

    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1": #-1이 아닌 곳에는 dp가 0 => 정사각형을 만들수없기때문
                if i == 0 or j == 0: #가장자리에 있는 것들은 최대 크키가 1
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i-1][j], #위
                        dp[i][j-1], #왼쪽
                        dp[i-1][j-1] #대각선위
                    ) + 1

                max_size = max(max_size, dp[i][j])

    # mats 중에서 가능한 최대 찾기
    mats.sort(reverse=True)
    for size in mats:
        if size <= max_size:
            return size

    return -1