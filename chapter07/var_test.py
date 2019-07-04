a = [1,2,3]
b = a.copy()
a.append(4)
print(b)
print(a)

#小整合与短字符串再python中会创建全局唯一变量
a = 'abc'
b = 'abc'
print(id(a),id(b))#相等

a = 1100000000009
b = 1100000000009
print(id(a),id(b))#相等


# == 符号与 is 的区别
#==符号调用魔法函数 __eq__来判断是否相等
#is 调用id方法判断值是否指向同一个对象