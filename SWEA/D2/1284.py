t=int(input())
for tc in range(1,t+1):
    P,Q,R,S,W = map(int,input().split())
    aCompany = P*W
    if W<=R:
        bCompany = Q
    else:
        bCompany = Q + (W-R)*S
    print(f'#{tc} {min(aCompany,bCompany)}')