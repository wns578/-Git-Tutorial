#!/usr/bin/env python
# coding: utf-8

# In[1]:


def exchange(ex):
    ex1 = ex
    n500 = ex1 // 500
    ex1 %= 500
    n100 = ex1 // 100
    ex1 %= 100
    n50 = ex1 // 50
    ex1 %= 50
    n10 = ex1 // 10
    
    # print출력문
    print('500원 동전의 개수:',n500)
    print('100원 동전의 개수:',n100)
    print('50원 동전의 개수:',n50)
    print('10원 동전의 개수:',n10)
    
    
def get_integer(prompt):
    n1 = int(input(prompt))
    return n1
    
number = get_integer('동전으로 교환하고자 하는 금액은?')
exchange(number)    


# In[ ]:




