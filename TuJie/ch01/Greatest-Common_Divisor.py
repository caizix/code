Num_1 = int(input('请输入第一个整数：'))
Num_2 = int(input('请输入第二个整数：'))

if Num_1 < Num_2:
    Tmp_Num = Num_1
    Num_1 = Num_2
    Num_2 = Tmp_Num
while Num_2 != 0:
    Tmp_Num = Num_1 % Num_2
    Num_1 = Num_2
    Num_2 = Tmp_Num

print('最大公约数（g.c.d）:',Num_1)