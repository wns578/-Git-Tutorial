#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area():
    S = 3.14*r*r
    return S

r = get_radius('넓이를 구하고자 하는 원의 반지름은?')
S = get_circle_area()
print('반지름 ',r,'인 원의 넓이 = ',3.14,' x ',r,' x ',r,' = ',S,sep = '')


# In[ ]:




