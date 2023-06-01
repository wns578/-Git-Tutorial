#!/usr/bin/env python
# coding: utf-8

# In[23]:


import os
import pickle

filepath = 'data/score.bin'

def input_scores():
    scores = []
    m=1
    while True:
        score = int(input(f'#{m}? '))
        m=m+1
        if score < 0:
            break
        scores.append(score)
    return scores


def get_average(scores):
    aver=0
    k = len(scores)
    for i in scores :
        aver=aver+i
    aver= aver/k
    
    return aver
    
def show_scores(scores):
    print('개인 점수: ',end='')
    for i in range(len(scores)) :
        print(scores[i],end=' ')
    a=get_average(scores)
    print()
    print(f'평균: {a:.1f}')    
    


def save_scores(scores):
    with open(filepath, "wb") as file:
        pickle.dump(scores, file)


def load_scores():
    with open(filepath, "rb") as file:
        scores = pickle.load(file)
    return scores


if os.path.exists(filepath) :
    scores = load_scores()
    print("[파일읽기]")
    
else:
    print("[점수 입력]")
    scores = input_scores()

average = get_average(scores)

print("\n[점수 출력]")
show_scores(scores)

save_scores(scores)


# In[ ]:




