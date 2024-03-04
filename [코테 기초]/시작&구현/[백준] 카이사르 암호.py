alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

arr = input()
result=[]
for i in arr:
    j=alph.index(i)
    j=j-3
    result.append(alph[j])
print("".join(result))
