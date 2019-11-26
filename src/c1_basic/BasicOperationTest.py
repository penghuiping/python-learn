# coding=utf-8

# 进制
print("2进制表示:", 0b1111)
print("10进制表示", 15)
print("16进制表示:", 0xF)

# 打印二进制与16进制
print(bin(15))
print(hex(15))

# 基本运算
print("加法:", 1 + 1)
print("减肥:", 2 - 1)
print("乘法:", 2 * 2)
print("除法:", 3 / 2)
print("指数:", 2 ** 2)
print("取模:", 3 % 2)

# 位运算
print("左移前:", bin(-1), "左移后:", bin(-1 << 3))
print("右移前:", bin(0b1111), "右移后", bin(0b1111 >> 3))

# 与、或、非、异或运算
print("与操作", bin(0b1111 & (0b1000 - 0b0001)))
print("或操作", bin(0b0111 | 0b1000))
print("非操作", bin(~0b1110))  # 注意这里是补码 原码=按位取反(无符号补码)+1
print("异或操作", bin(0b11 ^ 0b10))

# 变量与常量
a = 1
b = "hello world"
c = 1.0
f = 'c'

# 条件分支
a = 1
if a > 0:
    print("a>0")
elif a == 0:
    print("a=0")
else:
    print("a<0")

# 循环for
for i in range(10):
    print(i, end=' ')

print()

for i in range(2, 10):
    print(i, end=' ')

# 循环while
print('\n')
i = 0
while True:
    if i > 10:
        break
    else:
        i = i + 1
        print(i, end=' ')

