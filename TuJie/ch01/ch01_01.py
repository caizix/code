def fib(n):	# 定义函数fib()
    if n==0 :
        return 0 # 如果n=0 则返回 0
    elif n==1 or n==2:
        return 1
    else:   # 否则返回 fib(n-1)+fib(n-2)
        return (fib(n-1)+fib(n-2))

n=int(input('请输入要计算第几项斐波拉契数列:'))
for i in range(n+1):# 计算前n项斐波拉契数列
    print('fib(%d)=%d' %(i,fib(i)))
