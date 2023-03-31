#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 개념 확인 과제
# 사용자 정의 함수부

def draw_line_string(c) :
    
    num = int(c)
    rep_char('-',num+2)
    print(msg1)
    print(msg2)
    rep_char('-',num+2)

def rep_char(c,n) :
    
    print(c*n)

#주 프로그램부


name = input('Input his/her name: ')
msg1 = ' Hello ' + name + ', '
msg2 = ' Welcome to Seoul. '
nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)


draw_line_string(nstr)


# In[ ]:




