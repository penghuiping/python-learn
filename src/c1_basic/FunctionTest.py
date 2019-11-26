# encoding=utf8

# 普通函数
def my_print():
    print("hello")


my_print()


# 函数返回多个值

def pointAdd1(x, y):
    return x + 1, y + 1


print("函数可以返回多个值:", pointAdd1(1, 2))


# 内部函数
def my_print2():
    def test():
        print("hello")

    test()


my_print2()


# 匿名函数lambda
def add(x1, y1):
    f = lambda x, y: x + y
    return f(x1, y1)


print(add(1, 2))
