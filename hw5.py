#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 사용자 정의 함수
def read_single_digit(s) :
    if s == 1 :
        return '일'
    elif s == 2 :
        return '이'
    elif s == 3 :
        return '삼'
    elif s == 4 :
        return '사'
    elif s == 5 :
        return '오'
    elif s == 6 :
        return '육'
    elif s == 7 :
        return '칠'
    elif s == 8 :
        return '팔'
    elif s == 9 :
        return '구'
    elif s == 0 :
        return '영'
    
def red_number(n) :
    nn = n
    n100 = nn // 100
    nn = nn - 100*n100
    n10 = nn // 10
    nn = nn - 10*n10
    n1 = nn
    
    k1 = read_single_digit(n100)
    k2 = read_single_digit(n10)
    k3 = read_single_digit(n1)
    
    k = f'{k1} {k2} {k3}'
    return k

# 주 프로그램부
num = int(input('세 자리 정수 입력: '))
kk = red_number(num)
print(kk)


# In[ ]:





# In[ ]:




