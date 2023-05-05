def add(a: int | float, b: int | float) -> int | float:
    return a + b

def sub(a: int | float, b: int | float) -> int | float:
    return a - b

def mul(a: int | float, b: int | float) -> int | float:
    return a * b

def div(a: int | float, b: int | float) -> int | float:
    return a / b

def mod(a: int | float, b: int | float) -> int | float:
    return a % b

def pow(a: int | float, b: int | float) -> int | float:
    return a ** b

def floordiv(a: int | float, b: int | float) -> int:
    return a // b

def neg(a: int | float) -> int | float:
    return -a

def pos(a: int | float) -> int | float:
    return +a

def abs(a: int | float) -> int | float:
    return a if a >= 0 else -a

def invert(a: int) -> int:
    return ~a

def lshift(a: int, b: int) -> int:
    return a << b

def rshift(a: int, b: int) -> int:
    return a >> b

def and_(a: int, b: int) -> int:
    return a & b

def or_(a: int, b: int) -> int:
    return a | b

def xor(a: int, b: int) -> int:
    return a ^ b

def lt(a: int | float, b: int | float) -> bool:
    return a < b

def le(a: int | float, b: int | float) -> bool:
    return a <= b

def eq(a: int | float, b: int | float) -> bool:
    return a == b

def ne(a: int | float, b: int | float) -> bool:
    return a != b

def gt(a: int | float, b: int | float) -> bool:
    return a > b

def ge(a: int | float, b: int | float) -> bool:
    return a >= b

def matmul(a: int | float, b: int | float) -> int | float:
    return a @ b
