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

a = Value(5)
b = Value(3)
c = a * b
print(c.data)