#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 연습문제 9.4

# 주 프로그램부

shopping_bag = {} #장바구니
print('[구입]')
while True:
    item = input('상품명? ')     # item = 상품 이름을 입력받기
    if item == '' :
        break                    # item이 빈 문자열이면 루프 빠져 나가기
    amount = int(input('수량은? '))
    shopping_bag[item] = amount    # item amount개를 장바구니에 추가
    print(f'장바구니에 {item} {amount}개가 담겼습니다.')
    print()
    
print()
print(f'>>> 장바구니 보기: {shopping_bag}')
# 장바구니의 모든 상품 이름 출력

print()
print('[검색]')
q = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{q}은(는) {shopping_bag[q]}개 담겨 있습니다.')


# In[ ]:




