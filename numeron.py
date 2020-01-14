# coding:utf-8
import numpy as np


def get_random_num():
    answear = np.array(range(1, 10))
    answear = np.random.permutation(answear)
    return str(answear[0]) + str(answear[1]) + str(answear[2])


def evaluate(input_, answear):
    list_input = np.zeros(len(input_))
    list_answear = np.zeros(len(input_))
    for i in range(len(input_)):
        list_input[i] = input_[i]
        list_answear[i] = answear[i]

    ball = len(np.intersect1d(list_input, list_answear))
    hit = 0
    for i in range(len(list_input)):
        if list_input[i] == list_answear[i]:
            hit += 1
            ball -= 1
    return hit, ball
