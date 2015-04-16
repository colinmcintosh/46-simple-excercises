# problem03.py


"""
    Problem 3:
        Define a function that computes the length of a given list or string.
	(It is true that Python has the len() function built in, but writing
	it yourself is nevertheless a good exercise.)
"""

def len(obj):
    x = 0
    for _ in obj:
        x += 1
    return x


def test():
    print(len)
    print(len([1,2,3,4,4,5]))
    print(len([]))


if __name__ == "__main__":
    test()
