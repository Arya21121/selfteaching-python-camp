print("简易计算器，仅支持加减乘除")#界面提示
x=input('请输入第一个数字：')#输入第一个数字
m=int(x)#把输入的字符串转换成数字
b=input('请输入运算符仅支持+-*/:')#输入运算符
y=input('请输入第二个数字：')#输入第二个数字
n=int(y)#把输入的第二个字符串转换成数字
if b[0]=="+":
    c=m+n
else:
    if b[0]=="-":
        c=m-n
    else:
        if b[0]=="*":
            c=m*n
        else:
            c=m/n
print("结果是：",c,'\n')