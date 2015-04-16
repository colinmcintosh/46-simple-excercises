# problem02.py


"""
    Problem 2:
        Define a function max_of_three() that takes three numbers as arguments
        and returns the largest of them.
        
"""

def max_of_three(x, y, z):
    if z <= x >= y:
        return x
    elif z <= y >= x:
        return y
    else:
        return z


def test():
    print(max_of_three(10, 10, 20))


if __name__ == "__main__":
    test()
