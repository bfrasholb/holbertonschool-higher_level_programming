#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(0, len(matrix[0])):
            print("{}".format(matrix[i][j]), end=" ")
        print()
