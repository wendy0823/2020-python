a=input('請輸入(A,B,C,D,其他)')

if a in ['A','B']:
    print('年終六個月')

elif a in ['C','D']:
    print('年終四個月')

elif a in ['E','F']:
    print('年終三個月')

elif a in ['其他']:
    print('年終兩個月')