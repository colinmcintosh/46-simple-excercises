# problem01.py


"""
    Problem 1:
        
        Define a function max() that takes two numbers as arguments and returns
        the largest of them. Use the if-then-else construct available in Python.
        (It is true that Python has the max() function built in, but writing it
        yourself is nevertheless a good exercise.)
        
"""

def max(x, y):
    if x > y:
        return x
    return y


def test():
    print(max(10, 20))


if __name__ == "__main__":
    test()
