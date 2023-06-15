import numpy

N_OF_EXAMPLES = 4


def print_equations(A, b):
    print("Równania, które rozwiązujemy:")
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(f"{A[i, j]}x{j + 1}")
        print(" + ".join(row), "=", b[i])
    print()


def print_results(x):
    n = len(x)
    temp_str = ""
    for i in range(n):
        temp_str += f"x{i+1} = {round(x[i])} | "
    print(temp_str)


def get_example(n):
    e1 = (numpy.array([[10., -1., 2., 0.],
                       [-1., 11., -1., 3.],
                       [2., -1., 10., -1.],
                       [0.0, 3., -1., 8.]]),
          numpy.array([6., 25., -11., 15.]))
    e2 = (numpy.array([[2., 1.],
                       [1., 2.]]),
          numpy.array([8., 1.]))
    e3 = (numpy.array([[2., 1., 1.],
                       [3., 5., 2.],
                       [2., 1., 4.]]),
          numpy.array([5., 15., 8.]))
    e4 = (numpy.array([[3., 1., 1.],
                       [1., 4., 2.],
                       [1., 2., 5.]]),
          numpy.array([7., 13., 15.]))

    examples = [e1, e2, e3, e4]

    return examples[n - 1][0], examples[n-1][1]