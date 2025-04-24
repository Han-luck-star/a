
#学校作业，此文件免费使用，无附加要求，商用请告知一下
#School Assignment - This file is free to use with no additional requirements. Please inform the creator if used for commercial purposes.

def is_ana(a,b):
    a = a.lower()
    b = b.lower()
    testc = False
    if len(a) <= 0 or len(b) <= 0:
        if len(a) == len(b) == 0:
            print("符合Anagram规则")
            return
        else:
            print("两词字符数量不匹配")
            return
    for i in range(len(a)):
        for n in range(len(b)):
            if a[i] == b[n]:
                testc = True
                return is_ana(a[:i]+a[i+1:],b[:n]+b[n+1:])
    if testc == False:
        print("!不符合Anagram规则")
is_ana("hello","heLLo")    
#调用函数，用（“the eyes”，“they see”）和（“hello”，“world”）调用程序
is_ana("hello","world")
is_ana("the eyes","they see")
