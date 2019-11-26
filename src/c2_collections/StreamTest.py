# encoding=utf-8

import functools

# 流式编程 map/reduce/filter/sorted
print("map操作:{}".format(list(map(lambda x: x + 1, [1, 2, 3]))))

print("filter操作:{}".format(list(filter(lambda x: x % 2 == 0, [1, 2, 3]))))

print("sorted操作:{}".format(sorted([2, 6, 3, 2, 1], key=functools.cmp_to_key(lambda x, y: x - y), reverse=False)))

print("sum操作:{}".format(sum([1, 2, 3])))

print("reduce操作:{}".format(functools.reduce(lambda x, y: x * y, [1, 2, 3, 4])))
