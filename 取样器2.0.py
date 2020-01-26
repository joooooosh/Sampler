import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
import random


def fun1():
    index = random.randint(0, len(a) - 1)
    entry1.delete(0, END)
    bb = a[index]
    entry1.insert(10, bb)


a = ['李雪桐', '黄国栋', '高海鹏', '陈荣军', '唐朝阳', '张子晗', '黄诗懿', '贺馨月',
     '胡子翼', '李欣睿', '张曼笛', '李万宇', '孙静怡', '李文博', '方卓皓', '胡梦蝶',
     '刘青青', '尤可为', '谭沅媛', '孙嘉豪', '张雅雯', '樊儒毅', '黄骏杰', '李明睿',
     '占泽洲', '杨雪莉', '鲜雨珂', '谭政宇', '廖哲睿', '沈雨馨', '杨潍静', '周梦圆',
     '张楚君', '谭羽婷', '向怡', '吴欣', '张博', '邓子豪', '漆姝妤', '李诗语',
     '祁慧艳', '吴晋文', '陈双怡', '郑金诚', '钟华荣', '闫璃利', '陈智巍', '向天琪',
     '王烁', '蒋文武', '熊婧钰', '汤睿琪', '方洋', '秦舒懿', '喻明炜']

win = Tk()
win.title("决定命运的窗口")
win.geometry("350x200+450+200")

ft = tkfont.Font(size=80)
entry1 = Entry(win,
               font=ft,
               fg='red',
               width='6')
entry1.grid(row=1,
            column=10)

Button(win, text='下一位', command=fun1).grid(row=2, column=10, padx=5, pady=5)
Button(win, text="退出", command=win.quit).grid(row=3, column=10, padx=5, pady=5)

win.mainloop()
