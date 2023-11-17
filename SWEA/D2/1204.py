#1204. 최빈수 구하기
#11/17
t=int(input())
for tc in range(1,t+1):
    n=int(input())
    grades = list(map(int,input().split()))
    freq = [0]*101
    mode=0 #최빈값
    for grade in grades:
        freq[grade]+=1
        if freq[grade] >= freq[mode]:mode = grade
    print(f'#{tc} {mode}')