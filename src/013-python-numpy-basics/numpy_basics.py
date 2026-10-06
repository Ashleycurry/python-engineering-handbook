"""创建、切片、变形、合并和拆分 NumPy 数组。"""

import numpy as np


def main() -> None:
    """运行与课程主题对应的、结果可复现的数组操作案例。"""
    vector = np.array([1, 2, 3], dtype=int)
    zeros = np.zeros(3, dtype=int)
    matrix = np.arange(1, 7).reshape(2, 3)
    random_state = np.random.RandomState(7)
    random_integers = random_state.randint(0, 10, size=4)

    print("Vector:", vector)
    print("Zeros:", zeros)
    print("Matrix:\n{}".format(matrix))
    print("Random integers:", random_integers)

    print("Single value:", matrix[0, 1])
    print("Slice:\n{}".format(matrix[:, 1:]))
    print("Boolean subset:", vector[vector > 1])
    print("Independent copy:", matrix[:1].copy())

    print("Transpose:\n{}".format(matrix.T))
    print("Reshaped:\n{}".format(vector.reshape(3, 1)))
    print("Concatenated:", np.concatenate((vector, [4])))
    print("Vertical stack:\n{}".format(np.vstack((matrix, matrix))))
    print("Horizontal stack:\n{}".format(np.hstack((matrix, matrix))))

    left, right = np.hsplit(matrix, [1])
    top, bottom = np.vsplit(matrix, [1])
    print("Horizontal split:\n{}\n{}".format(left, right))
    print("Vertical split:\n{}\n{}".format(top, bottom))


if __name__ == "__main__":
    main()
