#frozenset 无序不重复且不可变  适合作dict的key
#set 的 update方法可用于合并两个set
set1 = set('abc')
set2 = set('cdef')
# set1.update(set2)
print(set1)

re1 = set1 - set2
re2 = set1 | set2
re3 = set1 & set2
print(re1,re2,re3)


d = {}
for i in range(100000):
    d[i] = str(i)

print(d)