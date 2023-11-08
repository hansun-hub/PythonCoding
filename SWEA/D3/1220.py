#swea. D3- 1220
for tc in range(1, 11):
    n = int(input())
    mag = [list(map(int, input().split())) for _ in range(n)]  # 1: N, 2: S

    total_res = 0
    for i in range(n):
        flag = 0
        for j in range(n):
            if mag[j][i] == 1:
                flag = 1
            elif mag[j][i] == 2:
                if flag:
                    total_res += 1
                    flag = 0

    print(f'#{tc} {total_res}')