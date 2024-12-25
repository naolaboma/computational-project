check = True
while check:
    # Defining equations to be solved
    # in diagonally dominant form
    print("\n\n*** JACOBI ITERATIVE TECHNIQUES ***")
    def f1(x, y, z, w): return (6+y-2*z)/10
    def f2(x, y, z, w): return (25+x+z-3*w)/11
    def f3(x, y, z, w): return (-11-2*x+y+w)/10
    def f4(x, y, z, w): return (15-3*y+z)/8

    # Initial setup
    x0 = 0
    y0 = 0
    z0 = 0
    w0 = 0
    count = 1

    # Reading tolerable error
    e = float(input('Enter tolerable error: '))

    # Implementation of Jacobi Iteration
    print('\nCount\tx\ty\tz\tw\n')

    condition = True

    while condition:
        x1 = f1(x0, y0, z0, w0)
        y1 = f2(x0, y0, z0, w0)
        z1 = f3(x0, y0, z0, w0)
        w1 = f4(x0, y0, z0, w0)
        print('%d\t%0.4f\t%0.4f\t%0.4f\t %0.4f\n' % (count, x1, y1, z1, w1))
        e1 = abs(x0-x1)
        e2 = abs(y0-y1)
        e3 = abs(z0-z1)
        e4 = abs(w0-w1)

        count += 1
        x0 = x1
        y0 = y1
        z0 = z1
        w0 = w1

        condition = e1 > e and e2 > e and e3 > e and e4 > e

    print('\nSolution: x = %0.3f, y = %0.3f , z = %0.3f and w = %0.3f\n' %
          (x1, y1, z1, w1))
    check = False

    st = input("Press any key to continue ... ")
    check = True
