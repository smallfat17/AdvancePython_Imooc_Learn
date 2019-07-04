import bisect
from collections import deque

a = deque()
bisect.insort(a,1)
bisect.insort(a,5)
bisect.insort(a,2)
print(a)

print(dir(bisect))
print(bisect.__package__)