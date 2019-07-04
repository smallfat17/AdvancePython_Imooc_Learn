#__getattr__与 __getattribute__的区别
#__getattr__只有当找不到类属性的时候会调用
#__getattribute__是访问类所有属性的入口
class Person():
    def __init__(self,info={}):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    #尽量不去复写这个函数
    # def __getattribute__(self, item):
    #     return 'aaa'




import numbers
#访问类属性优先级
#属性描述符->对象的__dict__ -> 类的__dict__ -> 非属性描述符 -> __getattr__
class IntField:
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value
    def __delete__(self, instance):
        pass

class NonDataField:
    def __get__(self, instance, owner):
        pass

class Student:
    age = IntField()


if __name__ == '__main__':
    p1 = Student()
    p1.age = 18
    print(p1.__dict__)
    print(Student.__dict__)
    print(p1.age)
