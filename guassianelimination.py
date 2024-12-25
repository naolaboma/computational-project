# Importing NumPy Library
import numpy as np
import sys

while True:
    print("*** Gaussian Elimination ***")

    # Reading number of unknowns
    n = int(input('Enter the Number of Unknowns: '))

    # Making numpy array of n x n+1 size and initializing
    # to zero for storing augmented matrix
    a = np.zeros((n, n+1))

    # Making numpy array of n size and initializing
    # to zero for storing solution vector
    x = np.zeros(n)

    # Reading augmented matrix coefficients
    print('Enter the Augmented Matrix Coefficients:')
    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

    # Applying Gauss Elimination with Partial Pivoting
    for i in range(n):
        # Partial Pivoting
        max_row = i
        for k in range(i+1, n):
            if abs(a[k][i]) > abs(a[max_row][i]):
                max_row = k
        a[[i, max_row]] = a[[max_row, i]]

        if a[i][i] == 0.0:
            sys.exit('Division by zero is detected!')

        for j in range(i+1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x[n-1] = a[n-1][n] / a[n-1][n-1]

    for i in range(n-2, -1, -1):
        x[i] = a[i][n]

        for j in range(i+1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    # Displaying solution
    print('\nThe Required Solution is:')
    for i in range(1, n+1):
        print('X%d = %0.2f' % (i, x[i-1]), end='\t')

    st = input("\nPress 'q' to quit or any other key to continue: ")
    if st.lower() == 'q':
        break
