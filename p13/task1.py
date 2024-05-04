def add_sudtract(a: int, b: int, act: str):
    if act == "+":
        return a + b
    elif act == "-":
        return a - b


res: int = 0
a1: int = 12
a2: int = 6
act: str = '+'

res = add_sudtract(a1, a2, act)
print(res)