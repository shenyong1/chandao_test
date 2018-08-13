# -*- coding:utf-8 -*-
iterable = [1,2,33,'dfssa','呵呵',324]
# [print(iter_var) for iter_var in iterable]


def add(x):
    return x*x

res = list(map(add,map(add,[10,2])))
print(res)


