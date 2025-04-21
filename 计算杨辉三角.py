#免费使用，商用请注明来源
#Free for non-commercial use. For commercial purposes, please explicitly credit the source.
def c(a,b):
    if a == 1 and b == 1:
        return 1
    if a <= 0 or b <= 0:
        return 0
    return c(a-1,b)+c(a-1,b-1)
#以上杨辉三角算式

#一下为输出一定范围内杨辉三角表
for n in range(1,10):
    for a in range(n*2,30):
        print(" ",end="")
    for i in range(1,n+1):
        ass = c(n,i)
        asslen = len(str(ass))
        print(c(n,i),end="  ")
        if int(asslen) > 1:
            for b in range(1,asslen):
                print(" ",end="")
    print("")