# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import random


def one_step_sampling(distribution_function):

    F = distribution_function.cumsum()
    uniform_value = random.random()
    for i in range(len(F)):
        if uniform_value < F[i]:
            return i


def one_dimension_sampling(initial_state, distribution, transform_matrix):

    x = initial_state
    p = distribution
    q = transform_matrix

    steps = 1
    while steps < 100:
        yield x
        y = one_step_sampling(q[x])
        alpha = random.random()
        if alpha < min((p[y]*q[y][x] / (p[x]*q[x][y])), 1):
            x = y
            steps += 1
        else:
            continue


def one_dimension_pdf(x):
    """
    a simple one dimension man-made probability density function, 1/x^2, with x ranging from 0 -> inf.
    :param x: value of random variable
    :return: value of pdf
    """
    if x < 0:
        raise ValueError('argument must be 0 or positive real value.')
    elif x < 1:
        return 0
    else:
        return 1/x**2


def two_dimension_pdf(x, y):
    """
    a simple two dimension man-made pdf:
    :param x:
    :param y:
    :return:
    """




if __name__ == '__main__':

    # p = np.array([0.3, 0.3, 0.4])
    # q = np.array([[0.2, 0.2, 0.6],
    #               [0.4, 0.2, 0.4],
    #               [0.1, 0.7, 0.2]])
    # out = list(one_dimension_sampling(0, p, q))
    #
    # num = len(out)
    # x0 = out.count(0)
    # x1 = out.count(1)
    # x2 = out.count(2)
    #
    # print(float(x0)/num, float(x1)/num, float(x2)/num)



