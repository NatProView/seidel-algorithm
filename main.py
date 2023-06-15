from helper_functions import *

# Metoda Gaussa-Seidla
# W oparciu o: https://pl.wikipedia.org/wiki/Metoda_Gaussa-Seidla

# Program przyjmuje tylko macierze dominujące przekątniowo

max_iteration_limit = 1000
RTOL = 1e-8


def seidel_algorithm(A, b):
    # zaczynamy z macierzą wypełnioną zerami
    x = numpy.zeros_like(b)

    for count in range(max_iteration_limit):
        print(f"Iteracja nr {count}: {x}")
        x_new = numpy.zeros_like(x)

        for i in range(len(A)):
            s1 = numpy.dot(A[i, :i], x_new[:i])
            s2 = numpy.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        # sprawdzamy, czy wynik jest odpowiednio blisko
        if numpy.allclose(x, x_new, rtol=RTOL):
            print("Osiągnięto oczekiwane przybliżenie")
            return x

        # jeżeli nie, używamy nowego x i zaczynamy ponownie
        x = x_new


n = int(input(f"Podaj numer przykładu od 1 do {N_OF_EXAMPLES}"))
A, b = get_example(n)

print_equations(A, b)

x = seidel_algorithm(A, b)

print_results(x)
