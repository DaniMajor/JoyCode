class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Option():
    def __init__(self, state, left, right):
        self.state = state
        self.left = left
        self.right = right

class If(Option):
    def eval(self):
        if bool(self.state):
            return self.left.eval()
        elif self.state != 0:
            return self.left.eval()
        else:
            return self.right.eval()

class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class ID(BinaryOp):
    def eval(self):
        return self.right.eval()

class More(BinaryOp):
    def eval(self):
        return bool(self.left.eval() > self.right.eval())

class Less(BinaryOp):
    def eval(self):
        return bool(self.left.eval() < self.right.eval())



