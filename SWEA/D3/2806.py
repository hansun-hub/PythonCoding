
def is_promising(x):
    for i in range(x):
        print(str(i) + ": is_promising문 i의 값")
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    print("return true 됨")
    return True

def n_queens(x):
    print("n_queens"+str(x)+"호출")
    global ans
    #만약 마지막 행까지 다 넣어줬다면? N개의 퀸을 다 소진한 것!
    if x == n:
        ans += 1
        return
    else:
        #x가 행이라면, i는 열이다.
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            print(str(i)+": else문 i(열)의 값")
            row[x] = i
            #[x, i]에 퀸을 놓아도 되냐 검사하겠음
            if is_promising(x):

                #그 다음 행 검사
                n_queens(x + 1)

t = int(input())
for tc in range(1,t+1):
    n=int(input())
    ans = 0
    #한 행에 하나씩 퀸을 넣어줘야함
    row = [0] * n
    n_queens(0)
    print(f'#{tc} {ans}')