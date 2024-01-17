import numpy as np

class Value:
    def __init__(self, data, _children=[], _op="") -> None:
        self.data = data
        self.grad = 0

        self._backward = lambda: None

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, [self, other], "+")

        def _backward():
            return ()
        self._backward =
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, [self, other], _op="*")

        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "This operation only accepts int/float as second operator"

        out = Value(self.data ** other, [self, other], "**")
        return out
    def backward(self):
        self.grad = 1

        return


#testing stuff
if __name__ == "__main__":
    a = Value(5)
    b = Value(6)
    c = a ** b.data
    print(c.data)