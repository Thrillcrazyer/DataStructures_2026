"""
https://karpathy.github.io/2026/02/12/microgpt/
"""


import math
import random
class Value:
    __slots__ = ('data', 'grad', '_children', '_local_grads')

    def __init__(self, data, children=(), local_grads=()):
        self.data = data                # scalar value of this node calculated during forward pass
        self.grad = 0                   # derivative of the loss w.r.t. this node, calculated in backward pass
        self._children = children       # children of this node in the computation graph
        self._local_grads = local_grads # local derivative of this node w.r.t. its children

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data + other.data, (self, other), (1, 1))

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data * other.data, (self, other), (other.data, self.data))

    def __pow__(self, other): return Value(self.data**other, (self,), (other * self.data**(other-1),))
    def log(self): return Value(math.log(self.data), (self,), (1/self.data,))
    def exp(self): return Value(math.exp(self.data), (self,), (math.exp(self.data),))
    def relu(self): return Value(max(0, self.data), (self,), (float(self.data > 0),))
    def __neg__(self): return self * -1
    def __radd__(self, other): return self + other
    def __sub__(self, other): return self + (-other)
    def __rsub__(self, other): return other + (-self)
    def __rmul__(self, other): return self * other
    def __truediv__(self, other): return self * other**-1
    def __rtruediv__(self, other): return other * self**-1

    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._children:
                    build_topo(child)
                topo.append(v)
        build_topo(self)
        print("TOPO:", [v.data for v in topo])  # Debug: Print the topological order of nodes
        self.grad = 1
        for v in reversed(topo):
            for child, local_grad in zip(v._children, v._local_grads):
                child.grad += local_grad * v.grad
                

                
if __name__ == "__main__":
    def almost_equal(left, right, tol=1e-9):
        return abs(left - right) <= tol

    def evaluate_case_1():
        a = Value(2.0)
        b = Value(3.0)

        c = a * b
        d = a + b
        e = c * d
        e.backward()

        return (e.data, a.grad, b.grad)

    def evaluate_case_2():
        x = Value(1.5)
        y = Value(-0.75)
        z = Value(2.0)

        nonlinear = (
            ((x + z) * (2 * y)) / (z ** 2)
            + (5 + x).log()
            - (-y)
            + (5 - x).relu()
            + (x * y).exp()
            + (10 / (z + 3))
        )

        result = nonlinear - (x / (z + 1)) + (4 - y)
        result.backward()

        return (result.data, x.grad, y.grad, z.grad)

    test_cases = [
        {
            "name": "Case 1",
            "description": "Basic graph: ((a * b) * (a + b))",
            "expected": (30.0, 21.0, 16.0),
            "actual": evaluate_case_1(),
        },
        {
            "name": "Case 2",
            "description": "Complex expression using all Value member operations",
            "expected": (
                9.88395464425994,
                -1.7979765300059416,
                2.2369787010375246,
                0.7041666666666666,
            ),
            "actual": evaluate_case_2(),
        },
    ]

    print("데이터 구조 및 알고리즘 실습 - 2026/04/30 - Practice: Autograd Test Cases\n")

    for test_case in test_cases:
        actual = test_case["actual"]
        expected = test_case["expected"]
        passed = all(almost_equal(actual_value, expected_value) for actual_value, expected_value in zip(actual, expected))

        print(f"{test_case['name']:<10}: {test_case['description']}")
        print(f"{'Expected Output':<15}: {expected}")

        if passed:
            print(f"{test_case['name']} 통과")
        else:
            print(f"{test_case['name']} 실패")

        print(f"{'Your Output':<15}: {actual}")
        print("-" * 30)