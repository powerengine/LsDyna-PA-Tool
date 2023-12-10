# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:05:53 2023

@author: USER
"""

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# 윈도우 생성
root = tk.Tk()
root.title("awdark 테마 예제")

# ThemedStyle을 사용하여 새로운 테마 생성
#root.tk.call("package", "require", 'awdark')
style = ThemedStyle(root)
style.set_theme("equilux")

# 버튼 클릭 시 실행할 함수 정의
def button_click():
    print("버튼이 클릭되었습니다!")

# 버튼 생성
button = ttk.Button(root, text="클릭!", command=button_click)
button.pack()

# GUI 실행
root.mainloop()

