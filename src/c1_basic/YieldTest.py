# encoding=utf-8


def number(x):
    yield x + 1


def number1(x):
    return x + 1


# 可以看到return回的是一个int值
print(number1(1))

# 可以看到yield回的是generator对象
print(number(1))

# 获取generator对象的值需要调用next函数，这意味着调用next,函数才会执行
for i in range(10):
    print(next(number(i)))
