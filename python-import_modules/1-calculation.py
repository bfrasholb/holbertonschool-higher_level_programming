#!/usr/bin/python3


from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    func = [add, sub, mul, div]
    ops = ["+", "-", "*", "/"]

    a = 10
    b = 5

    for i in range(len(ops)):
        print("{} {} {} = {}".format(a, ops[i], b, func[i](a, b)))
