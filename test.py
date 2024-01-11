import numpy as np

class Value:
    def __init__(self, data, _children) -> None:
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
    