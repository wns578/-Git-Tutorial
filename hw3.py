#!/usr/bin/env python
# coding: utf-8

# In[7]:


discount = 0

#사용자정의 함수부

def get_fixed_price(dp) :
    global discount
    result = dp / (100-discount) * 100
    return result
    
    

#주 프로그램부

discount = int(input('할인율은?'))
Adp = int(input('A 상품의 할인된 가격은?'))
Bdp = int(input('B 상품의 할인된 가격은?'))
Acp = int(get_fixed_price(Adp))
Bcp = int(get_fixed_price(Bdp))

#출력

print('A 상품의 정가는',Acp,'원')
print('B 상품의 정가는',Bcp,'원')


# In[14]:





# In[ ]:





# In[ ]:




