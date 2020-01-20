import abc

class Expression():
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    def calc(self):
        return self.value
    



class Const(Expression):
    def __init__(self, value):
        super().__init__()
        self.value = value

class Plus(Expression):
    def __init__(self, left = None, right = None):
        super().__init__(left, right)

    def calc(self):
        return self.left.calc() + self.right.calc()

class Minus(Expression):
    def __init__(self, left = None, right = None):
        super().__init__(left, right)

    def calc(self):
        return self.left.calc() - self.right.calc()

class Div(Expression):
    def __init__(self, left = None, right = None):
        super().__init__(left, right)

    def calc(self):
        return self.left.calc() / self.right.calc()

class M(Expression):
    def __init__(self, left = None, right = None):
        super().__init__(left, right)

    @abc.abstractmethod
    def calc(self):
        return self.left.calc() / self.right.calc()

def str_to_tree(expr):
    plus_index = expr.find('+')
    if plus_index != -1:
        print(expr[:plus_index])
        print(expr[plus_index+1:])
        left = str_to_tree(expr[:plus_index])
        right = str_to_tree(expr[plus_index + 1:])
        return Plus(left, right)

    plus_index = expr.find('-')
    if plus_index != -1:
        print(expr[:plus_index])
        print(expr[plus_index + 1:])
        left = str_to_tree(expr[:plus_index])
        right = str_to_tree(expr[plus_index + 1:])
        return Minus(left, right)

    plus_index = expr.find('*')
    if plus_index != -1:
        print(expr[:plus_index])
        print(expr[plus_index + 1:])
        left = str_to_tree(expr[:plus_index])
        right = str_to_tree(expr[plus_index + 1:])
        return M(left, right)

    plus_index = expr.find('/')
    if plus_index != -1:
        print(expr[:plus_index])
        print(expr[plus_index + 1:])
        left = str_to_tree(expr[:plus_index])
        right = str_to_tree(expr[plus_index + 1:])
        return Div(left, right)
































