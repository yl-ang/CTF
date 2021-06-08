def triangle(para1,para2):
    if para1<para2:
        iVar1 = 0
    else:
        if para1 == 1 and para2 == 1:
            iVar1 = 1
        else:
            if para2 == 1:
                iVar1 = triangle(para1 -1, para1 -1)
            else:
                iVar2 = triangle(para1,para2-1)
                iVar1 = triangle(para1-1,para2-1)
                iVar1 = iVar1 + iVar2
    return iVar1

num = 9
i = 1
while(i<=num):
    iVar3 = triangle(num,i)
    print(iVar3)
    i+=1