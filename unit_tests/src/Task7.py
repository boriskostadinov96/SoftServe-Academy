# Given two lines, determine whether or not they are parallel.
# Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.

def lines_are_parallel(first_line, second_line):
    if first_line[0] / first_line[1] == second_line[0] / second_line[1]:
        return True
    else:
        return False
