import numpy as np

class Value:
    def __init__(self, data) -> None:
        self.data = data
        self.grad = 0
    
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data)

        return out
    
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data)

        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "This operation only accepts int/float as second operator"

        out = Value(self.data ** other)
        return out

#testing stuff
if __name__ == "__main__":
    a = Value(5)
    b = Value(6)
    c = a ** b.data
    print(c.data)