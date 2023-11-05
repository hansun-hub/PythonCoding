#swea D3 - 1215.회문 1

for tc in range(1,11):
    #palindrome 의 길이 입력
    p=int(input())
    n=8
    arr = [list(input()) for _ in range(n)]
    cnt=0

    #가로일 때
    for i in range(0,n):
        for j in range(0,n-p+1):
            if arr[i][j:j+p] == arr[i][j:j+p][::-1]:
                cnt+=1
    #세로일 때
    for j in range(0,n):
        for i in range(0,n-p+1):
            #세로 문장을 확인하기 위해 char 변수 생성 및 초기화
            char = ''
            #i번쨰 행부터 회문의 길이만큼 문자열을 char 변수에 저장
            for ci in range(i,i+p):
                char += arr[ci][j]
            #char 문장과 그 역순 문장이 같으면 회문이므로, cnt에 1을 더해준다
            if char == char[::-1]:
                cnt+=1

    print(f'#{tc} {cnt}')
