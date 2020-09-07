#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
가위 바위 보 게임을 반복문을 사용하여 업그레이드
(끝나는 조건은 x나 q를 입력하면 종료)

끝날 때 결과에 ?승 ?패 출력
"""

# 가위 바위 보 프로그램
import random

rock = {1 : '가위', 2 : "바위", 3 : "보"}

while True:
    a = input("가위 바위 보 중 하나를 입력하세요 : ")
    if a == "x" or a =="q":
        break
    print(a)
    b = random.randint(1,3)
    c = rock[b]
    print("컴퓨터 :{0}".format(c))
    if a == "보" :
        if c == "바위" :
            print("사용자가 이겼습니다!")
        elif c == "가위" :
             print("컴퓨터가 이겼습니다.")
        else : print("비겼습니다.")
    elif a == "가위" :
        if c == "보" :
            print("사용자가 이겼습니다!")
        elif c == "바위" :
            print("컴퓨터가 이겼습니다.")
        else : print("비겼습니다.")

    elif a == "바위" :
        if c == "가위" :
            print("사용자가 이겼습니다!")
        elif c == "보" :
            print("컴퓨터가 이겼습니다.")
        else :
            print("비겼습니다.")
    else :
        print("다시 입력해 주세요")
    print(a)

        

