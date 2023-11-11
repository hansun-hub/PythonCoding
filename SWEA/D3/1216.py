#D3- 1216. 회문2
#M:회문길이, arr:리스트
#회문 있으면 True, 없으면 False
def palindrome(M,arr):
    for i in range(100):
        #가로회문
        for j in range(0,100-M+1):
            #구간 M에서 양 끝 값이 같을 때만 안쪽 확인
            # print("if문")
            # print('arr['+str(i)+']['+str(j)+'] == arr['+str(i)+']['+str(j)+'+'+str(M)+'-1]')
            if arr[i][j] == arr[i][j+M-1]:
                #안쪽확인
                #다르면 멈추기
                for k in range(1,M//2):
                    if arr[i][j+k] != arr[i][j+M-1-k]:
                        break
                else:
                    return True

        #세로회문
        for j in range(0,100-M+1):
            if arr[j][i] == arr[j+M-1][i]:
                for k in range(1,M//2):
                    if arr[j+k][i] != arr[j+M-1-k][i]:
                        break
                else:
                    return True
    return False

t=10
for tc in range(1,t+1):
    n=int(input())
    arr = [list(input()) for _ in range(100)]

    #M:회문의 길이
    for M in range(100,-1,-1):
        if palindrome(M,arr):
            print(f'#{tc} {M}')
            break