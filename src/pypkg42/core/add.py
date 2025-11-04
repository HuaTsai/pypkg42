def add(a: int | float, b: int | float) -> int | float:
    return a + b


def add_multiple(*args: int | float) -> int | float:
    return sum(args)


if __name__ == "__main__":
    print("Hello world from add.py!")
