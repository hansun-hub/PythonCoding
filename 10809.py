tmp = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet=list(alphabet)

lst=[-1 for i in range(26)]
num=-1
for i in tmp:
    num+=1
    if i in alphabet:
        n=alphabet.index(i)
        if lst[n]==-1:
            lst[n]=num
    
for j in lst:
    print(j,end=' ')
