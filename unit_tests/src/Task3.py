# A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x. Given a, b and c, you should return the number of solutions to the equation.

def solutions(a, b, c):
    if ((b * b) - (4 * a * c)) > 0:
        return 2
    elif ((b * b) - (4 * a * c)) == 0:
        return 1
    else:
        return 0
