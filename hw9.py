#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 연습문제 11,3

# 사용자 정의 함수부

class Point :
    def __init__(self, x=0, y=0) :
        self.__x=x
        self.__y=y
    
    def show(self) :
        print(f'({self.__x}, {self.__y})')
        
        
    def set(self, x, y) :
        self.__x=x
        self.__y=y
        
    def get(self) :
        return (self.__x,self.__y)




class Rectangle :
    
    
    def __init__(self, x1, y1, x2, y2) :
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
        
        self.__lt = Point(x1, y1)
        self.__rb = Point(x2, y2)

    def show(self) :
        print(f'좌측 상단 꼭지점이 {self.__lt.get()}이고 우측 상단 꼭짓점이 {self.__rb.get()}인 사각형입니다.')
        
    def getWidth(self) :
        w=self.__x2 - self.__x1
        return w
        
    def getHeight(self) :
        h=self.__y2 - self.__y1
        return h
    
    def getArea(self) :
        w = self.getWidth()
        h = self.getHeight()
        a = w * h
        return a
    
    def getPerimeter(self) :
        w = self.getWidth()
        h = self.getHeight()
        p= (w+h)*2
        return p
        

# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')


# In[ ]:




