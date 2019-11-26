# encoding utf8

# 创建类
class Person:
    age = None
    name = None

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self) -> str:
        return "name:{},age:{}".format(self.name, self.age)

    def doing(self):
        pass


# 接口
class Doable:
    def doing(self):
        pass


# 继承
class Singer(Person, Doable):

    def __init__(self, age, name):
        super().__init__(age, name)

    def doing(self):
        print("我在唱歌")


class Drawer(Person, Doable):
    def __init__(self, age, name):
        super().__init__(age, name)

    def doing(self):
        print("我在画画")


singer = Singer(22, "jack")
drawer = Drawer(20, "mary")

print(singer)

print(drawer)


# 多态
def do(person):
    person.doing()


do(singer)
do(drawer)
