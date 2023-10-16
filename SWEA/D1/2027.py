for i in range(5):
    str = ''
    for j in range(5):
        if i==j:
            str+='#'
        else:
            str+='+'
    print(str)