#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 연습문제 10.6

# 사용자 정의 함수부
def buy(shopping_bag) :
    print('[구입]')
    item = input('상품명? ')          # item = 상품 이름을 입력받기
    if item == '' :
        return False                 # item이 빈 문자열이면 False 반환
    amount = int(input('수량은? '))
    shopping_bag[item] = amount       # item amount개를 장바구니에 추가
    print(f'장바구니에 {item} {amount}개가 담겼습니다.')
    print()
    
def show(shopping_bag) :
    print()
    print(f'>>> 장바구니 보기: {shopping_bag}')
    # 장바구니의 모든 상품 이름 출력 (리스트 이름 사용)
    
def find(shopping_bag) :
    print()
    print('[검색]')
    q = input('장바구니에서 확인하고자 하는 상품은? ')
    print(f'{q}은(는) {shopping_bag[q]}개 담겨 있습니다.')
    
    

# 주 프로그램부

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)


# In[ ]:




