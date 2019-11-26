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


# 反射获取类的信息
person = Person(12, "jack")
print(type(person))
print(isinstance(person, Person))

# 获取类的属性与方法
print("person类的属性与方法:", dir(person))

# 动态判断类是否具有某个属性
print("person类是否具有color属性:", hasattr(person, "color"))
print("person类是否具有age属性:", hasattr(person, "age"))

# 动态获取属性值
print("person类是age属性值为:{}".format(getattr(person, "age")))
print("person类是name属性值为:{}".format(getattr(person, "name")))

# 动态修改属性值
setattr(person, "age", 18)
print("person类动态修改age属性值后:{}".format(getattr(person, "age")))
