import math


def sigmoid_scalar(x):
    y = 1 / (1 + math.exp(float(-x)))
    dy = y * (1 - y)
    return (y, dy)

def tanh_scalar(x):
    y = 1 - (2 / (math.exp(2 * float(x)) + 1))
    dy = 1 - y**2
    return (y, dy)


class Value:
    def __init__(self, data, _children=[], _op="") -> None:
        self.data = data
        self.grad = 0

        self._backward = lambda: None

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, [self, other], "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        
        self._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, [self, other], _op="*")

        def _backward():
            self.grad += other.grad * out.grad
            other.grad += self.grad * out.grad
        self._backward = _backward
        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "This operation only accepts int/float as second operator"

        out = Value(self.data ** other, [self, other], "**")
        return out
    
    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self, ), "relu")

        def _backward():
            self.grad += (self.data > 0) * out.grad
        self._backward = _backward
        
        return out
    
    def sigmoid(self):
        out = Value(sigmoid_scalar(self.data)[0], (self, ), "sigmoid")

        def _backward():
            self.grad += sigmoid_scalar(self.data)[1] * out.grad
        self._backward = _backward

        return out
    def tanh(self):
        out = Value(tanh_scalar(self.data)[0], (self, ), "tanh")

        def _backward():
            self.grad += tanh_scalar(self.data)[1] * out.grad
        self._backward = _backward

        return out    
    def backward(self):
        self.grad = 1

        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        for v in reversed(topo):
            v._backward()
        return

